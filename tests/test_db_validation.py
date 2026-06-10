from api.user_api import UserAPI

from db.db_helper import DB


api = UserAPI()

db = DB()


def test_validate_api_and_db():

    print("\nCreating User")


    create = api.create_user({

        "name": "Nigam",

        "job": "QA"
    })


    assert create.status_code == 201


    response = create.json()


    user_id = int(
        response["id"]
    )



    print(
        response
    )



    db.insert_user(

        user_id,

        response["name"],

        response["job"]

    )



    db_data = db.get_user(
        user_id
    )



    print(
        db_data
    )



    assert db_data[0] == user_id

    assert db_data[1] == response["name"]

    assert db_data[2] == response["job"]


    print(
        "\nDB Validation Passed"
    )