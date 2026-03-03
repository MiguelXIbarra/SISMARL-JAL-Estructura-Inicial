from fastapi import APIRouter
router = APIRouter(prefix="/usuarios")

@router.get("/")
def estado():
    return {"mensaje": "API Usuarios activa"}
