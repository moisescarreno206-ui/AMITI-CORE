# Archivo: n42_presencia_autoridad.py

def verificar_creador(frase):
    """
    Núcleo 42: Reconocimiento de Autoridad.
    Escucha la frase de activación del creador y responde activando la presencia.
    """
    frase_clave = "amiti llegó tu creador"
    
    if frase.lower() == frase_clave:
        return {
            "status": "presencia_activa",
            "modulo": "Presencia Autoridad",
            "mensaje": "¡Saludos, Moisés! Reconocimiento de autoridad confirmado. Todos los sistemas (42 núcleos) están a tu entera disposición. ¿Qué orden deseas ejecutar?",
            "codigo_activacion": "AMITI-ACTIVE-AUTH-001"
        }
    else:
        return {
            "status": "espera",
            "modulo": "Presencia Autoridad",
            "mensaje": "Protocolo de autenticación no activado."
        }
      
