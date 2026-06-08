# nucleos/n50_ejecutor.py
from nucleos.n46_explorador_externo import analizar_texto
from nucleos.n53_autonoma_reparadora import reparar_entorno

def ejecutar_accion(comando, tipo):
    try:
        if tipo == "analisis":
            return analizar_texto(comando)
        return f"Accion {tipo} en proceso."
    except ImportError as e:
        # Aquí el N53 toma el control total cuando falla una importación
        return f"Error crítico de red/modulo: {str(e)}. {reparar_entorno()}"

print("AMITI: Núcleos cargados. Esperando comandos.")
