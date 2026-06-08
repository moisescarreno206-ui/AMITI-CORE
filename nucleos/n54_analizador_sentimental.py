# nucleos/n54_analizador_sentimental.py

def analizar_sentimiento(texto):
    """
    Núcleo 54: Analiza la intención del usuario.
    """
    # Lógica inicial básica para reconocer comandos
    if "proyecto" in texto.lower():
        return "INICIANDO_PROYECTO"
    return "SENTIMIENTO_NEUTRAL"
