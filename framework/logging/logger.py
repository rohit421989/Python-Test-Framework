import logging
from pathlib import Path


class Logger:

    @staticmethod
    def get_logger(name):

        log_directory = Path("reports/logs")
        log_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        logger = logging.getLogger(name)

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            file_handler = logging.FileHandler(
                log_directory / "test_execution.log"
            )
            file_handler.setFormatter(formatter)

            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger