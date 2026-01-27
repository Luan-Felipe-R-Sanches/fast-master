from fastapi import FastAPI, status

from car_api.routes import users

app = FastAPI()

app.include_router(
    router=users.router,
    prefix="/api/v1/users",
    tags=["users"]
)

@app.get("/health_check", status_code=status.HTTP_200_OK)
def read_root():
    return {"status": "ok"}