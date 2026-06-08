import os

def procesar_mejora(comando):
    """
    Este núcleo analiza comandos de creación o reparación.
    """
    if "crear" in comando:
        return "Modo Arquitecto: Por favor, especifica el nombre del nuevo núcleo y su función."
    
    if "reparar" in comando:
        return "Modo Reparador: Analizando logs en busca de fallos en la estructura..."
    
    return "Arquitecto Activo. Estoy lista para reescribir mis propios núcleos bajo tu comando."

def auto_evolucionar(nombre_nucleo, codigo_nuevo):
    """
    Acción de alto nivel: AMITI escribe su propio código.
    """
    try:
        ruta = f"nucleos/{nombre_nucleo}.py"
        with open(ruta, "w") as f:
            f.write(codigo_nuevo)
        return f"Éxito: El núcleo {nombre_nucleo} ha sido creado/actualizado exitosamente."
    except Exception as e:
        return f"Error en evolución: {str(e)}"
