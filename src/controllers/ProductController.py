from src.database.Engine import Engine
from src.database.Bases import Product

class ProductController:

    """NOTE: Classe que controla as requisições de produto"""

    session = None

    def __init__(self) -> None:
        self.session = Engine().get_session()

    def list(self):        
        products = self.session.query(Product).all()
        return products

    def get(self, id):
        product = self.session.query(Product).filter(Product.Id == id).first()
        return product

    def add(self, data):
        try:
            product = Product(ProductName=data.ProductName, Value=data.Value)
            self.session.add(product)
            self.session.commit()
            return {
                'status': 'success',
                'message': 'Product insert success!'
            }
        except Exception:
            return {
                'status': 'error',
                'message': 'Product error!'
            }

    