import requests
import os

def enviar_whatsapp(mensaje):
    # Aquí irán tus datos. 
    # TIP: Puedes poner estos valores en las variables de entorno de Render
    # para que nadie más pueda ver tu clave.
    NUMERO = "+58XXXXXXXXXX" # Tu número con código de país (ej: +58412...)
    APIKEY = "TU_APIKEY_QUE_TE_DIO_CALLMEBOT"
    
    # URL de notificación directa
    url = f"https://api.callmebot.com/whatsapp.php?phone={NUMERO}&text={mensaje}&apikey={APIKEY}"
    
    try:
        requests.get(url)
        return True
    except Exception as e:
        print(f"Error al notificar: {e}")
        return False
        
