from beanie import Document
from beanie.odm.fields import PydanticObjectId
from pydantic import BaseModel, EmailStr
from pydantic.fields import Field


class UserIn(BaseModel):
    display_name: str
    email_address: EmailStr
    created_by_service: str


class User(UserIn, Document):
    created_by_service: str = Field(default="None")
    class Collection:
        name = "users"