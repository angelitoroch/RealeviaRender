
# Proyecto Web: Formulario con Backend en FastAPI

Este proyecto incluye un **formulario frontend** desarrollado con HTML + Tailwind CSS, y un **backend en Python con FastAPI** para recibir y procesar imágenes.

---

## 🧩 Requisitos en Visual Studio Code

### Extensiones recomendadas:
- **Python** (Microsoft): Soporte para ejecución y depuración de código Python.
- **Live Server**: Levanta un servidor local para ver el frontend.

---

## 🐍 Preparar el Backend

### 1. Abre VS Code en la carpeta `mi_proyecto`
```bash
cd mi_proyecto
```

### 2. Crea y activa un entorno virtual
```bash
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate        # Windows
```

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecuta el backend
```bash
uvicorn app.main:app --reload
```

El backend se iniciará en [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🌐 Preparar el Frontend

### 1. Asegúrate de que el `form` en tu HTML tenga este `action`:
```html
<form action="http://127.0.0.1:8000/upload/" method="POST" enctype="multipart/form-data" id="uploadForm">
```

### 2. Asegúrate de que tu `form` tenga este `id`:
```html
<form id="uploadForm"> ... </form>
```

### 3. Incluye correctamente tu script JS:
```html
<script src="ruta/relativa/a/tu/upload.js" defer></script>
```

---

## 🧪 Ejecutar el Frontend

### 1. Usa la extensión Live Server:
Haz clic derecho sobre tu archivo `index.html` → **"Open with Live Server"**

Verifica que se abra en algo como: [http://127.0.0.1:5500](http://127.0.0.1:5500)

---

## ⚠️ Problemas comunes

| Problema              | Causa                                           | Solución                                  |
|----------------------|--------------------------------------------------|-------------------------------------------|
| JS no se ejecuta     | ID incorrecto o mal referenciado                 | Asegúrate de tener `id="uploadForm"`      |
| Error CORS           | El backend no acepta peticiones externas         | Agrega middleware CORS a FastAPI          |
| `fetch` falla        | URL mal escrita o backend no corriendo           | Verifica el `action` y que Uvicorn esté activo |

---

## 📦 Estructura del proyecto

```
mi_proyecto/
│
├── app/
│   ├── api/
│   │   └── endpoints.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── image_model.py
│   ├── services/
│   │   └── image_service.py
│   ├── utils/
│   │   └── helpers.py
│   └── main.py
│
├── static/
├── templates/
├── tests/
│   └── test_api.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```
