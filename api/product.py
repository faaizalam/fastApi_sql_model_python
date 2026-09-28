from typing import List
from fastapi import APIRouter,Depends,HTTPException,status
from sqlmodel.ext.asyncio.session import AsyncSession
from core.db import get_session
from crud import curd_product
from schema import ProductCreate,ProductPublic



router=APIRouter()

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=ProductPublic)
async def create_new_product(product_date:ProductCreate,session:AsyncSession=Depends(get_session)):
    new_product=await curd_product.create_product(product_data=product_date,session=session)
    return new_product
    
    
    


@router.get("/",status_code=200,response_model=List[ProductPublic])
async def get_all_product_list(session:AsyncSession=Depends(get_session)):
    all_products=await curd_product.get_all_products(session=session)    
    return all_products




@router.get("/{product_id}",response_model=ProductPublic)
async def product(id:int,session:AsyncSession=Depends(get_session)):
    product=await curd_product.get_product_by_id(id,session=session)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return product