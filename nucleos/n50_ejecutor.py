# nucleos/n50_ejecutor.py
from nucleos.n44_calculo_logico import procesar_calculo
from nucleos.n48_arquitecto_autonomo import procesar_comando_arquitecto
from nucleos.n03_notificador import enviar_alerta
from nucleos.n45_memoria import guardar_memoria
from nucleos.n46_analizador_sentimental import analizar_texto
from nucleos.n49_vigilante import vigilar_sistema

def ejecutar_accion(comando, tipo):
    if tipo == "calculo":
        return procesar_calculo(comando)
    elif tipo == "arquitecto":
        return procesar_comando_arquitecto(comando)
    elif tipo == "seguridad":
        return enviar_alerta(comando)
    return "Acción no definida."
  
