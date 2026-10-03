import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError(
        "Falta la variable de entorno MONGO_URI. Revisa tu archivo .env (ver .env.example)."
    )

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=8000)
db = client["anime_db"]
coleccion_personajes = db["personajes"]
