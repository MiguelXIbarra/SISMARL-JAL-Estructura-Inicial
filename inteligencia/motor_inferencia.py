def evaluar_evento(tipo_evento):
    reglas = {
        "DESVIACION": "ALERTA: Posible riesgo detectado",
        "INICIO_RUTA": "Evento normal",
        "FINALIZACION": "Ruta completada correctamente"
    }
    return reglas.get(tipo_evento, "Evento no clasificado")
