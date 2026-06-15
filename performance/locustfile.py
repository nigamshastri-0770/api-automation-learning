from locust import (
    HttpUser,
    task,
    between
)


class UserLoadTest(
    HttpUser
):

    wait_time = between(
        1,
        3
    )


    headers = {

        "x-api-key":
        "free_user_3EqwNfJjHbaSI4VWRBchJllgjn9",
    }


    @task
    def get_user(self):

        response = self.client.get(

            "/api/users/2",

            headers=self.headers

        )


        assert (
            response.status_code
            ==
            200
        )


    @task
    def create_user(self):

        payload = {

            "name":
            "Nigam",

            "job":
            "QA"
        }


        response = self.client.post(

            "/api/users",

            json=payload,

            headers=self.headers

        )


        assert (
            response.status_code
            ==
            201
        )