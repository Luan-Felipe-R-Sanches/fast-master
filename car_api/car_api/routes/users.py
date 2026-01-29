from fastapi import APIRouter, status

from car_api.db import USERS
from car_api.schemas.users import (
    UserScreen,
    UserListPublicSchema,
    UserPublicSchema,

)       

router = APIRouter()

@router.post(path="/",
             status_code=status.HTTP_201_CREATED,
             response_model=UserPublicSchema,)
async def create_user(user:UserScreen):
    user_with_id = UserPublicSchema(**user.model_dump(), id=len(USERS)+1)
    USERS.append(user_with_id)
    return user_with_id


@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=UserListPublicSchema,)
async def list_users():
    return {"users": USERS}

@router.put("/{user_id}",status_code=status.HTTP_200_OK, response_model=UserPublicSchema,)

async def update_user(user_id: int, user: UserScreen):
    user_with_id = UserPublicSchema(**user.model_dump(), id=user_id)
    USERS[user_id - 1] = user_with_id
    return user_with_id
