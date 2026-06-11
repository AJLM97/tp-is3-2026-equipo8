from pydantic import BaseModel
from typing import List, Dict

class Message(BaseModel):
    date: str
    hour: str
    user: str
    message: str

class UserCount(BaseModel):
    user: str
    count: int
    
class WordCloudItem(BaseModel):
    text: str
    value: int

class AnalyticsExpanded(BaseModel):
    most_active_user: Dict
    peak_time: Dict
    active_days: List[Dict]
    hour_buckets: List[int] = []
    top_users: List[UserCount] = []
    word_cloud: List[WordCloudItem] = []

class ChatResponse(BaseModel):
    chat_name: str
    messages_total: int
    analytics: AnalyticsExpanded