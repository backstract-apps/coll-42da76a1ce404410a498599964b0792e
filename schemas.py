from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Products(BaseModel):
    product_id: Any
    product_name: str
    description: str
    price: float
    image_url: str
    seller_id: int


class ReadProducts(BaseModel):
    product_id: Any
    product_name: str
    description: str
    price: float
    image_url: str
    seller_id: int
    class Config:
        from_attributes = True


class Sellers(BaseModel):
    seller_id: Any
    seller_name: str
    contact_details: str
    seller_rating: float


class ReadSellers(BaseModel):
    seller_id: Any
    seller_name: str
    contact_details: str
    seller_rating: float
    class Config:
        from_attributes = True


class Customers(BaseModel):
    customer_id: Any
    customer_name: str
    address: str
    contact_details: str


class ReadCustomers(BaseModel):
    customer_id: Any
    customer_name: str
    address: str
    contact_details: str
    class Config:
        from_attributes = True


class Orders(BaseModel):
    order_id: Any
    order_date: Any
    shipping_address: str
    total_cost: float
    customer_id: int


class ReadOrders(BaseModel):
    order_id: Any
    order_date: Any
    shipping_address: str
    total_cost: float
    customer_id: int
    class Config:
        from_attributes = True


class OrderItems(BaseModel):
    order_item_id: Any
    order_id: int
    product_id: int
    quantity: int


class ReadOrderItems(BaseModel):
    order_item_id: Any
    order_id: int
    product_id: int
    quantity: int
    class Config:
        from_attributes = True


class User(BaseModel):
    id: int
    name: str


class ReadUser(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True




class PostProducts(BaseModel):
    product_id: int = Field(...)
    product_name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    price: Any = Field(...)
    image_url: str = Field(..., max_length=100)
    seller_id: int = Field(...)

    class Config:
        from_attributes = True



class PostSellers(BaseModel):
    seller_id: int = Field(...)
    seller_name: str = Field(..., max_length=100)
    contact_details: str = Field(..., max_length=100)
    seller_rating: Any = Field(...)

    class Config:
        from_attributes = True



class PostCustomers(BaseModel):
    customer_id: int = Field(...)
    customer_name: str = Field(..., max_length=100)
    address: str = Field(..., max_length=100)
    contact_details: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostOrders(BaseModel):
    order_id: int = Field(...)
    order_date: str = Field(..., max_length=100)
    shipping_address: str = Field(..., max_length=100)
    total_cost: Any = Field(...)
    customer_id: int = Field(...)

    class Config:
        from_attributes = True



class PostOrderItems(BaseModel):
    order_item_id: int = Field(...)
    order_id: int = Field(...)
    product_id: int = Field(...)
    quantity: int = Field(...)

    class Config:
        from_attributes = True



class PostUser(BaseModel):
    name: str = Field(..., max_length=100)

    @field_validator('name')
    def validate_name(cls, value: Optional[str]):
        if value is None:
            if False:
                return value
            else:
                raise ValueError("Field 'name' cannot be None")
        # Ensure re is imported in the generated file
        pattern= r'''^[a-zA-Z]+(?:[ -'][a-zA-Z]+)*$'''  
        if isinstance(value, str) and not re.match(pattern, value):
            # Use repr() for the regex pattern in the error for clarity
            raise ValueError(f"Field '{schema.key}' does not match regex pattern: {repr(schema.regularExpression)}")
        return value

    class Config:
        from_attributes = True

