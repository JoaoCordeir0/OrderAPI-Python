from src.database.Engine import Engine
from src.database.Bases import Order, ItemOrder, Product
from src.controllers.ProductController import ProductController

class OrderController:

    """NOTE: Classe que controla as requisições de pedidos"""

    session = None

    def __init__(self) -> None:
        self.session = Engine().get_session()

    def list(self):
        data = []
        orders = self.session.query(ItemOrder, Product, Order).join(Product, ItemOrder.ProductId == Product.Id).join(Order, ItemOrder.OrderId == Order.Id).all()
        for item, product, order in orders:
            data.append({
                'item': item,
                'product': product,
                'order': order
            })
        return data
    
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
                'id': item.Id,
                'productId': product.Id,
                'productName': product.ProductName,
                'unitValue': product.Value,
                'amount': item.Amount,
            })
            totalValue += product.Value * item.Amount

        data.append({
            'id': order.Id,
            'clientName': order.ClientName,
            'clientEmail': order.ClientEmail,
            'paid': order.Paid,
            'totalValue': totalValue,
            'itemsOrder': products
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
            if data.OrderId == None:                    
                order = Order(
                    ClientName=data.ClientName,
                    ClientEmail=data.ClientEmail,
                    CreationDate=data.CreationDate,
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

    