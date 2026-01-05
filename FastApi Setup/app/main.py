from fastapi import FastAPI, Depends

app = FastAPI(title="bsnt fastapi app", version="1.0.0")


@app.get("/")
def root():
    return {"detail": "fastapi sucessfully set up"}


from schemas.products import ProductCreate
from app.core.database import get_db
from sqlalchemy.orm import Session
from models.products import Products


@app.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product = Product
