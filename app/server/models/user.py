from beanie import Document
from beanie.odm.fields import PydanticObjectId
from pydantic import BaseModel, EmailStr
from pydantic.fields import Field
from bson.objectid import ObjectId


class User(Document):
    _id: PydanticObjectId = Field(default=ObjectId())
    display_name: str
    email_address: EmailStr

    class Collection:
        name = "users"