import pytest

from api.user_api import (
    UserAPI
)

from utils.test_data import (
    LOGIN_DATA
)

from db.db_helper import (
    DB
)


# Create API object once
@pytest.fixture(
    scope="session"
)
def session_api():

    return (
        UserAPI()
    )


# Login once and store token
@pytest.fixture(
    scope="session"
)
def auth_token(

    session_api

):

    login = (

        session_api.login(
            LOGIN_DATA
        )

    )

    assert (
        login.status_code
        ==
        200
    )

    token = (

        login
        .json()
        .get(
            "token"
        )

    )

    assert (
        token
        is not None
    )

    return token


# Provide ready API to tests
@pytest.fixture(
    scope="function"
)
def api(

    session_api,

    auth_token

):

    session_api.set_token(
        auth_token
    )

    return (
        session_api
    )


# Database fixture
@pytest.fixture(
    scope="function"
)
def db():

    database = (
        DB()
    )

    yield database

    database.close()