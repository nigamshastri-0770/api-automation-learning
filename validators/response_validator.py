def validate_status(
    response,
    expected
):

    assert (
        response.status_code
        ==
        expected
    ), (
        f"Expected {expected}, "
        f"got {response.status_code}"
    )


def validate_keys(
    response,
    keys
):

    body = (
        response.json()
    )

    for key in keys:

        assert (
            key
            in
            body
        )

    print(
        "\nResponse Validation Passed"
    )