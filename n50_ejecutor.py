# nucleos/n50_ejecutor.py
# Importamos desde los módulos locales en la misma carpeta 'nucleos'
from nucleos.n44_calculo_logico import procesar_calculo
from nucleos.n48_arquitecto_autonomo import procesar_comando_arquitecto
from nucleos.n03_notificador import enviar_alerta
from nucleos.n45_memoria import guardar_memoria, leer_memoria
from nucleos.n46_analizador_sentimental import analizar_texto
from nucleos.n49_vigilante import vigilar_sistema

def ejecutar_accion(comando, tipo):
    if tipo == "calculo":
        return procesar_calculo(comando)
    elif tipo == "arquitecto":
        # Usamos el nombre exacto de la función que tienes en tu n48
        return procesar_comando_arquitecto(comando)
    elif tipo == "seguridad":
        return enviar_alerta(f"Alerta de seguridad: {comando}")
    elif tipo == "memoria":
        return guardar_memoria("ultimo_comando", comando)
    elif tipo == "analisis":
        return analizar_texto(comando)
    elif tipo == "vigilancia":
        return vigilar_sistema(comando)
    return "Acción no reconocida por el Ejecutor Maestro."
