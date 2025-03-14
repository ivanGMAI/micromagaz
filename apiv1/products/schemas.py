from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    price: int
class Product(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
class ProductCreate(ProductBase):
    pass
class ProductUpdate(ProductCreate):
    pass
class ProductUpdatePartial(ProductCreate):
    name : str| None = None
    price : int | None = None
