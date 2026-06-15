import pytest
import allure


from utils.test_data import (
    CREATE_USERS
)

from schemas.user_schema import (
    USER_SCHEMA
)

from models.user_model import (
    UserResponse
)

from validators.response_validator import (

    validate_status,

    validate_keys

)

from validators.schema_validator import (

    validate_schema

)

from validators.contract_validator import (

    validate_contract

)


@pytest.mark.api

@allure.epic(
    "User Management"
)

@allure.feature(
    "CRUD User Flow"
)

@pytest.mark.parametrize(

    "name,job",

    CREATE_USERS

)

def test_user_flow(

    api,

    name,

    job

):


    # ==========================
    # CREATE USER
    # ==========================

    with allure.step(
        "Create User"
    ):

        create = (

            api.create_user({

                "name": name,

                "job": job

            })

        )


        validate_status(

            create,

            201

        )


        response = (

            create.json()

        )


        user_id = (

            response["id"]

        )


        allure.attach(

            create.text,

            name="Create Response",

            attachment_type=(

                allure.attachment_type.JSON

            )

        )


        print(

            f"\nCreated User "

            f"{user_id}"

        )


    # ==========================
    # RESPONSE VALIDATION
    # ==========================

    with allure.step(
        "Validate Response"
    ):


        validate_keys(

            create,

            [

                "name",

                "job",

                "id",

                "createdAt"

            ]

        )


        assert (

            response["name"]

            ==

            name

        )


        assert (

            response["job"]

            ==

            job

        )


        print(
            "Response Validation Passed"
        )


    # ==========================
    # SCHEMA VALIDATION
    # ==========================

    with allure.step(
        "Schema Validation"
    ):

        validate_schema(

            create,

            USER_SCHEMA

        )


        print(
            "Schema Passed"
        )


    # ==========================
    # CONTRACT VALIDATION
    # ==========================

    with allure.step(
        "Contract Validation"
    ):

        contract = (

            validate_contract(

                create,

                UserResponse

            )

        )


        assert (

            contract.name

            ==

            name

        )


        print(
            "Contract Passed"
        )


    # ==========================
    # VERIFY USER
    # ==========================

    with allure.step(
        "Verify User"
    ):

        verify = (

            api.verify_user(

                user_id

            )

        )


        allure.attach(

            verify.text,

            name="Verify Response",

            attachment_type=(

                allure.attachment_type.JSON

            )

        )


        print(

            f"Verify Status: "

            f"{verify.status_code}"

        )


    # ==========================
    # UPDATE USER
    # ==========================

    with allure.step(
        "Update User"
    ):

        update = (

            api.update_user(

                user_id,

                {

                    "name": name,

                    "job": "SDET"

                }

            )

        )


        validate_status(

            update,

            200

        )


        update_response = (

            update.json()

        )


        validate_keys(

            update,

            [

                "name",

                "job",

                "updatedAt"

            ]

        )


        assert (

            update_response["job"]

            ==

            "SDET"

        )


        allure.attach(

            update.text,

            name="Update Response",

            attachment_type=(

                allure.attachment_type.JSON

            )

        )


        print(
            "Update Passed"
        )


    # ==========================
    # DELETE USER
    # ==========================

    with allure.step(
        "Delete User"
    ):

        delete = (

            api.delete_user(

                user_id

            )

        )


        validate_status(

            delete,

            204

        )


        print(

            f"Deleted "

            f"{user_id}"

        )