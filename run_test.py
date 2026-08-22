import subprocess
import sys
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
        "--html=reports/html/report.html",
        "--self-contained-html"
    ]

    result = subprocess.run(
        command
    )

    sys.exit(
        result.returncode
    )

if __name__ == "__main__":
    main()