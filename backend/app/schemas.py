from pydantic import BaseModel, Field
from typing import List, Dict

class Message(BaseModel):
    date: str = Field(..., description="Fecha del mensaje extraída por el parser", examples=["31/3/2026"])
    hour: str = Field(..., description="Hora del mensaje (formato 24h o 12h con indicador)", examples=["18:11", "6:11 p. m."])
    user: str = Field(..., description="Nombre del usuario o 'Sistema'", examples=["Juan Perez"])
    message: str = Field(..., description="Contenido del mensaje, incluyendo cadenas multilínea", examples=["Este es un mensaje de ejemplo."])

class UserCount(BaseModel):
    user: str = Field(..., description="Nombre del usuario", examples=["Juan Perez"])
    count: int = Field(..., description="Cantidad total de mensajes enviados por el usuario", examples=[142])
    
class WordCloudItem(BaseModel):
    text: str = Field(..., description="Palabra filtrada libre de stop words y metadatos multimedia (WBS 2.2.1)", examples=["proyecto"])
    value: int = Field(..., description="Frecuencia de la palabra en el chat", examples=[5])

class Emoji(BaseModel):
    text: str = Field(..., description="Carácter Unicode del emoji unificado sin modificador de piel (WBS 2.2.2)", examples=["👍"])
    value: int = Field(..., description="Frecuencia de uso del emoji en el chat", examples=[20])

class AnalyticsExpanded(BaseModel):
    most_active_user: Dict = Field(
        ..., 
        description="Métrica del usuario que más mensajes envió (WBS 1.2.2)",
        examples=[{"user": "Juan Perez", "messages_total": 350}]
    )
    peak_time: Dict = Field(
        ..., 
        description="Franja horaria de 60 minutos con mayor cantidad de mensajes (WBS 1.2.3)",
        examples=[{"peak_time": "18:00 - 18:59", "messages_total": 120}]
    )
    active_days: List[Dict] = Field(
        ..., 
        description="Top 3 de fechas calendario con mayor actividad registrada (WBS 1.2.4)",
        examples=[[{"date": "31/3/2026", "messages_total": 450}]]
    )
    hour_buckets: List[int] = Field(
        default=[],
        description="Vector estático de 24 posiciones (0-23). Contiene el conteo de actividad por hora (WBS 2.2.3)",
        examples=[[12, 5, 0, 0, 0, 0, 8, 24, 45, 110, 85, 90, 130, 40, 55, 70, 150, 210, 340, 180, 95, 60, 30, 15]]
    )
    top_users: List[UserCount] = Field(
        default=[], 
        description="Ranking de los 10 usuarios más activos del chat grupal (WBS 2.1.1)"
    )
    word_cloud: List[WordCloudItem] = Field(
        default=[], 
        description="Colección de las 50 palabras más frecuentes para gráficos de nube de palabras (WBS 2.2.1)"
    )
    top_emojis: List[Emoji] = Field(
        default=[], 
        description="Listado detallado de los emojis más utilizados con limpieza Unicode aplicada (WBS 2.2.2)"
    )

class ChatResponse(BaseModel):
    chat_name: str = Field(..., description="Nombre del archivo original procesado", examples=["chat_is3.txt"])
    messages_total: int = Field(..., description="Métrica base del total de mensajes válidos parseados (WBS 1.2.1)", examples=[1542])
    analytics: AnalyticsExpanded = Field(..., description="Objeto contenedor de métricas analíticas (WBS 1.2.2 a 2.2.3)")

