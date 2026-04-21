from fastapi import APIRouter, UploadFile, File, HTTPException
from app import schemas

router = APIRouter()

@router.post("/upload", response_model=schemas.ChatResponse)
async def upload_file(file: UploadFile = File(...)):
    return {
        "chat_name": file.filename,
    }