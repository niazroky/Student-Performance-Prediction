import logging
import os
from datetime import datetime

# Construct a filename for the log file using the current date and time in the format 'mm_dd_YYYY_HH_MM_SS.log'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Construct the path to the 'logs' directory relative to the current working directory, and append the filename to it
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the 'logs' directory if it doesn't already exist, and ensure no exceptions are raised if it already exists
os.makedirs(logs_path, exist_ok=True)

# Construct the full path to the log file by joining the 'logs' directory path with the filename
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system with the following parameters:
# - filename: Specifies the filename for the log file
# - format: Specifies the format for log messages, including placeholders for timestamp, line number, logger name, log level, and message content
# - level: Sets the minimum logging level to INFO, which means that only messages with a level of INFO or higher will be logged
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

