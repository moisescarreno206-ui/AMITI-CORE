import requests

def enviar_alerta(mensaje):
    telefono = "584144627194"
    apikey = "1062466"  # Tu llave oficial
    
    # URL de CallMeBot para mensajes de texto
    url = f"https://api.callmebot.com/whatsapp.php?phone={telefono}&text={mensaje.replace(' ', '+')}&apikey={apikey}"
    
    try:
        requests.get(url)
        return True
    except Exception:
        return False
