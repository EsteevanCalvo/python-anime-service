"""
Inserta 10 personajes de anime de ejemplo en MongoDB.
Uso: python seed.py   (necesita el archivo .env ya configurado)
"""
from database import coleccion_personajes

personajes = [
    {"name": "Monkey D. Luffy", "anime": "One Piece", "role": "Capitan", "power": "Fruta Gomu Gomu", "description": "Capitan de los Piratas de Sombrero de Paja"},
    {"name": "Roronoa Zoro", "anime": "One Piece", "role": "Espadachin", "power": "Estilo de tres espadas", "description": "Primer tripulante en unirse a Luffy"},
    {"name": "Nami", "anime": "One Piece", "role": "Navegante", "power": "Clima Tact", "description": "Experta en cartografia y el clima"},
    {"name": "Sanji", "anime": "One Piece", "role": "Cocinero", "power": "Black Leg Style", "description": "Pelea solo con las piernas para no danar sus manos"},
    {"name": "Tony Tony Chopper", "anime": "One Piece", "role": "Medico", "power": "Fruta Hito Hito", "description": "Reno que gano inteligencia y forma humana"},
    {"name": "Nico Robin", "anime": "One Piece", "role": "Arqueologa", "power": "Fruta Hana Hana", "description": "Puede hacer florecer partes de su cuerpo en cualquier superficie"},
    {"name": "Edward Newgate", "anime": "One Piece", "role": "Emperador", "power": "Fruta Gura Gura", "description": "Conocido como Barbablanca, el hombre mas fuerte del mundo"},
    {"name": "Itachi Uchiha", "anime": "Naruto", "role": "Ninja renegado", "power": "Mangekyo Sharingan", "description": "Hermano mayor de Sasuke Uchiha"},
    {"name": "Levi Ackerman", "anime": "Attack on Titan", "role": "Capitan", "power": "Combate con equipo de maniobras 3D", "description": "El soldado mas fuerte de la humanidad"},
    {"name": "Izuku Midoriya", "anime": "My Hero Academia", "role": "Estudiante heroe", "power": "One For All", "description": "Protagonista que hereda el poder de All Might"},
]

resultado = coleccion_personajes.delete_many({})
print(f"Documentos anteriores eliminados: {resultado.deleted_count}")

resultado = coleccion_personajes.insert_many(personajes)
print(f"Listo: se insertaron {len(resultado.inserted_ids)} personajes.")
