import requests

def enviar_whatsapp(mensaje):
    # Sustituye aquí con tus datos reales
    NUMERO = "+58XXXXXXXXXX" # Tu número con código de país
    APIKEY = "TU_APIKEY_QUE_TE_DIO_CALLMEBOT"
    
    # Esta URL le envía el mensaje directo a tu WhatsApp
    url = f"https://api.callmebot.com/whatsapp.php?phone={NUMERO}&text={mensaje}&apikey={APIKEY}"
    
    try:
        requests.get(url) # AMITI envía el mensaje
        return True
    except Exception as e:
        print(f"Error de conexión: {e}")
        return False

def generar_alerta(analisis_previo):
    if analisis_previo["estado_sistema"] == "ALERTA_CRITICA":
        mensaje = "!!! AMITI: Alerta Critica Detectada !!!"
        enviar_whatsapp(mensaje)
    else:
        mensaje = "AMITI: Estado Normal."
    return {"reporte": mensaje}
    
