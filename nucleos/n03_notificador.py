import smtplib
from email.message import EmailMessage

def enviar_email(asunto, cuerpo):
    # Tus datos de Gmail
    EMAIL_EMISOR = "tu_correo@gmail.com"
    EMAIL_PASSWORD = "TU_CONTRASEÑA_DE_APLICACION" # La de 16 caracteres
    EMAIL_RECEPTOR = "tu_correo@gmail.com"

    msg = EmailMessage()
    msg.set_content(cuerpo)
    msg['Subject'] = asunto
    msg['From'] = EMAIL_EMISOR
    msg['To'] = EMAIL_RECEPTOR

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_EMISOR, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return True
    except Exception as e:
        print(f"Error enviando correo: {e}")
        return False

def generar_alerta(analisis_previo):
    if analisis_previo["estado_sistema"] == "ALERTA_CRITICA":
        asunto = "!!! AMITI: ALERTA CRÍTICA !!!"
        cuerpo = f"Atención: El sistema ha detectado una anomalía.\nDetalles: {analisis_previo}"
        enviar_email(asunto, cuerpo)
    else:
        asunto = "AMITI: Estado Normal"
        cuerpo = "El sistema está funcionando correctamente."
        # Solo enviamos correo si hay alerta para no llenar tu bandeja
    
    return {"reporte": asunto, "detalles": analisis_previo}
