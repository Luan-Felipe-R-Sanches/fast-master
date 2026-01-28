from fastapi import APIRouter, status
from car_api.schemas.users import UserListPublicSchema


router = APIRouter()

@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=UserListPublicSchema,)
async def list_users():
    return {"users": [
            {"id": 1, "username": "luan", "email": "luan@gmail.com"},
    ]}