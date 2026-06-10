import pytest

from utils.test_data import (
    LOGIN_DATA,
    CREATE_USERS
)


@pytest.mark.parametrize(
    "name,job",
    CREATE_USERS
)

def test_create_users(
    api,
    name,
    job
):


    login = api.login(
        LOGIN_DATA
    )

    assert login.status_code == 200



    create = api.create_user({

        "name": name,

        "job": job
    })


    assert create.status_code == 201


    response = create.json()


    print(
        f"\nCreated {name}"
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