from pathlib import Path
import shutil


class ReportManager:

    REPORT_DIRECTORY = Path("reports")

    @classmethod
    def clean_reports(cls):

        if cls.REPORT_DIRECTORY.exists():

            shutil.rmtree(
                cls.REPORT_DIRECTORY
            )

        cls.REPORT_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True
        )