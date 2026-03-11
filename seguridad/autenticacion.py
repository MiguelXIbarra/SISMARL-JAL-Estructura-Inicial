import os
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

# Configuración centralizada desde .env
SECRET_KEY = os.getenv("CLAVE_SECRETA")
ALGORITHM = os.getenv("ALGORITMO", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("MINUTOS_EXPIRACION", 30))

# Configuración de hashing con Passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def obtener_password_hash(password: str):
    """Genera un hash seguro para la base de datos"""
    return pwd_context.hash(password)

def verificar_password(plain_password: str, hashed_password: str):
    """Compara la contraseña ingresada con el hash guardado"""
    return pwd_context.verify(plain_password, hashed_password)

def crear_token_acceso(data: dict):
    """Crea el token JWT para la sesión"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)