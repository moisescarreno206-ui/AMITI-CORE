from nucleos import n44_calculo_logico
from nucleos import n48_arquitecto_autonomo
from nucleos import n03_notificador
from nucleos import n45_memoria
from nucleos import n46_analizador_sentimental

def procesar_comando(cmd):
    # 1. Análisis de Sentimiento (Siempre activo)
    analisis = n46_analizador_sentimental.analizar_texto(cmd)
    
    # 2. Si detecta peligro, alerta prioritaria
    if "ALERTA" in analisis:
        n03_notificador.enviar_alerta(f"AMITI detectó riesgo: {cmd}")
        return "He detectado una amenaza y he notificado a tu WhatsApp."

    # 3. Memoria (Si quieres guardar algo)
    if "recuerda" in cmd:
        n45_memoria.guardar_memoria("ultimo_comando", cmd)
        return "Información almacenada en memoria de largo plazo."

    # 4. Cálculo y Arquitectura
    if any(op in cmd for op in ["+", "-", "suma"]):
        return n44_calculo_logico.procesar_calculo(cmd)
        
    return f"{analisis} AMITI: Sistema operando correctamente."
    
