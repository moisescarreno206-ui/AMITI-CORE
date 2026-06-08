# nucleos/n50_ejecutor.py
from nucleos.n46_explorador_externo import analizar_texto

def ejecutar_accion(comando, tipo):
    # Enrutamiento centralizado
    if tipo == "analisis":
        return analizar_texto(comando)
    
    return f"Sistema ejecutando {tipo}: {comando}"

# Esta impresión aparecerá en los logs de Render
print("AMITI: Núcleo 50 y Núcleo 46 conectados correctamente.")
