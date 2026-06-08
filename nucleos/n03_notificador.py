# nucleos/n03_seguridad.py
import requests

def enviar_alerta(tipo_alerta, mensaje):
    # Número de destino: +58 4144627194
    telefono = "584144627194"
    alerta_formateada = f"⚠️ ALERTA AMITI ({tipo_alerta}): {mensaje}"
    
    # Aquí integrarías tu servicio de API de WhatsApp (ej. Twilio, CallMeBot, etc.)
    # Ejemplo conceptual:
    # requests.post("URL_DE_TU_API_WHATSAPP", json={"to": telefono, "text": alerta_formateada})
    
    print(f"Alerta enviada a {telefono}: {alerta_formateada}")
    return True

def monitorear_agresion(texto):
    if "ataque" in texto or "hackeo" in texto:
        enviar_alerta("SEGURIDAD DIGITAL", texto)
        return "Alerta enviada a tu móvil."
    return "Monitoreo activo."
