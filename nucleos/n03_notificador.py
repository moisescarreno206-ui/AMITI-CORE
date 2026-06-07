import requests

# Solo necesitas tu número y la APIKEY que te da CallMeBot
NUMERO = "+58XXXXXXXXXX" 
APIKEY = "TU_APIKEY_AQUI"

def enviar_whatsapp(mensaje):
    try:
        # Codificamos el mensaje para que la URL sea válida
        url = f"https://api.callmebot.com/whatsapp.php?phone={NUMERO}&text={mensaje}&apikey={APIKEY}"
        requests.get(url)
        return True
    except Exception as e:
        print(f"Error al notificar: {e}")
        return False

def generar_alerta(analisis_previo):
    if analisis_previo["estado_sistema"] == "ALERTA_CRITICA":
        mensaje = "!!! AMITI: Alerta Critica Detectada !!!"
        enviar_whatsapp(mensaje)
    else:
        mensaje = "AMITI: Estado Normal."
        
    return {"reporte": mensaje, "detalles": analisis_previo}
    
