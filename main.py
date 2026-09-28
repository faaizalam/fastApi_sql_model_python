from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



class Item(BaseModel):
    name:str
    price:int
    tax:Optional[float]=None
    
    
    
app= FastAPI()   
    
@app.get("/message")
async def read_root():
    return {"message":"kiya hal heee"}    



@app.get("/items/{item_name}")
async def get_item(item_name:str,company:str |None=None):
    return {"item_name":item_name,"company":company}    







@app.get("/items/")
async def all_items(skip:int =0, limit:int=10):
    dummy_data=[
        {"name":"lap1","price":100},
        {"name":"lap2","price":200,"tax":10.10},
    ]
    
    return Item(**dummy_data)