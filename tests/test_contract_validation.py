import pytest

from schemas.user_schema import (
    USER_SCHEMA
)

from validators.schema_validator import (
    validate_schema
)


@pytest.mark.contract
def test_create_user_contract(

    api

):

    print(
        "\nCreating User"
    )


    response = (

        api.create_user({

            "name":
            "Nigam",

            "job":
            "QA"

        })

    )


    assert (

        response.status_code

        ==

        201

    )


    validate_schema(

        response,

        USER_SCHEMA

    )


    print(
        "\nContract Validation Passed"
    )