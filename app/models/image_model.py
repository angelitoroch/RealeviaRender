from pydantic import BaseModel

class ImageData(BaseModel):
    name: str
    style: str
    color: str
    detalle: int