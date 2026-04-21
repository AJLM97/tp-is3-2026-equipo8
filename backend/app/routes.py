from fastapi import APIRouter, UploadFile, File, HTTPException
from app import schemas, parser, analytics
import zipfile
import io

router = APIRouter()

@router.post("/upload", response_model=schemas.ChatResponse)
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename.lower()
    content = await file.read()
    
    if filename.endswith(".zip"):
        with zipfile.ZipFile(io.BytesIO(content)) as z:
            txt_files = [f for f in z.namelist() if f.endswith(".txt")]
            if not txt_files: raise HTTPException(400, "No hay .txt en el ZIP")
            with z.open(txt_files[0]) as f:
                texto = f.read().decode("utf-8", errors="ignore")
    elif filename.endswith(".txt"):
        texto = content.decode("utf-8", errors="ignore")
    else:
        raise HTTPException(400, "Solo se permiten archivos .txt o .zip")

    messages = parser.process_chat(texto)
    return {
        "chat_name": file.filename,
        "messages_total": analytics.obtener_cantidad_mensajes(messages),
        "analytics": {
            "most_active_user": analytics.usuario_mas_activo(messages),
            "peak_time": analytics.franja_horaria_pico(messages),
            "active_days": analytics.dias_mas_activos(messages)
        }
    }
