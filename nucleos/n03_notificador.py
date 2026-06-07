import requests
import os

def enviar_whatsapp(mensaje):
    # Asegúrate de poner tu número con el formato correcto: +58412xxxxxxx
    NUMERO = "+58XXXXXXXXXX" 
    APIKEY = "TU_APIKEY_AQUI"
    
    url = f"https://api.callmebot.com/whatsapp.php?phone={NUMERO}&text={mensaje}&apikey={APIKEY}"
    
    try:
        respuesta = requests.get(url)
        print(f"Respuesta del bot: {respuesta.status_code}") # Esto aparecerá en los logs de Render
        return respuesta.status_code == 200
    except Exception as e:
        print(f"Error de conexión: {e}")
        return False
