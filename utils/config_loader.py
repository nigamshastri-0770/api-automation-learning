import os
import yaml


def load_config():

    env = (
        os.getenv(
            "ENV",
            "dev"
        )
    )

    file_path = (
        f"config/{env}.yaml"
    )

    if not os.path.exists(
        file_path
    ):

        raise FileNotFoundError(

            f"Config not found: {file_path}"

        )

    with open(

        file_path,

        "r"

    ) as file:

        config = (

            yaml.safe_load(
                file
            )

        )

    config[
        "env"
    ] = env

    return config


CONFIG = (
    load_config()
)