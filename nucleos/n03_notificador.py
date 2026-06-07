import requests

def enviar_whatsapp(mensaje):
    # Reemplaza con tu número y tu APIKEY
    NUMERO = "+58XXXXXXXXXX" 
    APIKEY = "TU_APIKEY_AQUI"
    
    # Esta URL dispara el mensaje a tu WhatsApp directamente
    url = f"https://api.callmebot.com/whatsapp.php?phone={NUMERO}&text={mensaje}&apikey={APIKEY}"
    
    try:
        requests.get(url) # AMITI "llama" a la puerta de WhatsApp
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def generar_alerta(analisis_previo):
    if analisis_previo["estado_sistema"] == "ALERTA_CRITICA":
        mensaje = "!!! AMITI: Alerta Critica Detectada !!!"
        enviar_whatsapp(mensaje) # Aquí es donde AMITI te habla
    else:
        mensaje = "AMITI: Estado Normal."
    return {"reporte": mensaje}
    
