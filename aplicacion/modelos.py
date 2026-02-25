"""
Archivo: modelos.py
Define las tablas del sistema.
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Numeric, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base_datos import Base

class Rol(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(Text, nullable=False)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    intentos_fallidos = Column(Integer, default=0)
    bloqueado = Column(Boolean, default=False)
    bloqueado_hasta = Column(DateTime, nullable=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    rol = relationship("Rol")
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

class Vehiculo(Base):
    __tablename__ = "vehiculos"
    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(20), unique=True, nullable=False)
    modelo = Column(String(100), nullable=False)
    capacidad_kg = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True)
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())

class Ruta(Base):
    __tablename__ = "rutas"
    id = Column(Integer, primary_key=True, index=True)
    origen = Column(String(150), nullable=False)
    destino = Column(String(150), nullable=False)
    distancia_km = Column(Numeric(6, 2), nullable=False)
    riesgo_estimado = Column(String(20))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))
    ruta_id = Column(Integer, ForeignKey("rutas.id"))
    tipo_evento = Column(String(50), nullable=False)
    descripcion = Column(Text)
    fecha_evento = Column(DateTime(timezone=True), server_default=func.now())

class LogSeguridad(Base):
    __tablename__ = "logs_seguridad"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    accion = Column(String(100), nullable=False)
    ip_origen = Column(String(45))
    descripcion = Column(Text)
    fecha = Column(DateTime(timezone=True), server_default=func.now())