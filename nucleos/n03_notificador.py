import smtplib
import os
from email.message import EmailMessage

def generar_alerta(analisis_previo):
    """
    Núcleo 03: Analizador y Notificador.
    Recibe el análisis, evalúa la gravedad y notifica si es necesario.
    """
    EMAIL_EMISOR = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
    # Análisis mejorado: categorizamos la alerta
    gravedad = analisis_previo.get("estado_sistema", "DESCONOCIDO")
    detalles = analisis_previo.get("detalles", "Sin detalles adicionales")
    
    if gravedad == "ALERTA_CRITICA":
        asunto = "!!! AMITI: ALERTA DE SEGURIDAD CRÍTICA !!!"
        cuerpo = (f"AMITI ha detectado un evento crítico.\n\n"
                  f"Estado: {gravedad}\n"
                  f"Detalle técnico: {detalles}\n"
                  f"Timestamp: Sistema operativo en la nube.")
        
        try:
            msg = EmailMessage()
            msg.set_content(cuerpo)
            msg['Subject'] = asunto
            msg['From'] = EMAIL_EMISOR
            msg['To'] = EMAIL_EMISOR 

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_EMISOR, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print("Notificación crítica enviada con éxito.")
            return {"status": "enviado", "gravedad": gravedad}
        except Exception as e:
            print(f"Error crítico enviando correo: {e}")
            return {"status": "error", "error": str(e)}
            
    return {"status": "ignorado", "razon": "No es una alerta crítica"}

def probar_correo():
    """Función de prueba para verificar conectividad."""
    prueba = {
        "estado_sistema": "ALERTA_CRITICA", 
        "detalles": "Prueba de diagnóstico de conectividad SMTP iniciada por el usuario."
    }
    return generar_alerta(prueba)
    
