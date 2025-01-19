from pydantic import BaseModel
from datetime import datetime

class Operation(BaseModel):
    expression: str
    result: float
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True
