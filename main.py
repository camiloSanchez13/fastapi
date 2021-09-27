from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

import models
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from pydantic import BaseModel
from models import User


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


class TestRequest(BaseModel):
    symbol: str


async def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post('/test')
async def crete_test(testRequest : TestRequest, db: AsyncSession = Depends(get_db)):

    user = User()
    user.email = testRequest.symbol
    db.add(user)
    db.commit()

    return {
        "code" : "success",
        "messge" : "test create"
    }

@app.get('/')
async def index():
    return 'Hello World'











# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Optional[bool] = None
#
# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}