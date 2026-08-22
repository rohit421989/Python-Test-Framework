from pathlib import Path
from datetime import datetime


class ScreenshotUtil:

    @staticmethod
    def capture(driver, test_name):

        directory = Path(
            "reports/screenshots"
        )

        directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_path = (
            directory
            / f"{test_name}_{timestamp}.png"
        )

        driver.save_screenshot(
            str(file_path)
        )

        return file_path