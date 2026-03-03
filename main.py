from fastapi import FastAPI
<<<<<<< HEAD
from api import usuarios, rutas_logisticas, eventos
from base_datos.conexion import Base, engine

=======
from api import usuarios, rutas_logisticas, eventos, vehiculos
from base_datos.conexion import Base, engine


>>>>>>> Bugs
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SISMARL-JAL")

app.include_router(usuarios.router)
app.include_router(rutas_logisticas.router)
app.include_router(eventos.router)
<<<<<<< HEAD
=======
app.include_router(vehiculos.router)
>>>>>>> Bugs

@app.get("/")
def root():
    return {"mensaje": "Sistema SISMARL-JAL operativo"}
