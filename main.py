from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
from bson.errors import InvalidId

from database import coleccion_personajes
from models import Personaje, PersonajeConId

app = FastAPI(
    title="API de Personajes de Anime",
    description=(
        "Microservicio en Python (FastAPI) que consume una base de datos "
        "MongoDB en la nube con 10 personajes de anime."
    ),
    version="1.0.0",
    # /docs (Swagger UI) y /redoc se generan automaticamente con estos datos.
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def documento_a_json(doc) -> dict:
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


@app.get("/", tags=["Estado"])
def estado():
    """Verifica que el microservicio esté activo."""
    return {
        "mensaje": "Microservicio de personajes de anime funcionando",
        "documentacion": "/docs",
    }


@app.get("/api/personajes", response_model=list[PersonajeConId], tags=["Personajes"])
def listar_personajes():
    """Lista todos los personajes de anime almacenados en la base de datos."""
    documentos = coleccion_personajes.find()
    return [documento_a_json(doc) for doc in documentos]


@app.get("/api/personajes/{personaje_id}", response_model=PersonajeConId, tags=["Personajes"])
def obtener_personaje(personaje_id: str):
    """Obtiene un personaje por su id de MongoDB."""
    try:
        oid = ObjectId(personaje_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Id invalido")

    documento = coleccion_personajes.find_one({"_id": oid})
    if not documento:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")

    return documento_a_json(documento)


@app.post("/api/personajes", response_model=PersonajeConId, status_code=201, tags=["Personajes"])
def crear_personaje(personaje: Personaje):
    """Crea un nuevo personaje de anime."""
    resultado = coleccion_personajes.insert_one(personaje.model_dump())
    nuevo = coleccion_personajes.find_one({"_id": resultado.inserted_id})
    return documento_a_json(nuevo)


@app.put("/api/personajes/{personaje_id}", response_model=PersonajeConId, tags=["Personajes"])
def actualizar_personaje(personaje_id: str, personaje: Personaje):
    """Actualiza un personaje existente."""
    try:
        oid = ObjectId(personaje_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Id invalido")

    resultado = coleccion_personajes.find_one_and_update(
        {"_id": oid},
        {"$set": personaje.model_dump()},
        return_document=True,
    )

    if not resultado:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")

    return documento_a_json(resultado)


@app.delete("/api/personajes/{personaje_id}", tags=["Personajes"])
def eliminar_personaje(personaje_id: str):
    """Elimina un personaje por su id."""
    try:
        oid = ObjectId(personaje_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Id invalido")

    resultado = coleccion_personajes.delete_one({"_id": oid})

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")

    return {"mensaje": "Personaje eliminado"}
