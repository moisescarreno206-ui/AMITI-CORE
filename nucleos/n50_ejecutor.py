# nucleos/n50_ejecutor.py
from nucleos.n44_calculo_logico import procesar_calculo
from nucleos.n48_arquitecto_autonomo import procesar_comando_arquitecto
from nucleos.n03_notificador import enviar_alerta
from nucleos.n45_memoria import guardar_memoria, leer_memoria
from nucleos.n46_explorador_externo import analizar_texto
from nucleos.n49_vigilante import vigilar_sistema
from nucleos.n52_dominio_de_red import exponer_dominio  # <--- NUEVO

def ejecutar_accion(comando, tipo):
    if tipo == "calculo":
        return procesar_calculo(comando)
    elif tipo == "arquitecto":
        return procesar_comando_arquitecto(comando)
    elif tipo == "red": # <--- NUEVA CONDICION
        return exponer_dominio(comando)
    # ... resto de tus condiciones
    return "Accion no definida"
  
