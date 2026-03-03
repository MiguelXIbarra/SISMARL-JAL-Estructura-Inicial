from sqlalchemy import Column, Integer, String, Boolean
from base_datos.conexion import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    correo = Column(String(150), unique=True)
    password_hash = Column(String(255))
    rol_id = Column(Integer)
    intentos_fallidos = Column(Integer, default=0)
    bloqueado = Column(Boolean, default=False)
