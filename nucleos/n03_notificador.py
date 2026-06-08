from twilio.rest import Client

# Tus credenciales de Twilio
ACCOUNT_SID = 'TU_ACCOUNT_SID'
AUTH_TOKEN = 'TU_AUTH_TOKEN'
TWILIO_NUMBER = 'whatsapp:+14155238886' # El número de sandbox de Twilio
MI_NUMERO = 'whatsapp:+58XXXXXXXXXX' # Tu número de WhatsApp

def enviar_whatsapp(mensaje):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=mensaje,
            from_=TWILIO_NUMBER,
            to=MI_NUMERO
        )
        return True
    except Exception as e:
        print(f"Error enviando WhatsApp: {e}")
        return False

def generar_alerta(analisis_previo):
    if analisis_previo["estado_sistema"] == "ALERTA_CRITICA":
        texto = "!!! AMITI: Alerta Crítica Detectada !!!"
        enviar_whatsapp(texto)
    else:
        texto = "AMITI: Estado del sistema normal."
        
    return {"reporte": texto, "detalles": analisis_previo}
    
