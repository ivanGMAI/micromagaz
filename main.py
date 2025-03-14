from contextlib import asynccontextmanager
from fastapi import FastAPI
from apiv1 import router as router_v1
from pydantic import BaseModel, EmailStr

from apiv1.products.vies import router
from items_views import router as items_router
import uvicorn
from core.config import settings
from users.vies import router as users_router
from core.models import Base,db_helper
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1,prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)




class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)