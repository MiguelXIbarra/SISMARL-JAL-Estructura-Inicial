import bcrypt
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "CLAVE_SUPER_SECRETA_JALISCO"
ALGORITHM = "HS256"

def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verificar_password(password: str, hashed: str):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def crear_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(hours=2)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
