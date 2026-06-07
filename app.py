import importlib
import pkgutil
import nucleos  # Importa el paquete donde están tus núcleos
from flask import Flask, jsonify

app = Flask(__name__)

def obtener_nucleos_disponibles():
    """Escanea la carpeta 'nucleos' y devuelve una lista de módulos encontrados."""
    modulos = []
    # Busca en el paquete 'nucleos' todos los archivos que contengan código
    for _, name, _ in pkgutil.iter_modules(nucleos.__path__):
        if name.startswith('n'):  # Solo carga los que siguen tu convención 'nXX...'
            modulos.append(name)
    return modulos

@app.route('/ejecutar/<nombre_modulo>/<nombre_funcion>')
def ejecutar(nombre_modulo, nombre_funcion):
    modulos_activos = obtener_nucleos_disponibles()
    
    if nombre_modulo not in modulos_activos:
        return jsonify({"estado": "error", "detalle": f"Núcleo {nombre_modulo} no encontrado o no activo"})

    try:
        # Carga dinámica: detecta el archivo sin tenerlo en una lista fija
        modulo = importlib.import_module(f"nucleos.{nombre_modulo}")
        funcion = getattr(modulo, nombre_funcion)
        resultado = funcion()
        return jsonify({"modulo": nombre_modulo, "resultado": resultado})
    except Exception as e:
        return jsonify({"estado": "error", "detalle": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
