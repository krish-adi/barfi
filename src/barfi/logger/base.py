import logging
import os
from datetime import datetime


class BarfiLogger:
    def __init__(
        self,
        log_level=logging.INFO,
        console_output=True,
        file_output=True,
        log_file_dir="./logs",
    ):
        """
        Initialize the Barfi logger.

        :param log_level: Logging level (default: logging.INFO)
        :param console_output: Whether to output logs to the console (default: True)
        :param file_output: Whether to output logs to a file (default: True)
        :param log_file_dir: Directory to store log files (default: "logs")
        """
        self.logger = logging.getLogger("barfi")
        self.logger.setLevel(log_level)

        # Set log format
        # log_format = logging.Formatter("%(levelname)-8s :: %(asctime)s - %(message)s")
        log_format = logging.Formatter(
            "%(levelname)-8s :: %(asctime)s.%(msecs)03d - %(message)s",
            datefmt="%H:%M:%S",
        )

        # Console handler
        if console_output:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(log_format)
            self.logger.addHandler(console_handler)

        # File handler
        if file_output:
            # Ensure log directory exists
            cwd = os.getcwd()
            log_dir_path = os.path.join(cwd, log_file_dir)
            if not os.path.exists(log_dir_path):
                os.makedirs(log_dir_path)

            # Create log file name based on date
            log_file = os.path.join(
                log_dir_path, f"{datetime.now().strftime('%Y-%m-%d')}.log"
            )
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(log_format)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        """Returns the configured logger."""
        return self.logger

    def log(self, message, level=logging.INFO):
        """Log a message with the specified level."""
        self.logger.log(level, message)


# Example usage
if __name__ == "__main__":
    barf_logger = BarfiLogger(log_level=logging.DEBUG)
    logger = barf_logger.get_logger()
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
    barf_logger.log("This is a log message.", logging.INFO)
