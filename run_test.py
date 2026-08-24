import subprocess
import sys
from config.execution_config import ExecutionConfig
from pathlib import Path
from framework.utilities.report_manager import (
    ReportManager
)


def main():

    ReportManager.clean_reports()

    report_directory = Path("reports/html")

    report_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    command = [
        sys.executable,
        "-m",
        "pytest",
        "-v",
        "-n",
        ExecutionConfig.WORKERS,
        "--html=reports/html/report.html",
        "--self-contained-html",
        "--alluredir=reports/allure-results"
    ]

    result = subprocess.run(
        command
    )

    sys.exit(
        result.returncode
    )

if __name__ == "__main__":
    main()