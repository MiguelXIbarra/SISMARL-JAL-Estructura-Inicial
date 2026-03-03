from fastapi import APIRouter
router = APIRouter(prefix="/rutas")

@router.get("/")
def estado():
    return {"mensaje": "API Rutas activa"}
