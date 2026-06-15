from pydantic import (
    BaseModel
)


class UserResponse(

    BaseModel

):

    name: str

    job: str

    id: str

    createdAt: str