from flask import Flask, render_template, request
import importlib
import pkgutil
import nucleos

app = Flask(__name__)

# --- 1. RUTA DE INTERFAZ ---
@app.route('/')
def home():
    return render_template('index.html')

# --- 2. ORQUESTADOR DINÁMICO (Detecta automáticamente nuevos núcleos) ---
def obtener_nucleos_disponibles():
    # Esta línea escanea la carpeta 'nucleos' cada vez que el sistema se inicia
    return [name for _, name, _ in pkgutil.iter_modules(nucleos.__path__) if name.startswith('n')]

# --- 3. RUTA DE PROCESAMIENTO (Cerebro n43 + Memoria + Exploración) ---
@app.route('/procesar')
def procesar():
    comando = request.args.get('comando', '').lower()
    try:
        # El n43 actúa como director de orquesta
        n43 = importlib.import_module("nucleos.n43_inteligencia_interpretativa")
        respuesta = n43.procesar_comando(comando)
        return {"respuesta": respuesta}
    except Exception as e:
        return {"respuesta": f"Error de núcleo: {str(e)}"}

# --- 4. RUTA DE EJECUCIÓN (Compatibilidad con el sistema viejo) ---
@app.route('/ejecutar/<nombre_modulo>/<nombre_funcion>')
def ejecutar(nombre_modulo, nombre_funcion):
    if nombre_modulo not in obtener_nucleos_disponibles():
        return {"estado": "error", "detalle": "Núcleo no encontrado en la base de datos"}
    try:
        modulo = importlib.import_module(f"nucleos.{nombre_modulo}")
        funcion = getattr(modulo, nombre_funcion)
        return {"resultado": funcion()}
    except Exception as e:
        return {"estado": "error", "detalle": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
