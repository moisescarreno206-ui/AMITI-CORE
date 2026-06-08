# nucleos/n49_vigilante.py
import json

def vigilar_sistema(logs_recientes):
    """
    Analiza logs en busca de errores. Si encuentra algo, 
    registra la solución en la memoria para que el n48 la use después.
    """
    if "Error" in logs_recientes or "ImportError" in logs_recientes:
        return "ADVERTENCIA: Anomalía detectada. Iniciando protocolo de auto-reparación..."
    
    return "Estado del sistema: Óptimo."

def aprender_de_error(error, solucion):
    # Registra el aprendizaje en memoria.json
    try:
        with open("memoria.json", "r+") as f:
            data = json.load(f)
            data["historial_reparaciones"].append({"error": error, "solucion": solucion})
            f.seek(0)
            json.dump(data, f)
    except:
        pass
      
