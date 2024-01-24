from pydantic import BaseModel, Field


class ItemSchema(BaseModel):
    name: str = Field(min_length=5, max_length=255)
    price: float
