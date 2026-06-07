from flask import Flask, render_template, request
import importlib
import pkgutil
import nucleos

app = Flask(__name__)

# --- 1. RUTA DE INTERFAZ (Tu chat Neón) ---
@app.route('/')
def home():
    return render_template('index.html')

# --- 2. ORQUESTADOR DINÁMICO (Sin límites: detecta todo automáticamente) ---
def obtener_nucleos_disponibles():
    # Escanea la carpeta 'nucleos' en tiempo real
    return [name for _, name, _ in pkgutil.iter_modules(nucleos.__path__) if name.startswith('n')]

# --- 3. RUTA DE PROCESAMIENTO ---
@app.route('/procesar')
def procesar():
    comando = request.args.get('comando', '').lower()
    
    # Intenta usar el n43 para interpretar
    try:
        n43 = importlib.import_module("nucleos.n43_inteligencia_interpretativa")
        respuesta = n43.procesar_comando(comando)
        return {"respuesta": respuesta}
    except Exception as e:
        return {"respuesta": f"Cerebro no detectado: {str(e)}"}

# --- 4. RUTA DE EJECUCIÓN DIRECTA (Compatible con tus 44+ núcleos) ---
@app.route('/ejecutar/<nombre_modulo>/<nombre_funcion>')
def ejecutar(nombre_modulo, nombre_funcion):
    if nombre_modulo not in obtener_nucleos_disponibles():
        return {"estado": "error", "detalle": "Núcleo no existe en el sistema"}
    try:
        modulo = importlib.import_module(f"nucleos.{nombre_modulo}")
        funcion = getattr(modulo, nombre_funcion)
        return {"resultado": funcion()}
    except Exception as e:
        return {"estado": "error", "detalle": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
