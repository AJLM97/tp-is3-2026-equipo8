from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    date: str
    hour: str
    user: str
    message: str

class ChatResponse(BaseModel):
    chat_name: str
    messages_total: int
    analytics: dict