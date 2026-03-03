from fastapi import FastAPI
from api import usuarios, rutas_logisticas, eventos
from base_datos.conexion import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SISMARL-JAL")

app.include_router(usuarios.router)
app.include_router(rutas_logisticas.router)
app.include_router(eventos.router)

@app.get("/")
def root():
    return {"mensaje": "Sistema SISMARL-JAL operativo"}
