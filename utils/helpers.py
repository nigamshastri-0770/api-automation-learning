from utils.config_loader import (
    CONFIG
)


BASE_URL = (
    CONFIG.get(
        "base_url"
    )
)


def get_headers():

    headers = (

        CONFIG.get(
            "headers",
            {}
        )

    )

    if not headers:

        print(
            "\nWARNING: No headers found in config"
        )

    else:

        print(
            "\nLoaded Headers:",
            headers
        )

    return (
        headers.copy()
    )