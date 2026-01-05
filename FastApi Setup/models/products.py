from sqlalchemy import Column, Integer, String, Float

from app.core.database import Base


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hs_code = Column(String(6), index=True)
    price = Column(float, default=0.0, index=True)
