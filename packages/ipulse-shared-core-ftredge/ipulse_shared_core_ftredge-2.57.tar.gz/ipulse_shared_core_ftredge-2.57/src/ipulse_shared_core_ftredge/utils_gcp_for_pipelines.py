# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
# pylint: disable=line-too-long
# pylint: disable=unused-variable
import json
import os
import time
from ipulse_shared_core_ftredge.enums.enums_common_utils import LogLevel
from .utils_custom_logs import ContextLog
from ipulse_shared_core_ftredge.utils_pipelinemon import Pipelinemon

############################################################################
##################### SETTING UP LOGGER ##########################

####DEPCREACATED: THIS APPROACH WAS GOOD, BUT ERRORS WERE NOT REPORTED TO ERROR REPORTING
# logging.basicConfig(level=logging.INFO)
# logging_client = google.cloud.logging.Client()
# logging_client.setup_logging()
###################################


##### THIS APPROACH IS USED NOW ########
ENV = os.getenv('ENV', 'LOCAL').strip("'")


def write_json_to_gcs_in_pipeline( pipelinemon:Pipelinemon, storage_client, data, bucket_name, file_name,
                      file_exists_if_starts_with_prefix:str=None, overwrite_if_exists:bool=False, increment_if_exists:bool=False,
                      save_locally:bool=False, local_path=None,  max_retries:int=2, max_deletable_files:int=1):
    """Saves data to Google Cloud Storage and optionally locally.
    
    This function attempts to upload data to GCS. 
    - If the upload fails after retries and `save_locally` is True or `local_path` is provided, it attempts to save the data locally.
    - It handles file name conflicts based on these rules:
        - If `overwrite_if_exists` is True: 
            - If `file_exists_if_contains_substr` is provided, ANY existing file containing the substring is deleted, and the new file is saved with the provided `file_name`.
            - If `file_exists_if_contains_substr` is None, and a file with the exact `file_name` exists, it's overwritten.
        - If `increment_if_exists` is True:
            - If `file_exists_if_contains_substr` is provided, a new file with an incremented version is created ONLY if a file with the EXACT `file_name` exists.
            - If `file_exists_if_contains_substr` is None, a new file with an incremented version is created if a file with the exact `file_name` exists. 
            
        -If both overwrite_if_exists and increment_if_exists are provided as Ture, an exception will be raised.
    """

    with pipelinemon.context("write_json_to_gcs_in_pipeline"):
        # GCS upload exception
        gcs_upload_error = False
        # Input validation
        if overwrite_if_exists and increment_if_exists:
            pipelinemon.add_log(ContextLog(LogLevel.ERROR_CUSTOM, subject="Param validation", description="Both 'overwrite_if_exists' and 'increment_if_exists' cannot be True simultaneously."))
            gcs_upload_error=True
        if not isinstance(data, (list, dict, str)):
            pipelinemon.add_log(ContextLog(LogLevel.ERROR_CUSTOM,subject="Data validation", description="Unsupported data type. Data must be a list, dict, or str."))
            gcs_upload_error=True
        if max_deletable_files > 10:
            pipelinemon.add_log(ContextLog(LogLevel.ERROR_CUSTOM,subject="max_deletable_files", description="max_deletable_files should be less than 10 for safety. For more use another method."))
            gcs_upload_error=True

        # Prepare data
        if isinstance(data, (list, dict)):
            data_str = json.dumps(data, indent=2)
        else:
            data_str = data

        bucket = storage_client.bucket(bucket_name)
        base_file_name, ext = os.path.splitext(file_name)
        increment = 0
        attempts = 0
        success = False

        # GCS-related metadata
        gcs_path = None
        gcs_file_overwritten = False
        gcs_file_already_exists = False
        gcs_file_saved_with_increment = False
        gcs_file_exists_checked_on_name = file_name
        gcs_deleted_files=[]

        # Local file path
        local_path_final = None

        try:
            upload_allowed = True
            # --- Overwrite Logic ---
            if overwrite_if_exists:
                with pipelinemon.context("overwriting"):
                    if file_exists_if_starts_with_prefix:
                        gcs_file_exists_checked_on_name = file_exists_if_starts_with_prefix
                        blobs_to_delete = list(bucket.list_blobs(prefix=file_exists_if_starts_with_prefix))
                        if len(blobs_to_delete) > max_deletable_files:
                            pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_exists_if_starts_with_prefix, description=f"Prefix matched with {len(blobs_to_delete)} files in bucket {bucket_name}"))
                            #### Ensuring to quit the operation if too many files are found
                            raise Exception(f"Error: Attempt to delete {len(blobs_to_delete)} matched files, but limit is {max_deletable_files}.")
                        if blobs_to_delete:
                            gcs_file_already_exists = True
                            pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_exists_if_starts_with_prefix, description=f"Prefix matched with {len(blobs_to_delete)} files in bucket {bucket_name}"))
                            for blob in blobs_to_delete:
                                gcs_path_del = f"gs://{bucket_name}/{blob.name}"
                                pipelinemon.add_system_impacted(f"delete: gcs_bucket_file: {gcs_path_del}")
                                blob.delete()
                                pipelinemon.add_log(ContextLog(LogLevel.INFO_REMOTE_DELETE_COMPLETE, subject= gcs_path_del, description="file deleted from GCS as part of overwrite, matched with prefix"))
                                gcs_deleted_files.append(blob.name)
                            gcs_file_overwritten = True
                    else:
                        blob = bucket.blob(file_name)
                        if blob.exists():
                            gcs_file_already_exists = True
                            pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_name, description=f"Exact name matched with existing file in bucket {bucket_name}"))
                            gcs_path_del = f"gs://{bucket_name}/{file_name}"
                            pipelinemon.add_system_impacted(f"delete: gcs_bucket_file: {gcs_path_del}")
                            blob.delete()  # Delete the existing blob
                            pipelinemon.add_log(ContextLog(LogLevel.INFO_REMOTE_DELETE_COMPLETE, subject= gcs_path_del, description="file deleted from GCS as part of overwrite, matched with exact name"))
                            gcs_deleted_files.append(blob.name)
                            gcs_file_overwritten = True

            # --- Increment Logic ---
            elif increment_if_exists:
                with pipelinemon.context("incrementing"):
                    gcs_file_exists_checked_on_name = file_name  # We only increment if the exact name exists
                    while bucket.blob(file_name).exists():
                        gcs_file_already_exists = True
                        increment += 1
                        file_name = f"{base_file_name}_v{increment}{ext}"
                        gcs_file_saved_with_increment = True
                    if increment>0:
                        pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_name, description=f"File saved with incremented version in {bucket_name}"))

             # --- Check for Conflicts (Including Prefix) ---
            else:
                if file_exists_if_starts_with_prefix:
                    blobs_matched = list(bucket.list_blobs(prefix=file_exists_if_starts_with_prefix))
                    if blobs_matched:
                        upload_allowed = False
                        pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_exists_if_starts_with_prefix, description=f"Prefix matched with {len(blobs_matched)} existing files in bucket {bucket_name}."))
                    elif bucket.blob(file_name).exists():
                        pipelinemon.add_log(ContextLog(LogLevel.NOTICE_ALREADY_EXISTS, subject=file_name, description=f"Exact name matched with existing file in bucket {bucket_name}."))
                        upload_allowed = False

            # --- GCS Upload ---
            if overwrite_if_exists or increment_if_exists or upload_allowed:
                with pipelinemon.context("uploading"):
                    while attempts < max_retries and not success:
                        try:
                            gcs_path = f"gs://{bucket_name}/{file_name}"
                            blob = bucket.blob(file_name)  # Use the potentially updated file_name
                            pipelinemon.add_system_impacted(f"upload: gcs_bucket_file: {gcs_path}")
                            blob.upload_from_string(data_str, content_type='application/json')
                            pipelinemon.add_log(ContextLog(LogLevel.INFO_REMOTE_PERSISTNACE_COMPLETE, subject= gcs_path, description="file uploaded to GCS"))
                            success = True
                        except Exception as e:
                            attempts += 1
                            if attempts < max_retries:
                                time.sleep(2 ** attempts)
                            else:
                                pipelinemon.add_log(ContextLog(LogLevel.ERROR_EXCEPTION, e=e))
                                gcs_upload_error = True

        except Exception as e:
            pipelinemon.add_log(ContextLog(LogLevel.ERROR_EXCEPTION, e=e))
            gcs_upload_error = True

        # --- Save Locally ---
        ###### Not logging the local save operation in pipeline, as it is not a critical operation
        write_out=False
        if not success or gcs_upload_error or save_locally or local_path:
            try:
                local_path=local_path if local_path else "/tmp"
                local_path_final = os.path.join(local_path, file_name)

                if os.path.exists(local_path_final):
                    if increment_if_exists:
                        increment = 0
                        while os.path.exists(local_path_final):
                            increment += 1
                            local_path_final = os.path.join(local_path, f"{base_file_name}_v{increment}{ext}")
                        write_out=True
                    elif overwrite_if_exists:
                        write_out=True
                    else:
                        write_out=False
                else:
                    write_out=True

                if write_out:
                    with open(local_path_final, 'w', encoding='utf-8') as f:
                        f.write(data_str)

            except Exception as local_e:
                pipelinemon.add_log(ContextLog(LogLevel.WARNING_FIX_RECOMMENDED, e=local_e, description="Failed to write to local file"))

        # --- Return Metadata ---
        return {
            "gcs_path": gcs_path if success else None,  # Only set gcs_path if upload succeeded
            "local_path": local_path_final if write_out else None,  # Only set local_path if saved locally
            "gcs_file_already_exists": gcs_file_already_exists,
            "gcs_file_exists_checked_on_name":gcs_file_exists_checked_on_name ,
            "gcs_file_overwritten": gcs_file_overwritten,
            "gcs_deleted_file_names": ",,,".join(gcs_deleted_files) if gcs_deleted_files else None,
            "gcs_file_saved_with_increment": gcs_file_saved_with_increment
        }
