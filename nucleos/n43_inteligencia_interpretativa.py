# nucleos/n43_inteligencia_interpretativa.py

# Importación de todos los núcleos funcionales
from nucleos.n44_calculo_logico import procesar_calculo
from nucleos.n48_arquitecto_autonomo import procesar_comando_arquitecto
from nucleos.n03_notificador import enviar_alerta
from nucleos.n45_memoria import guardar_memoria, leer_memoria
from nucleos.n46_analizador_sentimental import analizar_texto
from nucleos.n49_vigilante import vigilar_sistema

def procesar_comando(cmd):
    comando_limpio = cmd.lower()
    
    # 1. NIVEL DE VIGILANCIA (n49) - Siempre es lo primero
    estado_vigilante = vigilar_sistema(comando_limpio)
    if "ADVERTENCIA" in estado_vigilante:
        enviar_alerta("AMITI detectó un error interno y está en proceso de auto-reparación.")
        return "AMITI: He detectado un problema y estoy trabajando en ello."
    
    # 2. NIVEL DE ANÁLISIS SENTIMENTAL (n46)
    analisis = analizar_texto(comando_limpio)
    if "ALERTA" in analisis:
        enviar_alerta(f"AMITI detectó riesgo: {comando_limpio}")
        return "Alerta de seguridad enviada a tu WhatsApp."

    # 3. NIVEL DE ARQUITECTO (n48)
    if any(p in comando_limpio for p in ["crear", "mejora", "reparar"]):
        return procesar_comando_arquitecto(comando_limpio)

    # 4. NIVEL DE MEMORIA (n45)
    if "recuerda" in comando_limpio:
        guardar_memoria("ultimo_comando", comando_limpio)
        return "Información almacenada en la memoria AMITI."

    # 5. NIVEL DE CÁLCULO (n44)
    if any(op in comando_limpio for op in ["+", "-", "suma"]):
        return procesar_calculo(comando_limpio)
        
    return f"{analisis} | AMITI: Sistema en línea y operando."
    
