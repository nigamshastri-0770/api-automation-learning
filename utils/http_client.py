import requests

from requests.adapters import (
    HTTPAdapter
)

from urllib3.util.retry import (
    Retry
)


def get_session():

    session = (
        requests.Session()
    )

    retry = (
        Retry(

            total=3,

            backoff_factor=1
        )
    )

    adapter = (
        HTTPAdapter(

            max_retries=retry
        )
    )

    session.mount(
        "https://",
        adapter
    )

    session.headers.update({

        "Content-Type":
        "application/json"

    })

    return session