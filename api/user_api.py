import requests

from utils.helpers import (
    BASE_URL,
    get_headers
)


class UserAPI:


    def login(self, payload):

        return requests.post(
            f"{BASE_URL}/api/login",
            headers=get_headers(),
            json=payload
        )


    def get_user(self, user_id):

        return requests.get(
            f"{BASE_URL}/api/users/{user_id}",
            headers=get_headers()
        )


    def create_user(self, payload):

        return requests.post(
            f"{BASE_URL}/api/users",
            headers=get_headers(),
            json=payload
        )


    def update_user(
        self,
        user_id,
        payload
    ):

        return requests.put(
            f"{BASE_URL}/api/users/{user_id}",
            headers=get_headers(),
            json=payload
        )


    def delete_user(
        self,
        user_id
    ):

        return requests.delete(
            f"{BASE_URL}/api/users/{user_id}",
            headers=get_headers()
        )


    def verify_user(
        self,
        user_id
    ):

        return requests.get(
            f"{BASE_URL}/api/users/{user_id}",
            headers=get_headers()
        )