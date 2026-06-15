import pytest
import allure


@pytest.mark.api

@allure.feature(
    "User Chaining"
)

def test_user_order_flow(
    api
):

    with allure.step(
        "Create User"
    ):

        user = (

            api.create_user({

                "name":
                "Nigam",

                "job":
                "QA"

            })

        )

        assert (

            user.status_code

            ==

            201

        )

        user_id = (

            user
            .json()[
                "id"
            ]

        )


    with allure.step(
        "Verify User"
    ):

        response = (

            api.get_user(
                2
            )

        )

        assert (

            response.status_code

            ==

            200

        )

        assert (
            user_id
        )