# nucleos/n45_memoria.py
import json
import os

# Definimos la ruta de la memoria de forma absoluta
MEMORIA_FILE = "memoria.json"

def guardar_memoria(clave, valor):
    try:
        datos = {}
        if os.path.exists(MEMORIA_FILE):
            with open(MEMORIA_FILE, "r") as f:
                datos = json.load(f)
        
        datos[clave] = valor
        
        with open(MEMORIA_FILE, "w") as f:
            json.dump(datos, f)
        return True
    except Exception as e:
        return f"Error en memoria: {str(e)}"

def leer_memoria(clave):
    if not os.path.exists(MEMORIA_FILE):
        return None
    with open(MEMORIA_FILE, "r") as f:
        datos = json.load(f)
        return datos.get(clave)
        
