from pydantic import BaseModel


class Data(BaseModel):
    base64str: str
