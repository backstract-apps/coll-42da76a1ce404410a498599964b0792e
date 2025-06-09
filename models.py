from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Products(Base):
    __tablename__ = 'products'
    product_id = Column(String, primary_key=True)
    product_name = Column(String, primary_key=False)
    description = Column(String, primary_key=False)
    price = Column(Float, primary_key=False)
    image_url = Column(String, primary_key=False)
    seller_id = Column(Integer, primary_key=False)


class Sellers(Base):
    __tablename__ = 'sellers'
    seller_id = Column(String, primary_key=True)
    seller_name = Column(String, primary_key=False)
    contact_details = Column(String, primary_key=False)
    seller_rating = Column(Float, primary_key=False)


class Customers(Base):
    __tablename__ = 'customers'
    customer_id = Column(String, primary_key=True)
    customer_name = Column(String, primary_key=False)
    address = Column(String, primary_key=False)
    contact_details = Column(String, primary_key=False)


class Orders(Base):
    __tablename__ = 'orders'
    order_id = Column(String, primary_key=True)
    order_date = Column(String, primary_key=False)
    shipping_address = Column(String, primary_key=False)
    total_cost = Column(Float, primary_key=False)
    customer_id = Column(Integer, primary_key=False)


class OrderItems(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(String, primary_key=True)
    order_id = Column(Integer, primary_key=False)
    product_id = Column(Integer, primary_key=False)
    quantity = Column(Integer, primary_key=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)


