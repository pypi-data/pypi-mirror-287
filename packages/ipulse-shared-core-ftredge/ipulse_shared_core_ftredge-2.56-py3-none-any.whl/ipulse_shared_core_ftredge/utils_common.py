# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=logging-fstring-interpolation
# pylint: disable=line-too-long
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
import traceback
import json
import uuid
from datetime import datetime, timezone
from contextlib import contextmanager
from typing import List
from google.cloud import logging as cloudlogging
from ipulse_shared_core_ftredge.enums.enums_common_utils import TargetLogs, LogLevel, LogStatus
from ipulse_shared_core_ftredge.utils_gcp import write_json_to_gcs


# ["data_import","data_quality", "data_processing","data_general","data_persistance","metadata_quality", "metadata_processing", "metadata_persistance","metadata_general"]

class ContextLog:
    MAX_FIELD_LINES = 26  # Define the maximum number of traceback lines to include
    MAX_FIELD_LENGTH=10000

    def __init__(self, level: LogLevel, base_context: str = None, collector_id: str = None,
                context: str = None, description: str = None,
                e: Exception = None, e_type: str = None, e_message: str = None, e_traceback: str = None,
                log_status: LogStatus = LogStatus.OPEN, subject: str = None, systems_impacted: List[str] = None
                ):
        if e is not None:
            e_type = type(e).__name__ if e_type is None else e_type
            e_message = str(e) if e_message is None else e_message
            e_traceback = traceback.format_exc() if e_traceback is None else e_traceback
        elif e_traceback is None and (e_type or e_message):
            e_traceback = traceback.format_exc()

        self.level = level
        self.subject = subject
        self.description = description
        self._base_context = base_context
        self._context = context
        self._systems_impacted = systems_impacted if systems_impacted else []
        self.collector_id = collector_id
        self.exception_type = e_type
        self.exception_message = e_message
        self.exception_traceback = e_traceback
        self.log_status = log_status
        self.timestamp = datetime.now(timezone.utc).isoformat()

    @property
    def base_context(self):
        return self._base_context

    @base_context.setter
    def base_context(self, value):
        self._base_context = value

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value

    @property
    def systems_impacted(self):
        return self._systems_impacted

    @systems_impacted.setter
    def systems_impacted(self, list_of_si: List[str]):
        self._systems_impacted = list_of_si

    def add_system_impacted(self, system_impacted: str):
        if self._systems_impacted is None:
            self._systems_impacted = []
        self._systems_impacted.append(system_impacted)

    def remove_system_impacted(self, system_impacted: str):
        if self._systems_impacted is not None:
            self._systems_impacted.remove(system_impacted)

    def clear_systems_impacted(self):
        self._systems_impacted = []

    def _format_traceback(self, e_traceback, e_message):
        if not e_traceback or e_traceback == 'None\n':
            return None

        traceback_lines = e_traceback.splitlines()

            # Check if the traceback is within the limits
        if len(traceback_lines) <= self.MAX_FIELD_LINES and len(e_traceback) <= self.MAX_FIELD_LENGTH:
            return e_traceback

        # Remove lines that are part of the exception message if they are present in traceback
        message_lines = e_message.splitlines() if e_message else []
        if message_lines:
            for message_line in message_lines:
                if message_line in traceback_lines:
                    traceback_lines.remove(message_line)

        # Filter out lines from third-party libraries (like site-packages)
        filtered_lines = [line for line in traceback_lines if "site-packages" not in line]

        # If filtering results in too few lines, revert to original traceback
        if len(filtered_lines) < 2:
            filtered_lines = traceback_lines

        # Combine standalone bracket lines with previous or next lines
        combined_lines = []
        for line in filtered_lines:
            if line.strip() in {"(", ")", "{", "}", "[", "]"} and combined_lines:
                combined_lines[-1] += " " + line.strip()
            else:
                combined_lines.append(line)

            # Ensure the number of lines doesn't exceed MAX_TRACEBACK_LINES
        if len(combined_lines) > self.MAX_FIELD_LINES:
            keep_lines_start = min(self.MAX_FIELD_LINES // 2, len(combined_lines))
            keep_lines_end = min(self.MAX_FIELD_LINES // 2, len(combined_lines) - keep_lines_start)
            combined_lines = (
                combined_lines[:keep_lines_start] +
                ['... (truncated) ...'] +
                combined_lines[-keep_lines_end:]
            )

        formatted_traceback = '\n'.join(combined_lines)

        # Ensure the total length doesn't exceed MAX_TRACEBACK_LENGTH
        if len(formatted_traceback) > self.MAX_FIELD_LENGTH:
            truncated_length = self.MAX_FIELD_LENGTH - len('... (truncated) ...')
            half_truncated_length = truncated_length // 2
            formatted_traceback = (
                formatted_traceback[:half_truncated_length] +
                '\n... (truncated) ...\n' +
                formatted_traceback[-half_truncated_length:]
            )
        return formatted_traceback

    def to_dict(self, max_field_len:int =10000, size_limit:float=256 * 1024 * 0.80):
        size_limit = int(size_limit)  # Ensure size_limit is an integer

        # Unified list of all fields
        systems_impacted_str = f"{len(self.systems_impacted)} system(s): " + " ,,, ".join(self.systems_impacted) if self.systems_impacted else None
        fields = [
            ("log_status", str(self.log_status.name)),
            ("level_code", self.level.value),
            ("level_name", str(self.level.name)),
            ("base_context", str(self.base_context)),
            ("timestamp", str(self.timestamp)),
            ("collector_id", str(self.collector_id)),
            ("systems_impacted", systems_impacted_str),
            ("context", str(self.context)),  # special sizing rules apply to it
            ("subject", str(self.subject)),
            ("description", str(self.description)),
            ("exception_type", str(self.exception_type)),
            ("exception_message", str(self.exception_message)),
            ("exception_traceback", str(self._format_traceback(self.exception_traceback,self.exception_message)))
        ]

        # Function to calculate the byte size of a JSON-encoded field
        def field_size(key, value):
            return len(json.dumps({key: value}).encode('utf-8'))

        # Function to truncate a value based on its type
        # Function to truncate a value based on its type
        def truncate_value(value, max_size):
            if isinstance(value, str):
                half_size = max_size // 2
                return value[:half_size] + '...' + value[-(max_size - half_size - 3):]
            return value

         # Ensure no field exceeds max_field_len
        for i, (key, value) in enumerate(fields):
            if isinstance(value, str) and len(value) > max_field_len:
                fields[i] = (key, truncate_value(value, max_field_len))

        # Ensure total size of the dict doesn't exceed size_limit
        total_size = sum(field_size(key, value) for key, value in fields)
        log_dict = {}
        truncated = False

        if total_size > size_limit:
            truncated = True
            remaining_size = size_limit
            remaining_fields = len(fields)

            for key, value in fields:
                if remaining_fields > 0:
                    max_size_per_field = remaining_size // remaining_fields
                else:
                    max_size_per_field = 0

                field_sz = field_size(key, value)
                if field_sz > max_size_per_field:
                    value = truncate_value(value, max_size_per_field)
                    field_sz = field_size(key, value)

                log_dict[key] = value
                remaining_size -= field_sz
                remaining_fields -= 1
        else:
            log_dict = dict(fields)

        log_dict['trunc'] = truncated

        return log_dict

class Pipelinemon:
    ERROR_START_CODE = LogLevel.ERROR.value
    WARNING_START_CODE = LogLevel.WARNING.value
    NOTICE_START_CODE = LogLevel.NOTICE.value
    SUCCESS_START_CODE = LogLevel.SUCCESS.value
    INFO_START_CODE = LogLevel.INFO.value

    def __init__(self, base_context: str, target_logs: TargetLogs = TargetLogs.MIXED, logger_name=None, max_log_field_size:int =10000, max_log_dict_size:float=256 * 1024 * 0.80):
        self._id = str(uuid.uuid4())
        self._logs = []
        self._early_stop = False
        self._errors_count = 0
        self._warnings_count = 0
        self._notices_count = 0
        self._successes_count = 0
        self._infos_count = 0
        self._systems_impacted = []
        self._level_counts = {level.name: 0 for level in LogLevel}
        self._base_context = base_context
        self._context_stack = []
        self._target_logs = target_logs.value
        self._logger = self._initialize_logger(logger_name)
        self._max_log_field_size = max_log_field_size
        self._max_log_dict_size = max_log_dict_size

    def _initialize_logger(self, logger_name):
        if logger_name:
            logging_client = cloudlogging.Client()
            return logging_client.logger(logger_name)
        return None

    @contextmanager
    def context(self, context):
        self.push_context(context)
        try:
            yield
        finally:
            self.pop_context()

    def push_context(self, context):
        self._context_stack.append(context)

    def pop_context(self):
        if self._context_stack:
            self._context_stack.pop()

    @property
    def current_context(self):
        return " >> ".join(self._context_stack)

    @property
    def base_context(self):
        return self._base_context

    @property
    def id(self):
        return self._id

    @property
    def systems_impacted(self):
        return self._systems_impacted

    @systems_impacted.setter
    def systems_impacted(self, list_of_si: List[str]):
        self._systems_impacted = list_of_si

    def add_system_impacted(self, system_impacted: str):
        if self._systems_impacted is None:
            self._systems_impacted = []
        self._systems_impacted.append(system_impacted)

    def clear_systems_impacted(self):
        self._systems_impacted = []

    @property
    def max_log_field_size(self):
        return self._max_log_field_size

    @max_log_field_size.setter
    def max_log_field_size(self, value):
        self._max_log_field_size = value

    @property
    def max_log_dict_size(self):
        return self._max_log_dict_size

    @max_log_dict_size.setter
    def max_log_dict_size(self, value):
        self._max_log_dict_size = value

    @property
    def early_stop(self):
        return self._early_stop

    def set_early_stop(self, max_errors_tolerance: int, create_error_log=True, pop_context=False):
        self._early_stop = True
        if create_error_log:
            if pop_context:
                self.pop_context()
            self.add_log(ContextLog(level=LogLevel.ERROR_PIPELINE_THRESHOLD_REACHED,
                                    subject="EARLY_STOP",
                                    description=f"Total MAX_ERRORS_TOLERANCE of {max_errors_tolerance} has been reached."))

    def reset_early_stop(self):
        self._early_stop = False


    def add_log(self, log: ContextLog, ):
        if (self._target_logs == TargetLogs.SUCCESSES and log.level >=self.NOTICE_START_CODE) or \
           (self._target_logs == TargetLogs.WARNINGS_AND_ERRORS and log.level.value < self.WARNING_START_CODE):
            raise ValueError(f"Invalid log level {log.level.name} for Pipelinemon target logs setup: {self._target_logs}")
        log.base_context = self.base_context
        log.context = self.current_context
        log.collector_id = self.id
        log.systems_impacted = self.systems_impacted
        log_dict = log.to_dict(max_field_len=self.max_log_field_size, size_limit=self.max_log_dict_size)
        self._logs.append(log_dict)
        self._update_counts(log_dict)

        if self._logger:
            # We specifically want to avoid having an ERROR log level for this structured Pipelinemon reporting, to ensure Errors are alerting on Critical Application Services.
            # A single ERROR log level can be used for the entire pipeline, which shall be used at the end of the pipeline
            if log.level.value >= self.WARNING_START_CODE:
                self._logger.log_struct(log_dict, severity="WARNING")
            elif log.level.value >= self.NOTICE_START_CODE:
                self._logger.log_struct(log_dict, severity="NOTICE")
            else:
                self._logger.log_struct(log_dict, severity="INFO")

    def add_logs(self, logs: List[ContextLog]):
        for log in logs:
            self.add_log(log)

    def clear_logs_and_counts(self):
        self._logs = []
        self._errors_count = 0
        self._warnings_count = 0
        self._notices_count = 0
        self._successes_count = 0
        self._infos_count = 0
        self._level_counts = {level.name: 0 for level in LogLevel}

    def clear_logs(self):
        self._logs = []

    def get_all_logs(self):
        return self._logs

    def get_logs_for_level(self, level: LogLevel):
        return [log for log in self._logs if log["level_code"] == level.value]

    def get_logs_by_str_in_context(self, context_substring: str):
        return [
            log for log in self._logs
            if context_substring in log["context"]
        ]

    def contains_errors(self):
        return self._errors_count > 0

    def count_errors(self):
        return self._errors_count

    def contains_warnings_or_errors(self):
        return self._warnings_count > 0 or self._errors_count > 0

    def count_warnings_and_errors(self):
        return self._warnings_count + self._errors_count

    def count_warnings(self):
        return self._warnings_count

    def count_notices(self):
        return self._notices_count

    def count_successes(self):
        return self._successes_count

    def count_successes_with_notice(self):
        return self.count_logs_by_level(LogLevel.SUCCESS_WITH_NOTICES)

    def count_successes_no_notice(self):
        return self.count_logs_by_level(LogLevel.SUCCESS)

    def count_infos(self):
        return self._infos_count

    def count_all_logs(self):
        return len(self._logs)

    def count_logs_by_level(self, level: LogLevel):
        return self._level_counts.get(level.name, 0)

    def _count_logs(self, context_substring: str, exact_match=False, level_code_min=None, level_code_max=None):
        return sum(
            1 for log in self._logs
            if (log["context"] == context_substring if exact_match else context_substring in log["context"]) and
               (level_code_min is None or log["level_code"] >= level_code_min) and
               (level_code_max is None or log["level_code"] <= level_code_max)
        )

    def count_logs_for_current_context(self):
        return self._count_logs(self.current_context, exact_match=True)

    def count_logs_for_current_and_nested_contexts(self):
        return self._count_logs(self.current_context)

    def count_logs_by_level_for_current_context(self, level: LogLevel):
        return self._count_logs(self.current_context, exact_match=True, level_code_min=level.value, level_code_max=level.value)

    def count_logs_by_level_for_current_and_nested_contexts(self, level: LogLevel):
        return self._count_logs(self.current_context, level_code_min=level.value, level_code_max=level.value)

    def count_errors_for_current_context(self):
        return self._count_logs(self.current_context, exact_match=True, level_code_min=self.ERROR_START_CODE)

    def count_errors_for_current_and_nested_contexts(self):
        return self._count_logs(self.current_context, level_code_min=self.ERROR_START_CODE)

    def count_warnings_and_errors_for_current_context(self):
        return self._count_logs(self.current_context, exact_match=True, level_code_min=self.WARNING_START_CODE)

    def count_warnings_and_errors_for_current_and_nested_contexts(self):
        return self._count_logs(self.current_context, level_code_min=self.WARNING_START_CODE)

    def count_warnings_for_current_context(self):
        return self._count_logs(self.current_context, exact_match=True, level_code_min=self.WARNING_START_CODE, level_code_max=self.ERROR_START_CODE - 1)

    def count_warnings_for_current_and_nested_contexts(self):
        return self._count_logs(self.current_context, level_code_min=self.WARNING_START_CODE, level_code_max=self.ERROR_START_CODE - 1)

    def count_notices_for_current_context(self):
        return self._count_logs(self.current_context, exact_match=True, level_code_min=self.NOTICE_START_CODE, level_code_max=self.WARNING_START_CODE-1)

    def count_notices_for_current_and_nested_contexts(self):
        return self._count_logs(self.current_context, level_code_min=self.NOTICE_START_CODE, level_code_max=self.WARNING_START_CODE-1)

    def count_successes_for_current_context(self):
        return self._count_logs(self.current_context, exact_match=True, level_code_min=self.SUCCESS_START_CODE, level_code_max=self.NOTICE_START_CODE-1)

    def count_successes_for_current_and_nested_contexts(self):
        return self._count_logs(self.current_context, level_code_min=self.SUCCESS_START_CODE, level_code_max=self.NOTICE_START_CODE-1)

    def count_infos_for_current_context(self):
        return self._count_logs(self.current_context, exact_match=True, level_code_min=self.INFO_START_CODE, level_code_max=self.SUCCESS_START_CODE-1)

    def count_infos_for_current_and_nested_contexts(self):
        return self._count_logs(self.current_context, level_code_min=self.INFO_START_CODE, level_code_max=self.SUCCESS_START_CODE-1)

    def export_logs_to_gcs_file(self, bucket_name, storage_client, file_prefix=None, file_name=None, top_level_context=None, save_locally=False, overwrite_if_exists=False, increment_if_exists=True, local_path=None, logger=None, max_retries=2):
        def log_message(message):
            if logger:
                logger.info(message)

        def log_error(message, exc_info=False):
            if logger:
                logger.error(message, exc_info=exc_info)

        if not file_prefix:
            file_prefix = self._target_logs
        if not file_name:
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            if top_level_context:
                file_name = f"{file_prefix}_{timestamp}_{top_level_context}_len{len(self._logs)}.json"
            else:
                file_name = f"{file_prefix}_{timestamp}_len{len(self._logs)}.json"

        result = None
        try:
            result = write_json_to_gcs(
                bucket_name=bucket_name,
                storage_client=storage_client,
                data=self._logs,
                file_name=file_name,
                save_locally=save_locally,
                local_path=local_path,
                logger=logger,
                max_retries=max_retries,
                overwrite_if_exists=overwrite_if_exists,
                increment_if_exists=increment_if_exists

            )
            log_message(f"{file_prefix} successfully saved (overwritten={result.get('gcs_file_overwritten')}, incremented={result.get('gcs_file_saved_with_increment')}) to GCS at {result.get('gcs_path')} and locally at {result.get('local_path')}.")
        except Exception as e:
            log_error(f"Failed at export_logs_to_gcs_file for {file_prefix} for file {file_name} to bucket {bucket_name}: {type(e).__name__} - {str(e)}")

        return result

    def import_logs_from_json(self, json_or_file, logger=None):
        def log_message(message):
            if logger:
                logger.info(message)

        def log_warning(message, exc_info=False):
            if logger:
                logger.warning(message, exc_info=exc_info)

        try:
            if isinstance(json_or_file, str):  # Load from string
                imported_logs = json.loads(json_or_file)
            elif hasattr(json_or_file, 'read'):  # Load from file-like object
                imported_logs = json.load(json_or_file)
            self.add_logs(imported_logs)
            log_message("Successfully imported logs from json.")
        except Exception as e:
            log_warning(f"Failed to import logs from json: {type(e).__name__} - {str(e)}", exc_info=True)

    def _update_counts(self, log, remove=False):
        level_code = log["level_code"]
        level_name = log["level_name"]

        if remove:
            if level_code >= self.ERROR_START_CODE:
                self._errors_count -= 1
            elif self.WARNING_START_CODE <= level_code < self.ERROR_START_CODE:
                self._warnings_count -= 1
            elif self.NOTICE_START_CODE <= level_code < self.WARNING_START_CODE:
                self._notices_count -= 1
            elif self.SUCCESS_START_CODE <= level_code < self.NOTICE_START_CODE:
                self._successes_count -= 1
            elif self.INFO_START_CODE <= level_code < self.SUCCESS_START_CODE:
                self._infos_count -= 1
            self._level_counts[level_name] -= 1
        else:
            if level_code >= self.ERROR_START_CODE:
                self._errors_count += 1
            elif self.WARNING_START_CODE <= level_code < self.ERROR_START_CODE:
                self._warnings_count += 1
            elif self.NOTICE_START_CODE <= level_code < self.WARNING_START_CODE:
                self._notices_count += 1
            elif self.SUCCESS_START_CODE <= level_code < self.NOTICE_START_CODE:
                self._successes_count += 1
            elif self.INFO_START_CODE <= level_code < self.SUCCESS_START_CODE:
                self._infos_count += 1
            self._level_counts[level_name] += 1
