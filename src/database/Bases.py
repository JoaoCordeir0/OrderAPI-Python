from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, DECIMAL, ForeignKey

Base = declarative_base()

class Order(Base):    
    __tablename__ = 'order'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    ClientName = Column(String)
    ClientEmail = Column(Integer)
    CreationDate = Column(DateTime)
    Paid = Column(Boolean)

class Product(Base):    
    __tablename__ = 'product'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    ProductName = Column(String)
    Value = Column(DECIMAL)

class ItemOrder(Base):    
    __tablename__ = 'item_order'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    OrderId = Column(Integer, ForeignKey('order.Id'))
    ProductId = Column(Integer, ForeignKey('product.Id'))
    Amount = Column(Integer)

