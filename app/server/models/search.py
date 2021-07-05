from beanie import Document
from beanie import PydanticObjectId
from pydantic import BaseModel
from enum import Enum
from typing import Any, List

class SearchOperationsEnum(str, Enum):
    equal = 'equal'
    less_than = 'less_than'
    bigger_than = 'bigger_than'



class SearchTerm(BaseModel):
    operation: SearchOperationsEnum
    field_name: str
    value: Any


class SavedSearchIn(BaseModel):
    terms: List[SearchTerm]


class SavedSearch(SavedSearchIn, Document):
    user_id: PydanticObjectId
    class Collection:
        name = "saved-searches"
