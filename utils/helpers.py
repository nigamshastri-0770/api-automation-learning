BASE_URL = "https://reqres.in"

API_KEY = "free_user_3EqwNfJjHbaSI4VWRBchJllgjn9"


def get_headers():
    return {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
