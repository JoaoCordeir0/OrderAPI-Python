from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderRequest(BaseModel):
    
    """NOTE: Classe modelo do produto"""

    OrderId: Optional[int] = None
    ClientName: Optional[str] = None
    ClientEmail: Optional[str] = None
    CreationDate: Optional[datetime] = None
    Paid: Optional[bool] = None
    ProductId: int    
    Amount: int
    