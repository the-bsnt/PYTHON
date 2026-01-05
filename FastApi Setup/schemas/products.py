from pydantic import BaseModel


class ProductCreate(BaseModel):

    name: str
    hs_code: str
    price: str
