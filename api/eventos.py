from fastapi import APIRouter
router = APIRouter(prefix="/eventos")

@router.get("/")
def estado():
    return {"mensaje": "API Eventos activa"}
