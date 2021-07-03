import beanie
from server.models.search import SavedSearch
from fastapi import APIRouter, HTTPException, Depends
from server.models.user import User
from beanie import PydanticObjectId
from typing import List



users_router = APIRouter()

async def get_user(user_id: PydanticObjectId) -> User:
    user = await User.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_saved_search(saved_search_id: PydanticObjectId) -> SavedSearch:
    saved_search = await SavedSearch.get(saved_search_id)
    if not saved_search:
        raise HTTPException(status_code=404, detail="SavedSearch maching this ID is not found")


@users_router.post('/users/', response_model=User)
async def create_user(user: User):
    await user.create()
    return user


@users_router.get("/users/{user_id}", response_model=User)
async def get_user_by_id(user: User = Depends(get_user)):
    return user


@users_router.get("/users/", response_model=List[User])
async def list_users():
    return await User.find_all().to_list()


@users_router.get("/users/{user_id}/searches/", response_model=List[SavedSearch])
async def list_searches(user_id: PydanticObjectId):
    return await SavedSearch.find_many({'user_id': user_id}).to_list()

@users_router.post("/users/{user_id}/searches/", response_model=SavedSearch)
async def create_saved_search(saved_search: SavedSearch, user: User =Depends(get_user)):
    return await SavedSearch.crete()