# nucleos/n50_ejecutor.py
from nucleos.n46_explorador_externo import analizar_texto

def ejecutar_accion(comando, tipo):
    # Lógica de enrutamiento
    if tipo == "analisis":
        return analizar_texto(comando)
    
    return f"Sistema ejecutando {tipo}: {comando}"

print("Núcleo 50 y Núcleo 46 cargados exitosamente.")
