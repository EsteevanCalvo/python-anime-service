# Microservicio de Personajes de Anime (Python + MongoDB)

Microservicio REST en FastAPI que lee y escribe 10 personajes de anime en
una base de datos MongoDB alojada en la nube. Swagger se genera solo
(FastAPI lo incluye por defecto).

## Correrlo en tu computadora

1. (Recomendado) crea un entorno virtual:
   `python -m venv venv` y actívalo.
2. `pip install -r requirements.txt`
3. Copia `.env.example` a `.env` y coloca tu `MONGO_URI` real.
4. Inserta los 10 personajes de ejemplo: `python seed.py`
5. Arranca el servidor: `uvicorn main:app --reload`
6. Abre `http://localhost:8000/docs` para ver la documentación Swagger
   (interactiva: puedes probar cada endpoint desde ahí).

## Desplegarlo públicamente (Render)

1. Sube esta carpeta a un repositorio de GitHub (sin la carpeta `venv`,
   ya está en `.gitignore`).
2. En https://render.com crea un **New Web Service** apuntando a ese repo.
3. Runtime: Python 3
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. En **Environment**, agrega la variable `MONGO_URI` con tu cadena de
   conexión real de MongoDB Atlas.
7. Despliega. Tu servicio quedará en una URL como
   `https://tu-servicio.onrender.com`.
8. La documentación pública quedará en
   `https://tu-servicio.onrender.com/docs` — ese es el link que debes
   entregar.

(En Railway: mismo repo, mismo Start Command, misma variable de entorno
`MONGO_URI`.)

## Endpoints

| Método | Ruta                      | Descripción               |
|--------|---------------------------|----------------------------|
| GET    | /api/personajes           | Lista los 10 personajes    |
| GET    | /api/personajes/{id}      | Obtiene uno por id         |
| POST   | /api/personajes           | Crea uno nuevo             |
| PUT    | /api/personajes/{id}      | Actualiza uno              |
| DELETE | /api/personajes/{id}      | Elimina uno                |
| GET    | /docs                     | Documentación Swagger      |
