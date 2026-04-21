from pydantic import BaseModel

class ChatResponse(BaseModel):
    chat_name: str