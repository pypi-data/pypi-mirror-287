# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
# pylint: disable=line-too-long
# pylint: disable=unused-variable
import json
import csv
from io import StringIO
import logging
import os
import time
import traceback
from google.cloud import error_reporting, logging as cloud_logging
from google.api_core.exceptions import NotFound


############################################################################
##################### SETTING UP LOGGER ##########################

####DEPCREACATED: THIS APPROACH WAS GOOD, BUT ERRORS WERE NOT REPORTED TO ERROR REPORTING
# logging.basicConfig(level=logging.INFO)
# logging_client = google.cloud.logging.Client()
# logging_client.setup_logging()
###################################


##### THIS APPROACH IS USED NOW ########
ENV = os.getenv('ENV', 'LOCAL').strip("'")

def setup_gcp_logger_and_error_report(logger_name,level=logging.INFO, use_cloud_logging=True):
    """Sets up a logger with Error Reporting and Cloud Logging handlers.

    Args:
        logger_name: The name of the logger.

    Returns:
        logging.Logger: The configured logger instance.
    """

    class ErrorReportingHandler(logging.Handler):
        def __init__(self, level=logging.ERROR):
            super().__init__(level)
            self.error_client = error_reporting.Client()
            self.propagate = True

        def emit(self, record):
            try:
                if record.levelno >= logging.ERROR:
                    message = self.format(record)
                    if record.exc_info:
                        message += "\n" + ''.join(traceback.format_exception(*record.exc_info))
                    if hasattr(record, 'pathname') and hasattr(record, 'lineno'):
                        message += f"\nFile: {record.pathname}, Line: {record.lineno}"
                    self.error_client.report(message)
            except Exception as e:
                # Ensure no exceptions are raised during logging
                self.handleError(record)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Add a console handler for local development
    if ENV == "LOCAL" or not use_cloud_logging:
        formatter = logging.Formatter('%(levelname)s : %(name)s : %(asctime)s : %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if use_cloud_logging:
        # Create Error Reporting handler
        error_reporting_handler = ErrorReportingHandler()

        # Create Google Cloud Logging handler
        cloud_logging_client = cloud_logging.Client()
        cloud_logging_handler = cloud_logging_client.get_default_handler()

        # Add handlers to the logger
        logger.addHandler(error_reporting_handler)
        logger.addHandler(cloud_logging_handler)
    return logger
############################################################################


############################################################################
##################### GOOGLE CLOUD STORAGE UTILS ##########################

def read_json_from_gcs(bucket_name, file_name, stor_client, logger):
    """ Helper function to read a JSON file from Google Cloud Storage """
    try:
        bucket = stor_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        data_string = blob.download_as_text()
        data = json.loads(data_string)
        return data
    except NotFound:
        logger.error(f"Error: The file {file_name} was not found in the bucket {bucket_name}.")
        return None
    except json.JSONDecodeError:
        logger.error(f"Error: The file {file_name} could not be decoded as JSON.")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)
        return None

def read_csv_from_gcs(bucket_name, file_name, storage_client, logger):
    """ Helper function to read a CSV file from Google Cloud Storage """
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        data_string = blob.download_as_text()
        data_file = StringIO(data_string)
        reader = csv.DictReader(data_file)
        return list(reader)
    except NotFound:
        logger.error(f"Error: The file {file_name} was not found in the bucket {bucket_name}.")
        return None
    except csv.Error:
        logger.error(f"Error: The file {file_name} could not be read as CSV.")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)
        return None



def write_json_to_gcs(bucket_name, storage_client, data, file_name,
                      save_locally=False, local_path=None, logger=None, max_retries=2,
                      overwrite_if_exists=False, increment_if_exists=False):
    """Saves data to Google Cloud Storage and optionally locally.

    This function attempts to upload data to GCS. If the upload fails after
    retries and `save_locally` is True or `local_path` is provided, it attempts
    to save the data locally.
    It also tries to handle file name conflicts by overwriting or incrementing. If both are provided as Ture, an exception will be raised.
    """

    def log_message(message):
        if logger:
            logger.info(message)

    def log_error(message, exc_info=False):
        if logger:
            logger.error(message, exc_info=exc_info)

    def log_warning(message):
        if logger:
            logger.warning(message)

    attempts = 0
    success = False
    gcs_path = None
    local_path_final = None
    gcs_file_overwritten = False
    gcs_file_already_exists = False
    gcs_file_saved_with_increment = False
    gcs_upload_exception = None  # Store potential GCS exception

    # Check for conflicting options
    if overwrite_if_exists and increment_if_exists:
        raise ValueError("When writing JSON to GCS, both overwrite and increment_if_exists cannot be True at the same time.")

    if isinstance(data, (list, dict)):
        data_str = json.dumps(data, indent=2)
    elif isinstance(data, str):
        data_str = data
    else:
        raise ValueError("Unsupported data type. It should be a list, dict, or str.")

    bucket = storage_client.bucket(bucket_name)
    base_file_name, ext = os.path.splitext(file_name)
    increment = 0

    while attempts < max_retries and not success:
        try:
            if increment_if_exists:
                while bucket.blob(file_name).exists():
                    gcs_file_already_exists = True
                    increment += 1
                    file_name = f"{base_file_name}_{increment}{ext}"
                    gcs_file_saved_with_increment = True
                    log_warning(f"File {file_name} already exists in bucket {bucket_name}. Writing with increment: {increment_if_exists}")
            else:
                blob = bucket.blob(file_name)

                # Check if the file exists
                if blob.exists():
                    gcs_file_already_exists = True
                    gcs_path = f"gs://{bucket_name}/{file_name}"
                    log_message(f"File {file_name} already exists in bucket {bucket_name}. Overwriting: {overwrite_if_exists}")
                    if not overwrite_if_exists:
                        log_warning(f"File {file_name} already exists and overwrite is set to False. Skipping save to GCS.")
                        break
                    else:
                        gcs_file_overwritten = True

            blob.upload_from_string(data_str, content_type='application/json')
            gcs_path = f"gs://{bucket_name}/{file_name}"
            log_message(f"Successfully saved file to GCS {gcs_path}.")
            success = True
        except Exception as e:
            gcs_upload_exception = e
            attempts += 1
            if attempts < max_retries:
                time.sleep(2 ** attempts)
            else:
                log_error(f"Failed to write {file_name} to GCS bucket {bucket_name} after {max_retries} attempts: {e}")

    if not success or save_locally or local_path:
        try:
            if not local_path:
                local_path_final = os.path.join("/tmp", file_name)
            else:
                local_path_final = os.path.join(local_path, file_name)

            if os.path.exists(local_path_final):
                if increment_if_exists:
                    increment = 0
                    while os.path.exists(local_path_final):
                        increment += 1
                        local_path_final = os.path.join(local_path, f"{base_file_name}_{increment}{ext}")
                elif not overwrite_if_exists:
                    log_message(f"File {file_name} already exists locally at {local_path_final} and overwrite is set to False. Skipping save.")
                    success = True
                else:
                    log_message(f"File {file_name} already exists locally at {local_path_final}. Overwriting: {overwrite_if_exists}")

            if not success:
                with open(local_path_final, 'w', encoding='utf-8') as f:
                    f.write(data_str)
                log_message(f"Saved {file_name} locally at {local_path_final}. Overwritten: {overwrite_if_exists}")
                success = True
        except Exception as local_e:
            log_error(f"Failed to write {file_name} locally: {local_e}", exc_info=True)

    if gcs_upload_exception is not None:
        raise gcs_upload_exception  # Propagate without nesting

    return {
        "gcs_path": gcs_path,
        "local_path": local_path_final,
        "gcs_file_already_exists": gcs_file_already_exists,
        "gcs_file_overwritten": gcs_file_overwritten,
        "gcs_file_saved_with_increment": gcs_file_saved_with_increment
    }


def write_csv_to_gcs(bucket_name, file_name, data, storage_client, logger,log_info_verbose=True):
    """ Helper function to write a CSV file to Google Cloud Storage """
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        data_file = StringIO()
        if data and isinstance(data, list) and isinstance(data[0], dict):
            fieldnames = data[0].keys()
            writer = csv.DictWriter(data_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        else:
            raise ValueError("Data should be a list of dictionaries")
        blob.upload_from_string(data_file.getvalue(), content_type='text/csv')
        if log_info_verbose:
            logger.info(f"Successfully wrote CSV to {file_name} in bucket {bucket_name}.")
    except ValueError as e:
        logger.error(f"ValueError: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while writing CSV to GCS: {e}", exc_info=True)
