from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, DECIMAL, ForeignKey

Base = declarative_base()

class Order(Base):    
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    clientName = Column(String)
    clientEmail = Column(Integer)
    creationDate = Column(DateTime)
    paid = Column(Boolean)

class Product(Base):    
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    productName = Column(String)
    value = Column(DECIMAL)

class ItemOrder(Base):    
    __tablename__ = 'item_order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    orderId = Column(Integer, ForeignKey('order.Id'))
    productId = Column(Integer, ForeignKey('product.Id'))
    amount = Column(Integer)

