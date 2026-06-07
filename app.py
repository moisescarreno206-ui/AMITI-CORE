import os
import importlib
from flask import Flask, jsonify

app = Flask(__name__)

# Lista de tus núcleos (aquí los irás agregando poco a poco hasta llegar a 35)
NUCLEOS_REGISTRADOS = ['n03_notificador'] 

def ejecutar_nucleo(nombre, funcion, *args):
    """Carga dinámicamente cualquier núcleo y ejecuta su función."""
    modulo = importlib.import_module(f"nucleos.{nombre}")
    func = getattr(modulo, funcion)
    return func(*args)

@app.route('/')
def home():
    return "AMITI-CORE: Sistema de 35 núcleos en preparación."

@app.route('/ejecutar/<nombre_nucleo>/<nombre_funcion>')
def ejecutar(nombre_nucleo, nombre_funcion):
    try:
        resultado = ejecutar_nucleo(nombre_nucleo, nombre_funcion)
        return jsonify({"estado": "exito", "data": resultado})
    except Exception as e:
        return jsonify({"estado": "error", "mensaje": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
