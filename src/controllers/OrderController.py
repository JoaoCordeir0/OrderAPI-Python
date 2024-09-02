from src.database.Engine import Engine
from src.database.Bases import Order, ItemOrder, Product
from src.controllers.ProductController import ProductController
from datetime import datetime

class OrderController:

    """NOTE: Classe que controla as requisições de pedidos"""

    session = None

    def __init__(self) -> None:
        self.session = Engine().get_session()

    def list(self):        
        orders = self.session.query(Order).all()        
        return orders
    
    def get(self, id):
        data = []
        order = self.session.query(Order).filter(Order.id == id).first()

        if order == None:                
            return {                
                'message': 'Order not found!'
            }     
        
        items = self.session.query(ItemOrder).filter(ItemOrder.orderId == id).all()
        
        totalValue = 0
        products = []
        for item in items:
            product = self.session.query(Product).filter(Product.id == item.productId).first()
            products.append({
                'id': item.id,
                'productId': product.id,
                'productName': product.productName,
                'unitValue': product.value,
                'amount': item.amount,
            })
            totalValue += product.value * item.amount

        data.append({
            'id': order.id,
            'clientName': order.clientName,
            'clientEmail': order.clientEmail,
            'paid': order.paid,
            'totalValue': totalValue,
            'items': products
        })
        return data[0]

    def add(self, data):
        try:
            if data.amount < 1:
                return {                    
                    'message': 'The quantity must be equal to or greater than 1!'
                }
            
            product = ProductController().get(data.productId)

            if product == None:                
                return {                    
                    'message': 'Product not found!'
                }            

            # Caso o id do pedido não for passado, cria o pedido com as info do usuário
            if data.orderId == None or data.orderId == 0:                    
                order = Order(
                    clientName=data.clientName,
                    clientEmail=data.clientEmail,
                    creationDate=datetime.now(),
                    paid=data.paid
                )
                self.session.add(order)
                self.session.commit()
                data.orderId = order.id

            item = ItemOrder(
                orderId=data.orderId,
                productId=data.productId,
                amount=data.amount
            )
            self.session.add(item)
            self.session.commit()

            return {                
                'message': 'Order insert success!'
            }
        except Exception:
            return {                
                'message': 'Order error!'                                
            }

    