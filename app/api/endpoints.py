from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload/")
async def upload_image(
    name: str = Form(...),
    style: str = Form(...),
    color: str = Form(...),
    detalle: int = Form(...),
    image: UploadFile = File(...)
):
    return JSONResponse(content={"message": "Imagen recibida", "nombre": name})
