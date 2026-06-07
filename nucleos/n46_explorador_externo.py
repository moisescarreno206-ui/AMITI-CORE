# nucleos/n46_explorador_externo.py
from datetime import datetime

def obtener_contexto_externo():
    """Núcleo de exploración: Obtiene datos del entorno."""
    hora = datetime.now().strftime("%H:%M")
    return f"La hora actual del sistema es {hora}."
