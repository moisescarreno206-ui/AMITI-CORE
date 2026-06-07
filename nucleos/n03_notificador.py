import smtplib
import os
from email.message import EmailMessage

def enviar_email(asunto, cuerpo):
    # AMITI usa las llaves que guardaste en Render
    EMAIL_EMISOR = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
    msg = EmailMessage()
    msg.set_content(cuerpo)
    msg['Subject'] = asunto
    msg['From'] = EMAIL_EMISOR
    msg['To'] = EMAIL_EMISOR 

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_EMISOR, EMAIL_PASSWORD)
        smtp.send_message(msg)
        
