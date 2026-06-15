from api.base_api import (
    BaseAPI
)

from utils.helpers import (
    get_headers
)

from utils.config_loader import (
    CONFIG
)

from utils.logger import (
    logger
)


class UserAPI(
    BaseAPI
):

    def __init__(self):

        super().__init__()

        self.token = None

        self.base_url = (
            CONFIG[
                "base_url"
            ]
        )

        self.timeout = (
            CONFIG[
                "timeout"
            ]
        )

    def set_token(

        self,

        token

    ):

        self.token = token

    def auth_headers(

        self

    ):

        headers = (
            get_headers()
            .copy()
        )

        if self.token:

            headers[
                "Authorization"
            ] = (

                f"Bearer {self.token}"

            )

        return headers

    def login(

        self,

        payload

    ):

        response = (

            self.post(

                f"{self.base_url}/api/login",

                payload=payload,

                headers=get_headers()

            )

        )

        logger.info(
            f"LOGIN | "
            f"{response.status_code}"
        )

        print(
            "\nLOGIN RESPONSE:",
            response.text
        )

        return response

    def get_user(

        self,

        user_id

    ):

        response = (

            self.get(

                f"{self.base_url}/api/users/{user_id}",

                headers=self.auth_headers()

            )

        )

        logger.info(

            f"GET USER {user_id} | "

            f"{response.status_code}"

        )

        print(
            "\nGET USER:",
            response.text
        )

        return response

    def create_user(

        self,

        payload

    ):

        response = (

            self.post(

                f"{self.base_url}/api/users",

                payload=payload,

                headers=self.auth_headers()

            )

        )

        logger.info(

            f"CREATE USER | "

            f"{response.status_code}"

        )

        print(
            "\nCREATE RESPONSE:",
            response.text
        )

        return response

    def update_user(

        self,

        user_id,

        payload

    ):

        response = (

            self.put(

                f"{self.base_url}/api/users/{user_id}",

                payload=payload,

                headers=self.auth_headers()

            )

        )

        logger.info(

            f"UPDATE USER | "

            f"{response.status_code}"

        )

        print(
            "\nUPDATE RESPONSE:",
            response.text
        )

        return response

    def delete_user(

        self,

        user_id

    ):

        response = (

            self.delete(

                f"{self.base_url}/api/users/{user_id}",

                headers=self.auth_headers()

            )

        )

        logger.info(

            f"DELETE USER | "

            f"{response.status_code}"

        )

        print(
            "\nDELETE STATUS:",
            response.status_code
        )

        return response

    def verify_user(

        self,

        user_id

    ):

        response = (

            self.get_user(
                user_id
            )

        )

        logger.info(

            f"VERIFY USER {user_id} | "

            f"{response.status_code}"

        )

        return response