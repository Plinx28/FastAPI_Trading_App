from datetime import datetime
from pydantic import BaseModel

class OperationCreate(BaseModel):
    operation_number: str
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str