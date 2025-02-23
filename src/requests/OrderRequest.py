from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderRequest(BaseModel):
    
    """NOTE: Classe modelo do pedido"""

    orderId: Optional[int] = None
    clientName: Optional[str] = None
    clientEmail: Optional[str] = None
    creationDate: Optional[datetime] = None
    paid: Optional[bool] = None
    productId: int    
    amount: int
    