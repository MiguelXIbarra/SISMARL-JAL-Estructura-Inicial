from sqlalchemy import Column, Integer, String, Float
from base_datos.conexion import Base

class Ruta(Base):
    __tablename__ = "rutas"
    id = Column(Integer, primary_key=True)
    origen = Column(String(150))
    destino = Column(String(150))
    distancia_km = Column(Float)
    riesgo_estimado = Column(String(20))
