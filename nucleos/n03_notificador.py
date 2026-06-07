import smtplib
import os
from email.message import EmailMessage

def generar_alerta(analisis_previo):
    """
    Esta es la función que tu sistema busca. 
    Asegúrate de que se llame exactamente así.
    """
    # 1. Configuración de credenciales seguras
    EMAIL_EMISOR = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
    # 2. Solo enviamos correo si hay ALERTA_CRITICA
    if analisis_previo.get("estado_sistema") == "ALERTA_CRITICA":
        asunto = "!!! AMITI: ALERTA CRÍTICA DETECTADA !!!"
        cuerpo = f"Atención: El sistema ha detectado una anomalía.\n\nDetalles: {analisis_previo}"
        
        msg = EmailMessage()
        msg.set_content(cuerpo)
        msg['Subject'] = asunto
        msg['From'] = EMAIL_EMISOR
        msg['To'] = EMAIL_EMISOR 

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_EMISOR, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print("Correo de alerta enviado con éxito.")
        except Exception as e:
            print(f"Error enviando correo: {e}")
    
    return {"reporte": "Procesado", "detalles": analisis_previo}
    
# Esta función es solo para probar que el correo llega
def probar_correo():
    mensaje_prueba = {"estado_sistema": "ALERTA_CRITICA", "info": "Esta es una prueba de AMITI"}
    return generar_alerta(mensaje_prueba)
    
