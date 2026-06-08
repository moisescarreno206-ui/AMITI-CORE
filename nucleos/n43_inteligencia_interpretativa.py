# nucleos/n43_inteligencia_interpretativa.py

# Importación directa desde los archivos individuales
from nucleos.n44_calculo_logico import procesar_calculo
from nucleos.n48_arquitecto_autonomo import procesar_comando_arquitecto
from nucleos.n03_notificador import enviar_alerta
from nucleos.n45_memoria import guardar_memoria, leer_memoria
from nucleos.n46_analizador_sentimental import analizar_texto

def procesar_comando(cmd):
    comando_limpio = cmd.lower()
    
    # Análisis de sentimiento constante
    analisis = analizar_texto(comando_limpio)
    
    # 1. Seguridad (Prioridad alta)
    if "alerta" in comando_limpio or "ALERTA" in analisis:
        enviar_alerta(f"AMITI detectó riesgo: {comando_limpio}")
        return "Alerta de seguridad enviada a tu WhatsApp."

    # 2. Arquitecto
    if any(p in comando_limpio for p in ["crear", "mejora", "reparar"]):
        return procesar_comando_arquitecto(comando_limpio)

    # 3. Memoria
    if "recuerda" in comando_limpio:
        guardar_memoria("ultimo_comando", comando_limpio)
        return "Información almacenada en la memoria AMITI."

    # 4. Cálculo
    if any(op in comando_limpio for op in ["+", "-", "suma"]):
        return procesar_calculo(comando_limpio)
        
    return f"{analisis} | AMITI: Esperando instrucción."
    
