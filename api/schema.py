from sqlmodel import SQLModel
from typing import List,Optional


class CategoryBase(SQLModel):
    pass
class CategoryCreate(CategoryBase):
    pass
class CategoryPublic(CategoryBase):
    pass
class UserBase(CategoryBase):
    pass

class ReviewBase(SQLModel):
    pass
class ReviewPublic(ReviewBase):
    pass




class ProductBase(SQLModel):
    name:str
    description:str
    price:float
    
    
    

class ProductCreate(ProductBase):
    category_id:int
    category:CategoryPublic
    review:List[ReviewPublic]=[]
    

class ProductPublic(ProductBase):
    id:int
    category:CategoryPublic  

    
    
    


        