from sqlalchemy import Column, Integer, String, Text
from base_datos.conexion import Base

class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True)
    vehiculo_id = Column(Integer)
    ruta_id = Column(Integer)
    tipo_evento = Column(String(50))
    descripcion = Column(Text)
