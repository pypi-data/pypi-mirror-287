# code2prompt/utils/logging_utils.py

import sys
import logging
from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init()

class ColorfulFormatter(logging.Formatter):
    """
    A custom formatter for logging messages that colors the output based on the log level
    and prefixes each message with an emoji corresponding to its severity.

    Attributes:
        COLORS (dict): Mapping of log levels to color codes.
        EMOJIS (dict): Mapping of log levels to emojis.

    Methods:
        format(record): Formats the given LogRecord.
    """
    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.MAGENTA
    }

    EMOJIS = {
        'DEBUG': '🔍',
        'INFO': '✨',
        'WARNING': '⚠️',
        'ERROR': '💥',
        'CRITICAL': '🚨'
    }

    def format(self, record):
        """
        Formats the given LogRecord.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message.
        """
        color = self.COLORS.get(record.levelname, Fore.WHITE)
        emoji = self.EMOJIS.get(record.levelname, '')
        return f"{color}{emoji} {record.levelname}: {record.getMessage()}{Style.RESET_ALL}"

def setup_logger(name='code2prompt', level=logging.INFO):
    """
    Sets up and returns a logger with the specified name and logging level.

    Args:
        name (str): The name of the logger. Defaults to 'code2prompt'.
        level (int): The root logger level. Defaults to logging.INFO.

    Returns:
        logging.Logger: The configured logger instance.
    """
    local_logger = logging.getLogger(name)
    local_logger.setLevel(level)

    # Only add handler if there are none to prevent duplicate logging
    if not local_logger.handlers:
        # Create handlers
        c_handler = logging.StreamHandler(sys.stderr)
        c_handler.setFormatter(ColorfulFormatter())

        # Add handlers to the logger
        local_logger.addHandler(c_handler)

    return local_logger

# Create a global logger instance
logger = setup_logger()

def log_debug(message):
    """
    Logs a debug-level message.

    This function logs a message at the debug level, which is intended for detailed information,
    typically of interest only when diagnosing problems.

    Args:
        message (str): The message to log.

    Example:
        log_debug("This is a debug message")
    """
    logger.debug(message)

def log_info(message):
    """
    Logs an informational-level message.

    This function logs a message at the INFO level, which is used to provide general information
    about the program's operation without implying any particular priority.

    Args:
        message (str): The message to log.

    Example:
        log_info("Processing started")
    """
    logger.info(message)

def log_warning(message):
    """
    Logs a warning-level message.

    This function logs a message at the WARNING level, indicating that something unexpected
    happened, but did not stop the execution of the program.

    Args:
        message (str): The message to log as a warning.

    Example:
        log_warning("An error occurred while processing the file")
    """
    logger.warning(message)

def log_error(message):
    """
    Logs an error-level message.

    This function logs a message at the ERROR level, indicating that an error occurred
    that prevented the program from continuing normally.

    Args:
        message (str): The message to log as an error.

    Example:
        log_error("Failed to process file due to permission issues")
    """
    logger.error(message)

def log_critical(message):
    """
    Logs a critical-level message.

    This function logs a message at the CRITICAL level, indicating a severe error
    that prevents the program from functioning correctly.

    Args:
        message (str): The message to log as a critical error.

    Example:
        log_critical("A critical system failure occurred")
    """
    logger.critical(message)

def log_success(message):
    """
    Logs a success-level message.

    This function logs a message at the INFO level with a green color and a checkmark emoji,
    indicating that an operation was successful.

    Args:
        message (str): The message to log as a success.

    Example:
        log_success("File processed successfully")
    """
    logger.info(f"{Fore.GREEN}✅ SUCCESS: {message}{Style.RESET_ALL}")

def log_file_processed(file_path):
    """
    Logs a message indicating that a file has been processed.

    This function logs a message at the INFO level, indicating that a specific file has been processed.
    It uses a blue color and a file emoji for visual distinction.

    Args:
        file_path (str): The path to the file that was processed.

    Example:
        log_file_processed("/path/to/file.txt")
    """
    logger.info(f"{Fore.BLUE}📄 Processed: {file_path}{Style.RESET_ALL}")

def log_token_count(count):
    """
    Logs the total number of tokens processed.

    This function logs the total count of tokens processed by the application,
    using a cyan color and a token emoji for visual distinction.

    Args:
        count (int): The total number of tokens processed.

    Example:
        log_token_count(5000)
    """
    logger.info(f"{Fore.CYAN}🔢 Token count: {count}{Style.RESET_ALL}")

def log_output_created(output_path):
    """
    Logs a message indicating that an output file has been created.

    This function logs a message at the INFO level, indicating that an output file has been successfully created.
    It uses a green color and a folder emoji for visual distinction.

    Args:
        output_path (str): The path to the output file that was created.

    Example:
        log_output_created("/path/to/output/file.txt")
    """
    logger.info(f"{Fore.GREEN}📁 Output file created: {output_path}{Style.RESET_ALL}")

def log_clipboard_copy(success=True):
    """
    Logs whether the content was successfully copied to the clipboard.

    This function logs a message indicating whether the content copying to the clipboard was successful or not.
    It uses different emojis and colors depending on the success status.

    Args:
        success (bool): Indicates whether the content was successfully copied to the clipboard. Defaults to True.

    Examples:
        log_clipboard_copy(True)
            Logs: 📋 Content copied to clipboard
        log_clipboard_copy(False)
            Logs: 📋 Failed to copy content to clipboard
    """
    if success:
        logger.info(f"{Fore.GREEN}📋 Content copied to clipboard{Style.RESET_ALL}")
    else:
        logger.warning(f"{Fore.YELLOW}📋 Failed to copy content to clipboard{Style.RESET_ALL}")