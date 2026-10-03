from pydantic import BaseModel, Field
from typing import Optional


class Personaje(BaseModel):
    """Personaje de anime almacenado en MongoDB."""

    name: str = Field(..., example="Monkey D. Luffy")
    anime: str = Field(..., example="One Piece")
    role: str = Field(..., example="Capitan")
    power: str = Field(..., example="Fruta Gomu Gomu")
    description: Optional[str] = Field(
        None, example="Capitan de los Piratas de Sombrero de Paja"
    )


class PersonajeConId(Personaje):
    id: str = Field(..., example="651f1b2e9a7c4e6f3d2a1b4c")
