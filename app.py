from flask import Flask, render_template, request
import importlib
import pkgutil
import nucleos

app = Flask(__name__)

# --- 1. RUTA DE INTERFAZ (Tu chat Neón) ---
@app.route('/')
def home():
    return render_template('index.html')

# --- 2. RUTA DE PROCESAMIENTO (El puente al Cerebro n43) ---
@app.route('/procesar')
def procesar():
    comando = request.args.get('comando', '')
    try:
        # Llama al nuevo núcleo de inteligencia
        n43 = importlib.import_module("nucleos.n43_inteligencia_interpretativa")
        respuesta = n43.procesar_comando(comando)
        return {"respuesta": respuesta}
    except Exception as e:
        return {"respuesta": f"Error de núcleo: {str(e)}"}

# --- 3. TU ORQUESTADOR VIEJO (Funcionalidad intacta) ---
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
    
