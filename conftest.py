import pytest
from api.user_api import UserAPI


@pytest.fixture
def api():
    return UserAPI()