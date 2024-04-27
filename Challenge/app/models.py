from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()
metadata = Base.metadata

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    department = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class ProductModel(BaseModel):
    name: str
    department: str
    price: float