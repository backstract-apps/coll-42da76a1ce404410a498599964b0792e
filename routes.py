from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/products/')
async def get_products(db: Session = Depends(get_db)):
    try:
        return await service.get_products(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/products/')
async def post_products(raw_data: schemas.PostProducts, db: Session = Depends(get_db)):
    try:
        return await service.post_products(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/products/product_id/')
async def put_products_product_id(product_id: int, product_name: Annotated[str, Query(max_length=100)], description: Annotated[str, Query(max_length=100)], price: float, image_url: Annotated[str, Query(max_length=100)], seller_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_products_product_id(db, product_id, product_name, description, price, image_url, seller_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/products/product_id')
async def delete_products_product_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_products_product_id(db, product_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/sellers/')
async def get_sellers(db: Session = Depends(get_db)):
    try:
        return await service.get_sellers(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/sellers/seller_id')
async def get_sellers_seller_id(seller_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_sellers_seller_id(db, seller_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/sellers/')
async def post_sellers(raw_data: schemas.PostSellers, db: Session = Depends(get_db)):
    try:
        return await service.post_sellers(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/sellers/seller_id/')
async def put_sellers_seller_id(seller_id: int, seller_name: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], seller_rating: float, db: Session = Depends(get_db)):
    try:
        return await service.put_sellers_seller_id(db, seller_id, seller_name, contact_details, seller_rating)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/sellers/seller_id')
async def delete_sellers_seller_id(seller_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_sellers_seller_id(db, seller_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/')
async def get_customers(db: Session = Depends(get_db)):
    try:
        return await service.get_customers(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/customer_id')
async def get_customers_customer_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_customers_customer_id(db, customer_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/customers/')
async def post_customers(raw_data: schemas.PostCustomers, db: Session = Depends(get_db)):
    try:
        return await service.post_customers(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/customers/customer_id/')
async def put_customers_customer_id(customer_id: int, customer_name: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_customers_customer_id(db, customer_id, customer_name, address, contact_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/customers/customer_id')
async def delete_customers_customer_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_customers_customer_id(db, customer_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/')
async def get_orders(db: Session = Depends(get_db)):
    try:
        return await service.get_orders(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/order_id')
async def get_orders_order_id(order_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_orders_order_id(db, order_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/orders/')
async def post_orders(raw_data: schemas.PostOrders, db: Session = Depends(get_db)):
    try:
        return await service.post_orders(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/orders/order_id/')
async def put_orders_order_id(order_id: int, order_date: Annotated[str, Query(max_length=100)], shipping_address: Annotated[str, Query(max_length=100)], total_cost: float, customer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_orders_order_id(db, order_id, order_date, shipping_address, total_cost, customer_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/orders/order_id')
async def delete_orders_order_id(order_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_orders_order_id(db, order_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/order_items/')
async def get_order_items(db: Session = Depends(get_db)):
    try:
        return await service.get_order_items(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/order_items/order_item_id')
async def get_order_items_order_item_id(order_item_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_order_items_order_item_id(db, order_item_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/order_items/')
async def post_order_items(raw_data: schemas.PostOrderItems, db: Session = Depends(get_db)):
    try:
        return await service.post_order_items(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/order_items/order_item_id/')
async def put_order_items_order_item_id(order_item_id: int, order_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    try:
        return await service.put_order_items_order_item_id(db, order_item_id, order_id, product_id, quantity)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/order_items/order_item_id')
async def delete_order_items_order_item_id(order_item_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_order_items_order_item_id(db, order_item_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/products/product_id')
async def get_products_product_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_products_product_id(db, product_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user')
async def post_user(raw_data: schemas.PostUser, db: Session = Depends(get_db)):
    try:
        return await service.post_user(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

