import logging
import os
from pathlib import Path


class Logger:

    @staticmethod
    def get_logger(name):

        log_directory = Path("reports/logs")
        log_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        worker_id = os.getenv(
            "PYTEST_XDIST_WORKER",
            "master"
        )

        log_file = (
            log_directory /
            f"test_execution_{worker_id}.log"
        )

        logger = logging.getLogger(name)

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | "
                "%(name)s | %(message)s"
            )

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            file_handler = logging.FileHandler(
                log_file
            )
            file_handler.setFormatter(formatter)

            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger