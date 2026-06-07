# nucleos/n45_memoria_sesion.py
# Usaremos una lista global simple para memoria de sesión
memoria_temporal = []

def guardar_recuerdo(mensaje):
    memoria_temporal.append(mensaje)
    return f"Recuerdo registrado: {mensaje}"

def obtener_recuerdos():
    return " | ".join(memoria_temporal[-3:]) # Te devuelve los últimos 3 mensajes
