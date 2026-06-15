import requests


class BaseAPI:

    def __init__(self):

        self.session = (
            requests.Session()
        )


    def get(

        self,

        url,

        headers=None

    ):

        return (

            self.session.get(

                url,

                headers=headers

            )

        )


    def post(

        self,

        url,

        payload=None,

        headers=None

    ):

        return (

            self.session.post(

                url,

                json=payload,

                headers=headers

            )

        )


    def put(

        self,

        url,

        payload=None,

        headers=None

    ):

        return (

            self.session.put(

                url,

                json=payload,

                headers=headers

            )

        )


    def delete(

        self,

        url,

        headers=None

    ):

        return (

            self.session.delete(

                url,

                headers=headers

            )

        )