# nucleos/n50_ejecutor.py

# IMPORTANTE: Cambiamos la importación del núcleo antiguo al nuevo n54
from nucleos.n54_analizador_sentimental import analizar_sentimiento 

def ejecutar_accion(comando, tipo):
    try:
        if tipo == "analisis":
            return analizar_sentimiento(comando)
        # ... resto de tu lógica
    except Exception as e:
        return f"Error en AMITI: {str(e)}"
        
