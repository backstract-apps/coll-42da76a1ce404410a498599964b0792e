from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_products(db: Session):

    query = db.query(models.Products)

    products_all = query.all()
    products_all = (
        [new_data.to_dict() for new_data in products_all]
        if products_all
        else products_all
    )
    res = {
        "products_all": products_all,
    }
    return res


async def post_products(db: Session, raw_data: schemas.PostProducts):
    product_id: int = raw_data.product_id
    product_name: str = raw_data.product_name
    description: str = raw_data.description
    price: float = raw_data.price
    image_url: str = raw_data.image_url
    seller_id: int = raw_data.seller_id

    record_to_be_added = {
        "price": price,
        "image_url": image_url,
        "seller_id": seller_id,
        "product_id": product_id,
        "description": description,
        "product_name": product_name,
    }
    new_products = models.Products(**record_to_be_added)
    db.add(new_products)
    db.commit()
    db.refresh(new_products)
    products_inserted_record = new_products.to_dict()

    res = {
        "products_inserted_record": products_inserted_record,
    }
    return res


async def put_products_product_id(
    db: Session,
    product_id: int,
    product_name: str,
    description: str,
    price: float,
    image_url: str,
    seller_id: int,
):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.product_id == product_id))
    products_edited_record = query.first()

    if products_edited_record:
        for key, value in {
            "price": price,
            "image_url": image_url,
            "seller_id": seller_id,
            "product_id": product_id,
            "description": description,
            "product_name": product_name,
        }.items():
            setattr(products_edited_record, key, value)

        db.commit()
        db.refresh(products_edited_record)

        products_edited_record = (
            products_edited_record.to_dict()
            if hasattr(products_edited_record, "to_dict")
            else vars(products_edited_record)
        )
    res = {
        "products_edited_record": products_edited_record,
    }
    return res


async def delete_products_product_id(db: Session, product_id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.product_id == product_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        products_deleted = record_to_delete.to_dict()
    else:
        products_deleted = record_to_delete
    res = {
        "products_deleted": products_deleted,
    }
    return res


async def get_sellers(db: Session):

    query = db.query(models.Sellers)

    sellers_all = query.all()
    sellers_all = (
        [new_data.to_dict() for new_data in sellers_all] if sellers_all else sellers_all
    )
    res = {
        "sellers_all": sellers_all,
    }
    return res


async def get_sellers_seller_id(db: Session, seller_id: int):

    query = db.query(models.Sellers)
    query = query.filter(and_(models.Sellers.seller_id == seller_id))

    sellers_one = query.first()

    sellers_one = (
        (
            sellers_one.to_dict()
            if hasattr(sellers_one, "to_dict")
            else vars(sellers_one)
        )
        if sellers_one
        else sellers_one
    )

    res = {
        "sellers_one": sellers_one,
    }
    return res


async def post_sellers(db: Session, raw_data: schemas.PostSellers):
    seller_id: int = raw_data.seller_id
    seller_name: str = raw_data.seller_name
    contact_details: str = raw_data.contact_details
    seller_rating: float = raw_data.seller_rating

    record_to_be_added = {
        "seller_id": seller_id,
        "seller_name": seller_name,
        "seller_rating": seller_rating,
        "contact_details": contact_details,
    }
    new_sellers = models.Sellers(**record_to_be_added)
    db.add(new_sellers)
    db.commit()
    db.refresh(new_sellers)
    sellers_inserted_record = new_sellers.to_dict()

    res = {
        "sellers_inserted_record": sellers_inserted_record,
    }
    return res


async def put_sellers_seller_id(
    db: Session,
    seller_id: int,
    seller_name: str,
    contact_details: str,
    seller_rating: float,
):

    query = db.query(models.Sellers)
    query = query.filter(and_(models.Sellers.seller_id == seller_id))
    sellers_edited_record = query.first()

    if sellers_edited_record:
        for key, value in {
            "seller_id": seller_id,
            "seller_name": seller_name,
            "seller_rating": seller_rating,
            "contact_details": contact_details,
        }.items():
            setattr(sellers_edited_record, key, value)

        db.commit()
        db.refresh(sellers_edited_record)

        sellers_edited_record = (
            sellers_edited_record.to_dict()
            if hasattr(sellers_edited_record, "to_dict")
            else vars(sellers_edited_record)
        )
    res = {
        "sellers_edited_record": sellers_edited_record,
    }
    return res


async def delete_sellers_seller_id(db: Session, seller_id: int):

    query = db.query(models.Sellers)
    query = query.filter(and_(models.Sellers.seller_id == seller_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        sellers_deleted = record_to_delete.to_dict()
    else:
        sellers_deleted = record_to_delete
    res = {
        "sellers_deleted": sellers_deleted,
    }
    return res


async def get_customers(db: Session):

    query = db.query(models.Customers)

    customers_all = query.all()
    customers_all = (
        [new_data.to_dict() for new_data in customers_all]
        if customers_all
        else customers_all
    )
    res = {
        "customers_all": customers_all,
    }
    return res


async def get_customers_customer_id(db: Session, customer_id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))

    customers_one = query.first()

    customers_one = (
        (
            customers_one.to_dict()
            if hasattr(customers_one, "to_dict")
            else vars(customers_one)
        )
        if customers_one
        else customers_one
    )

    res = {
        "customers_one": customers_one,
    }
    return res


async def post_customers(db: Session, raw_data: schemas.PostCustomers):
    customer_id: int = raw_data.customer_id
    customer_name: str = raw_data.customer_name
    address: str = raw_data.address
    contact_details: str = raw_data.contact_details

    record_to_be_added = {
        "address": address,
        "customer_id": customer_id,
        "customer_name": customer_name,
        "contact_details": contact_details,
    }
    new_customers = models.Customers(**record_to_be_added)
    db.add(new_customers)
    db.commit()
    db.refresh(new_customers)
    customers_inserted_record = new_customers.to_dict()

    res = {
        "customers_inserted_record": customers_inserted_record,
    }
    return res


async def put_customers_customer_id(
    db: Session,
    customer_id: int,
    customer_name: str,
    address: str,
    contact_details: str,
):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))
    customers_edited_record = query.first()

    if customers_edited_record:
        for key, value in {
            "address": address,
            "customer_id": customer_id,
            "customer_name": customer_name,
            "contact_details": contact_details,
        }.items():
            setattr(customers_edited_record, key, value)

        db.commit()
        db.refresh(customers_edited_record)

        customers_edited_record = (
            customers_edited_record.to_dict()
            if hasattr(customers_edited_record, "to_dict")
            else vars(customers_edited_record)
        )
    res = {
        "customers_edited_record": customers_edited_record,
    }
    return res


async def delete_customers_customer_id(db: Session, customer_id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        customers_deleted = record_to_delete.to_dict()
    else:
        customers_deleted = record_to_delete
    res = {
        "customers_deleted": customers_deleted,
    }
    return res


async def get_orders(db: Session):

    query = db.query(models.Orders)

    orders_all = query.all()
    orders_all = (
        [new_data.to_dict() for new_data in orders_all] if orders_all else orders_all
    )
    res = {
        "orders_all": orders_all,
    }
    return res


async def get_orders_order_id(db: Session, order_id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.order_id == order_id))

    orders_one = query.first()

    orders_one = (
        (orders_one.to_dict() if hasattr(orders_one, "to_dict") else vars(orders_one))
        if orders_one
        else orders_one
    )

    res = {
        "orders_one": orders_one,
    }
    return res


async def post_orders(db: Session, raw_data: schemas.PostOrders):
    order_id: int = raw_data.order_id
    order_date: str = raw_data.order_date
    shipping_address: str = raw_data.shipping_address
    total_cost: float = raw_data.total_cost
    customer_id: int = raw_data.customer_id

    record_to_be_added = {
        "order_id": order_id,
        "order_date": order_date,
        "total_cost": total_cost,
        "customer_id": customer_id,
        "shipping_address": shipping_address,
    }
    new_orders = models.Orders(**record_to_be_added)
    db.add(new_orders)
    db.commit()
    db.refresh(new_orders)
    orders_inserted_record = new_orders.to_dict()

    res = {
        "orders_inserted_record": orders_inserted_record,
    }
    return res


async def put_orders_order_id(
    db: Session,
    order_id: int,
    order_date: str,
    shipping_address: str,
    total_cost: float,
    customer_id: int,
):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.order_id == order_id))
    orders_edited_record = query.first()

    if orders_edited_record:
        for key, value in {
            "order_id": order_id,
            "order_date": order_date,
            "total_cost": total_cost,
            "customer_id": customer_id,
            "shipping_address": shipping_address,
        }.items():
            setattr(orders_edited_record, key, value)

        db.commit()
        db.refresh(orders_edited_record)

        orders_edited_record = (
            orders_edited_record.to_dict()
            if hasattr(orders_edited_record, "to_dict")
            else vars(orders_edited_record)
        )
    res = {
        "orders_edited_record": orders_edited_record,
    }
    return res


async def delete_orders_order_id(db: Session, order_id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.order_id == order_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        orders_deleted = record_to_delete.to_dict()
    else:
        orders_deleted = record_to_delete
    res = {
        "orders_deleted": orders_deleted,
    }
    return res


async def get_order_items(db: Session):

    query = db.query(models.OrderItems)

    order_items_all = query.all()
    order_items_all = (
        [new_data.to_dict() for new_data in order_items_all]
        if order_items_all
        else order_items_all
    )
    res = {
        "order_items_all": order_items_all,
    }
    return res


async def get_order_items_order_item_id(db: Session, order_item_id: int):

    query = db.query(models.OrderItems)
    query = query.filter(and_(models.OrderItems.order_item_id == order_item_id))

    order_items_one = query.first()

    order_items_one = (
        (
            order_items_one.to_dict()
            if hasattr(order_items_one, "to_dict")
            else vars(order_items_one)
        )
        if order_items_one
        else order_items_one
    )

    res = {
        "order_items_one": order_items_one,
    }
    return res


async def post_order_items(db: Session, raw_data: schemas.PostOrderItems):
    order_item_id: int = raw_data.order_item_id
    order_id: int = raw_data.order_id
    product_id: int = raw_data.product_id
    quantity: int = raw_data.quantity

    record_to_be_added = {
        "order_id": order_id,
        "quantity": quantity,
        "product_id": product_id,
        "order_item_id": order_item_id,
    }
    new_order_items = models.OrderItems(**record_to_be_added)
    db.add(new_order_items)
    db.commit()
    db.refresh(new_order_items)
    order_items_inserted_record = new_order_items.to_dict()

    res = {
        "order_items_inserted_record": order_items_inserted_record,
    }
    return res


async def put_order_items_order_item_id(
    db: Session, order_item_id: int, order_id: int, product_id: int, quantity: int
):

    query = db.query(models.OrderItems)
    query = query.filter(and_(models.OrderItems.order_item_id == order_item_id))
    order_items_edited_record = query.first()

    if order_items_edited_record:
        for key, value in {
            "order_id": order_id,
            "quantity": quantity,
            "product_id": product_id,
            "order_item_id": order_item_id,
        }.items():
            setattr(order_items_edited_record, key, value)

        db.commit()
        db.refresh(order_items_edited_record)

        order_items_edited_record = (
            order_items_edited_record.to_dict()
            if hasattr(order_items_edited_record, "to_dict")
            else vars(order_items_edited_record)
        )
    res = {
        "order_items_edited_record": order_items_edited_record,
    }
    return res


async def delete_order_items_order_item_id(db: Session, order_item_id: int):

    query = db.query(models.OrderItems)
    query = query.filter(and_(models.OrderItems.order_item_id == order_item_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        order_items_deleted = record_to_delete.to_dict()
    else:
        order_items_deleted = record_to_delete
    res = {
        "order_items_deleted": order_items_deleted,
    }
    return res


async def get_products_product_id(db: Session, product_id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.product_id == product_id))

    products_one = query.first()

    products_one = (
        (
            products_one.to_dict()
            if hasattr(products_one, "to_dict")
            else vars(products_one)
        )
        if products_one
        else products_one
    )

    test = aliased(models.Sellers)
    query = db.query(models.Products, test)

    query = query.join(
        test, and_(models.Products.product_id == models.Products.product_id)
    )

    test_1 = query.first()
    test_1 = (
        [
            {
                "test_1_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
                "test_1_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
            }
            for s1, s2 in test_1
        ]
        if test_1
        else test_1
    )

    res = {
        "products_one": products_one,
        "test_1": test_1,
    }
    return res


async def post_user(db: Session, raw_data: schemas.PostUser):
    name: str = raw_data.name

    record_to_be_added = {"id": id, "name": name, "customer_name": name}
    new_user = models.User(**record_to_be_added)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user = new_user.to_dict()

    record_to_be_added = {"customer_name": name}
    new_customers = models.Customers(**record_to_be_added)
    db.add(new_customers)
    db.commit()
    db.refresh(new_customers)
    lkfgdhgj = new_customers.to_dict()

    res = {
        "user": user,
    }
    return res
