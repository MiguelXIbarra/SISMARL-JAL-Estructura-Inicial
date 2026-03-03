"""
Archivo: principal.py
Punto de entrada del sistema.
"""

from fastapi import FastAPI
from .base_datos import motor
from .modelos import Base

app = FastAPI()

Base.metadata.create_all(bind=motor)

@app.get("/")
def inicio():
    return {"mensaje": "Sistema SISMARL-JAL funcionando correctamente"}
