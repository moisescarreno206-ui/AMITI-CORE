# nucleos/n46_analizador_sentimental.py

def analizar_texto(texto):
    texto = texto.lower()
    # Detectar agresividad o peligro
    palabras_peligro = ["amenaza", "agresión", "hackeo", "insulto"]
    if any(p in texto for p in palabras_peligro):
        return "ALERTA: He detectado lenguaje agresivo."
    
    # Análisis de humor
    if "feliz" in texto or "bien" in texto:
        return "AMITI: Detecto un estado de ánimo positivo."
        
    return "Análisis: Tono neutral."
    
