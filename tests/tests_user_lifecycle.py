def test_complete_user_flow():

    api = UserAPI()

    create = api.create_user({
        "name": "Nigam",
        "job": "QA"
    })

    assert create.status_code == 201

    user_id = create.json()["id"]

    verify = api.verify_user(user_id)

    update = api.update_user(
        user_id,
        {
            "job": "SDET"
        }
    )

    assert update.status_code == 200

    delete = api.delete_user(
        user_id
    )

    assert delete.status_code == 204