from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderEditRequest(BaseModel):
    
    """NOTE: Classe modelo do pedido"""

    id: int = None
    clientName: Optional[str] = None
    clientEmail: Optional[str] = None
    creationDate: Optional[datetime] = None
    paid: Optional[bool] = None    
    