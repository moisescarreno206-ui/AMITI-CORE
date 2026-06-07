from flask import Flask, render_template  # <--- Asegúrate de importar render_template
import importlib
import pkgutil
import nucleos

app = Flask(__name__)

# --- NUEVA RUTA PARA TU DISEÑO NEÓN ---
@app.route('/')
def home():
    return render_template('index.html') # Esto buscará el archivo en /templates/
# --------------------------------------

def obtener_nucleos_disponibles():
    modulos = []
    for _, name, _ in pkgutil.iter_modules(nucleos.__path__):
        if name.startswith('n'):
            modulos.append(name)
    return modulos

@app.route('/ejecutar/<nombre_modulo>/<nombre_funcion>')
def ejecutar(nombre_modulo, nombre_funcion):
    modulos_activos = obtener_nucleos_disponibles()
    if nombre_modulo not in modulos_activos:
        return {"estado": "error", "detalle": "Núcleo no encontrado"}
    try:
        modulo = importlib.import_module(f"nucleos.{nombre_modulo}")
        funcion = getattr(modulo, nombre_funcion)
        return {"resultado": funcion()}
    except Exception as e:
        return {"estado": "error", "detalle": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
