from fastapi import FastAPI, File, Form, UploadFile
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Obtener clave API
api_key = os.getenv("OPENAI_API_KEY")

# Instancia moderna del cliente OpenAI
client = OpenAI(api_key=api_key)

app = FastAPI()

@app.post("/upload/")
async def upload_image(
    name: str = Form(...),
    style: str = Form(...),
    color: str = Form(...),
    detalle: int = Form(...),
    image: UploadFile = File(...),
):
    # Aquí iría la lógica de guardado/uso de imagen
    mensaje = f"Hola, quiero transformar la imagen de {name} al estilo {style} con color base {color} y detalle {detalle}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": mensaje}],
        temperature=0.7,
    )

    return {"respuesta": response.choices[0].message.content}