import requests
import time
import threading

# URL de tu servidor (reemplaza con tu URL real de Render)
URL_AMITI = "https://amiti-core.onrender.com"

def mantener_vida():
    print("[05_ACTIVADOR] Iniciando pulso cardiaco...")
    while True:
        try:
            # Hace una petición a sí mismo para mantener el servidor despierto
            requests.get(URL_AMITI)
            print("[05_ACTIVADOR] Pulso enviado. Sistema activo.")
        except Exception as e:
            print(f"[05_ACTIVADOR] Error en el pulso: {e}")
        
        # Espera 5 minutos (300 segundos) antes del siguiente pulso
        time.sleep(300)

def iniciar_activador():
    hilo = threading.Thread(target=mantener_vida, daemon=True)
    hilo.start()
  
