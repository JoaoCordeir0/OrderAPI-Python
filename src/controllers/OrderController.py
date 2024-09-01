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
        order = self.session.query(Order).filter(Order.Id == id).first()

        if order == None:                
            return {
                'status': 'warning',
                'message': 'Order not found!'
            }     
        
        items = self.session.query(ItemOrder).filter(ItemOrder.OrderId == id).all()
        
        totalValue = 0
        products = []
        for item in items:
            product = self.session.query(Product).filter(Product.Id == item.ProductId).first()
            products.append({
                'Id': item.Id,
                'ProductId': product.Id,
                'ProductName': product.ProductName,
                'UnitValue': product.Value,
                'Amount': item.Amount,
            })
            totalValue += product.Value * item.Amount

        data.append({
            'Id': order.Id,
            'ClientName': order.ClientName,
            'ClientEmail': order.ClientEmail,
            'Paid': order.Paid,
            'TotalValue': totalValue,
            'ItemsOrder': products
        })
        return data

    def add(self, data):
        try:
            if data.Amount < 1:
                return {
                    'status': 'warning',
                    'message': 'The quantity must be equal to or greater than 1!'
                }
            
            product = ProductController().get(data.ProductId)

            if product == None:                
                return {
                    'status': 'warning',
                    'message': 'Product not found!'
                }            

            # Caso o id do pedido não for passado, cria o pedido com as info do usuário
            if data.OrderId == None or data.OrderId == 0:                    
                order = Order(
                    ClientName=data.ClientName,
                    ClientEmail=data.ClientEmail,
                    CreationDate=datetime.now(),
                    Paid=data.Paid
                )
                self.session.add(order)
                self.session.commit()
                data.OrderId = order.Id

            item = ItemOrder(
                OrderId=data.OrderId,
                ProductId=data.ProductId,
                Amount=data.Amount
            )
            self.session.add(item)
            self.session.commit()

            return {
                'status': 'success',
                'message': 'Order insert success!'
            }
        except Exception:
            return {
                'status': 'error',
                'message': 'Order error!'                                
            }

    