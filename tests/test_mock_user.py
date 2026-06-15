from unittest.mock import (
    Mock
)


def test_mock_create_user(

    api,

    mocker

):


    fake_response = Mock()


    fake_response.status_code = (
        201
    )


    fake_response.json.return_value = {

        "id": "999",

        "name": "Nigam",

        "job": "SDET"

    }



    mocker.patch.object(

        api,

        "create_user",

        return_value=fake_response

    )



    response = (

        api.create_user({

            "name": "Nigam",

            "job": "QA"

        })

    )



    assert (

        response.status_code

        ==

        201

    )



    assert (

        response.json()["id"]

        ==

        "999"

    )



    print(
        "\nMock API Passed"
    )