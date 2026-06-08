from nucleos import n44_calculo_logico
from nucleos import n48_arquitecto_autonomo
from nucleos import n03_notificador

def procesar_comando(cmd):
    comando_limpio = cmd.lower()

    # --- 1. MÓDULO DE SEGURIDAD (n03) ---
    if "alerta" in comando_limpio:
        resultado = n03_notificador.enviar_alerta("Prueba de seguridad AMITI activa")
        if resultado:
            return "Alerta enviada a tu WhatsApp, Moisés."
        else:
            return "Error: No pude conectar con el servicio de alertas."

    # --- 2. MÓDULO ARQUITECTO (n48) ---
    if any(palabra in comando_limpio for palabra in ["crear", "mejora", "reparar"]):
        return n48_arquitecto_autonomo.procesar_comando_arquitecto(comando_limpio)

    # --- 3. MÓDULO DE CÁLCULO (n44) ---
    # Detecta si el usuario está pidiendo una operación matemática
    if any(operador in comando_limpio for operador in ["+", "-", "suma", "resta"]):
        return n44_calculo_logico.procesar_calculo(comando_limpio)

    # --- 4. RESPUESTA POR DEFECTO ---
    return "AMITI: Procesando información con acceso total a memoria y contexto externo."
    
