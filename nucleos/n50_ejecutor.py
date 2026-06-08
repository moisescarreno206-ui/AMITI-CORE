# nucleos/n50_ejecutor.py
from nucleos.n46_explorador_externo import analizar_texto
from nucleos.n48_arquitecto_autonomo import procesar_comando_arquitecto
from nucleos.n49_vigilante import vigilar_sistema
from nucleos.n53_autonoma_reparadora import diagnosticar_error

def ejecutar_accion(comando, tipo):
    try:
        if tipo == "analisis":
            return analizar_texto(comando)
        elif tipo == "arquitecto":
            return procesar_comando_arquitecto(comando)
        elif tipo == "vigilancia":
            return vigilar_sistema(comando)
        return "Tipo de acción no reconocido."
    except Exception as e:
        return f"Error detectado: {str(e)}. {diagnosticar_error(str(e))}"
        
