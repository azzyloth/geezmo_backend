from pydantic import BaseModel

# Shared properties
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int

# When creating a product (input)
class ProductCreate(ProductBase):
    pass

# When updating a product (partial update allowed)
class ProductUpdate(ProductBase):
    pass

# When returning a product (output)
class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True
