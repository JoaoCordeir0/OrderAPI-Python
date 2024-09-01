from pydantic import BaseModel
from typing import Optional

class ProductRequest(BaseModel):
    
    """NOTE: Classe modelo do produto"""

    id: Optional[int] = None
    ProductName: str
    Value: float