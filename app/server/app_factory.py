import motor
from beanie import init_beanie
from fastapi import FastAPI
from pydantic import BaseSettings

# from models import Note
# from routes import notes_router
from server.routes.users import users_router
from server.models.user import User
app = FastAPI()


class Settings(BaseSettings):
    mongo_host: str = "localhost"
    mongo_user: str = "beanie"
    mongo_pass: str = "beanie"
    mongo_db: str = "beanie_db"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @property
    def mongo_dsn(self):
        return f"mongodb+srv://{self.mongo_user}:{self.mongo_pass}@{self.mongo_host}/{self.mongo_db}"


@app.on_event("startup")
async def app_init():
    # CREATE MOTOR CLIENT
    client = motor.motor_asyncio.AsyncIOMotorClient(
        Settings().mongo_dsn
    )

    # INIT BEANIE
    await init_beanie(client.beanie_db, document_models=[User])


    app.include_router(users_router, prefix="/v1", tags=["users"])
