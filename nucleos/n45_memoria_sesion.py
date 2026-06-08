import json

def guardar_memoria(clave, valor):
    try:
        with open("memoria.json", "r+") as f:
            data = json.load(f)
            data[clave] = valor
            f.seek(0)
            json.dump(data, f)
        return "Dato guardado."
    except:
        return "Error en persistencia."

def leer_memoria(clave):
    with open("memoria.json", "r") as f:
        data = json.load(f)
        return data.get(clave, "No tengo registro de eso.")
