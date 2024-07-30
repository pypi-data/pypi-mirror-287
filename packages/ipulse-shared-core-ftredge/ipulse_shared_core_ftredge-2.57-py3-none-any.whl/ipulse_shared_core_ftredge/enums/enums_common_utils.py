
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

from enum import Enum


class SystemsImpacted(Enum):
    NO = "__no"
    YES = "__yes"
    INVESTIGATE = "__investigate"
    MULTIPLE = "__multiple"
    DB = "db"
    BQ_TABLE= "bq_table"
    BQ_TABLES = "bq_tables"
    GCS_BUCKET = "gcs_bucket"
    GCS_BUCKETS = "gcs_buckets"
    GCS_BUCKET_FILE = "gcs_bucket_file"
    GCS_BUCKET_FILES = "gcs_bucket_files"
    API = "api"
    APIS = "apis"
    LOCAL_FILE = "local_file"
    LOCAL_FILES = "local_files"

class TargetLogs(Enum):
    MIXED="mixed_logs"
    SUCCESSES = "success_logs"
    NOTICES = "notice_logs"
    SUCCESSES_AND_NOTICES = "succs_n_notc_logs"
    WARNINGS = "warning_logs"
    WARNINGS_AND_ERRORS = "warn_n_err_logs"
    ERRORS = "error_logs"

class LogLevel(Enum):
    """
    Standardized notice levels for data engineering pipelines,
    designed for easy analysis and identification of manual 
    intervention needs.
    """
    DEBUG = 10  # Detailed debug information (for development/troubleshooting)

    INFO = 100
    INFO_REMOTE_PERSISTNACE_COMPLETE= 101
    INFO_REMOTE_UPDATE_COMPLETE = 102
    INFO_REMOTE_DELETE_COMPLETE = 103

    INFO_REMOTE_BULK_PERSISTNACE_COMPLETE= 111
    INFO_REMOTE_BULK_UPDATE_COMPLETE = 112
    INFO_REMOTE_BULK_DELETE_COMPLETE = 113

    INFO_LOCAL_PERSISTNACE_COMPLETE = 121

    SUCCESS = 201
    SUCCESS_WITH_NOTICES = 211
    SUCCESS_WITH_WARNINGS = 212

    NOTICE = 300  # Maybe same file or data already fully or partially exists
    NOTICE_ALREADY_EXISTS = 301 # Data already exists, no action required
    NOTICE_PARTIAL_EXISTS = 302 # Partial data exists, no action required
    NOTICE_ACTION_CANCELLED = 303 # Data processing cancelled, no action required

     # Warnings indicate potential issues that might require attention:
    WARNING = 400 # General warning, no immediate action required
    # WARNING_NO_ACTION = 401 # Minor issue or Unexpected Behavior, no immediate action required (can be logged frequently)
    WARNING_REVIEW_RECOMMENDED = 402 # Action recommended to prevent potential future issues
    WARNING_FIX_RECOMMENDED = 403 # Action recommended to prevent potential future issues
    WARNING_FIX_REQUIRED = 404  # Action required, pipeline can likely continue

    ERROR = 500 # General error, no immediate action required

    ERROR_EXCEPTION = 501
    ERROR_CUSTOM = 502 # Temporary error, automatic retry likely to succeed
    ERROR_OPERATION_PARTIALLY_FAILED = 511 # Partial or full failure, manual intervention required
    ERROR_OPERATION_FAILED = 512 # Operation failed, manual intervention required
    ERORR_OPERATION_WITH_WARNINGS = 513 # Partial or full failure, manual intervention required
    ERORR_OPERATION_WITH_ERRORS = 514 # Partial or full failure, manual intervention required
    ERORR_OPERATION_WITH_WARNINGS_OR_ERRORS = 515 # Partial or full failure, manual intervention required

    ERROR_THRESHOLD_REACHED = 551
    ERROR_PIPELINE_THRESHOLD_REACHED = 552 # Error due to threshold reached, no immediate action required
    ERROR_SUBTHRESHOLD_REACHED = 553 # Error due to threshold reached, no immediate action required
    ERROR_DATA_QUALITY_THRESHOLD_REACHED = 554 # Error due to threshold reached, no immediate action required
    # Critical errors indicate severe failures requiring immediate attention:
    CRITICAL=600 # General critical error, requires immediate action
    CRITICAL_SYSTEM_FAILURE = 601 # System-level failure (e.g., infrastructure, stackoverflow ), requires immediate action

    UNKNOWN=1001 # Unknown error, should not be used in normal operation


class LogStatus(Enum):
    OPEN = "open"
    ACKNOWLEDGED = "acknowledged"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    IGNORED = "ignored"
    CANCELLED = "cancelled"

### Exception during full exection, partially saved
# Exception during ensemble pipeline; modifications collected in local object , nothing persisted
# Exception during ensemble pipeline; modifications persisted , metadata failed
# Exception during ensemble pipeline; modifications persisted , metadata persisted
# Exception during ensemble pipeline; modifications persisted , metadata persisted


class Unit(Enum):
    MIX="MIX"
    # Currency and Financial Values
    USD = "USD"  # United States Dollar
    EUR = "EUR"  # Euro
    JPY = "JPY"  # Japanese Yen
    GBP = "GBP"  # British Pound Sterling
    AUD = "AUD"  # Australian Dollar
    CAD = "CAD"  # Canadian Dollar
    CHF = "CHF"  # Swiss Franc
    CNY = "CNY"  # Chinese Yuan Renminbi
    SEK = "SEK"  # Swedish Krona
    NZD = "NZD"  # New Zealand Dollar
    MXN = "MXN"  # Mexican Peso
    SGD = "SGD"  # Singapore Dollar
    HKD = "HKD"  # Hong Kong Dollar
    NOK = "NOK"  # Norwegian Krone
    KRW = "KRW"  # South Korean Won
    RUB = "RUB"  # Russian Ruble
    INR = "INR"  # Indian Rupee
    BRL = "BRL"  # Brazilian Real
    ZAR = "ZAR"  # South African Rand
    CURRENCY = "currency"    # General currency, when specific currency is not needed

    # Stock Market and Investments
    SHARES = "shares"        # Number of shares
    PERCENT = "prcnt"      # Percentage, used for rates and ratios
    BPS = "bps"              # Basis points, often used for interest rates and financial ratios

    # Volume and Quantitative Measurements
    VOLUME = "volume"        # Trading volume in units
    MILLIONS = "mills"    # Millions, used for large quantities or sums
    BILLIONS = "bills"    # Billions, used for very large quantities or sums

    # Commodity Specific Units
    BARRELS = "barrels"      # Barrels, specifically for oil and similar liquids
    TONNES = "tonnes"        # Tonnes, for bulk materials like metals or grains
    TROY_OUNCES = "troy_oz" # Troy ounces, specifically for precious metals

    # Real Estate and Physical Properties
    SQUARE_FEET = "sq_ft"    # Square feet, for area measurement in real estate
    METER_SQUARE = "m2"      # Square meters, for area measurement in real estate
    ACRES = "acres"          # Acres, used for measuring large plots of land

    # Miscellaneous and Other Measures
    UNITS = "units"          # Generic units, applicable when other specific units are not suitable
    COUNT = "count"          # Count, used for tallying items or events
    INDEX_POINTS = "index_pnts"  # Index points, used in measuring indices like stock market indices
    RATIO = "ratio"          # Ratio, for various financial ratios

class Frequency(Enum):
    ONE_MIN = "1min"
    FIVE_MIN="5min"
    FIFTEEN_MIN="15min"
    THIRTY_MIN = "30min"
    ONE_H = "1h"
    TWO_H = "2h"
    SIX_H = "6h"
    TWELVE_H = "12h"
    FOUR_H = "4h"
    EOD="eod"
    ONE_D = "1d"
    TWO_D = "2d"
    THREE_D = "3d"
    ONE_W = "1w"
    ONE_M = "1m"
    TWO_M="2m"
    THREE_M="3m"
    SIX_M="6m"
    ONE_Y="1y"
    THREE_Y="3y"
