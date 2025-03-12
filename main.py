from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from items_views import router as items_router
import uvicorn
from users.vies import router as users_router
app = FastAPI()
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




if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)