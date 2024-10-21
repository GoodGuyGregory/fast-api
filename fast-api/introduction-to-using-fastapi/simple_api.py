from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    # properties
    name: str
    price: float
    is_offer: Union[bool, None] = None


# first endpoint 
@app.get("/")
def read_root():
    return {"message":"Greetings Earthlings."}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str,None] = None):
        return {"item_id": item_id, "q": q}


"""
    pretend to update a db item
"""
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
