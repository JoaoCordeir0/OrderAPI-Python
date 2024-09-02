from fastapi import APIRouter, Depends
from src.controllers.ProductController import ProductController
from src.controllers.OrderController import OrderController
from src.requests.ProductRequest import ProductRequest
from src.requests.OrderRequest import OrderRequest

router = APIRouter()

@router.get("/")
def main():
    return {
        "info": {
            "name": "Stefanini teste",
        },
        "dev": "João Victor Cordeiro",        
    }

@router.get('/api/product/list')
async def product_list():        
    return ProductController().list()

@router.get('/api/product/{id}')
async def product_get(id: int):        
    return ProductController().get(id)

@router.post('/api/product/add')
async def product_add(request: ProductRequest):        
    return ProductController().add(request)

@router.put('/api/product/edit')
async def product_edit(request: ProductRequest):        
    return ProductController().edit(request)

@router.delete('/api/product/{id}')
async def product_delete(id):        
    return ProductController().delete(id)

@router.get('/api/order/list')
async def order_list():        
    return OrderController().list()

@router.get('/api/order/{id}')
async def order_get(id: int):        
    return OrderController().get(id)

@router.post('/api/order/add')
async def order_add(request: OrderRequest):        
    return OrderController().add(request)
