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
        product = self.session.query(Product).filter(Product.id == id).first()
        return product

    def add(self, data):
        try:
            product = Product(
                productName=data.productName, 
                value=data.value
            )
            self.session.add(product)
            self.session.commit()
            return {                
                'message': 'Product insert success!'
            }
        except Exception:
            return {                
                'message': 'Product error!'
            }

    def edit(self, data):
        product = self.session.query(Product).filter(Product.id == data.id).first()

        if product:            
            if data.productName:
                product.productName = data.productName
            if data.value:
                product.value = data.value           

            self.session.commit()
            return {                
                'message': 'Product edited success!'
            }
        return {                
            'message': 'Product not found!'
        }    

    def delete(self, id):
        product = self.session.query(Product).filter(Product.id == id).first()

        if product:            
            self.session.delete(product)            
            self.session.commit()
            return {                
                'message': 'Product delete success!'
            }
        return {                
            'message': 'Product not found!'
        }    
    