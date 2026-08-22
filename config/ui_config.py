import os


class UIConfig:

    BROWSER = os.getenv(
        "BROWSER",
        "chrome"
    ).lower()

    HEADLESS = os.getenv(
        "HEADLESS",
        "false"
    ).lower() == "true"

    TIMEOUT = int(
        os.getenv(
            "UI_TIMEOUT",
            "10"
        )
    )

    LOGIN_URL = os.getenv(
    "LOGIN_URL",
    "https://the-internet.herokuapp.com/login"
)