from pydantic import BaseModel

class Agreement(BaseModel):
    message: str
    price: int
    deadline_hours: int
    accepted: bool
