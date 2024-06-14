from pydantic import BaseModel


class ImageSchema(BaseModel):
    image: str
