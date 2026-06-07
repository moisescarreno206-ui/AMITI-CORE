# Lista global para guardar alertas pendientes (Buzón)
alertas_pendientes = []

def generar_alerta(analisis_previo):
    """
    Núcleo 03: Analizador. 
    Registra la alerta en el buzón y libera el proceso inmediatamente.
    """
    if analisis_previo.get("estado_sistema") == "ALERTA_CRITICA":
        alertas_pendientes.append(analisis_previo)
        print(f"Alerta registrada en buzón: {analisis_previo}")
        return {"status": "registrada"}
    
    return {"status": "ok"}
    
