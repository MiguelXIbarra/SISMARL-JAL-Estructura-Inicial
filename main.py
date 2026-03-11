from fastapi import FastAPI
from api import usuarios, rutas_logisticas, eventos, vehiculos
from base_datos.conexion import Base, engine
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SISMARL-JAL")

app.include_router(usuarios.router)
app.include_router(rutas_logisticas.router)
app.include_router(eventos.router)
app.include_router(vehiculos.router)

@app.get("/")
def root():
    return {"mensaje": "Sistema SISMARL-JAL operativo"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=7000, reload=True)
