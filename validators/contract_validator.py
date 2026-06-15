def validate_contract(

    response,

    model

):

    body = (

        response.json()

    )

    validated = (

        model(

            **body

        )

    )

    print(
        "\nContract Passed"
    )

    return validated