from fastapi import APIRouter
router = APIRouter(prefix="/vehiculos")

@router.get("/")
def estado_vehiculos():
    return {"mensaje": "API de Gestión de Vehículos SISMARL-JAL activa"}