from flask import Flask, render_template, request
import importlib
import pkgutil
import nucleos
import os

app = Flask(__name__)

# --- RUTA DE INTERFAZ (Tu Chat Neón) ---
@app.route('/')
def home():
    # Aseguramos que busque en la carpeta correcta 'templates'
    return render_template('index.html')

# --- DETECTOR AUTOMÁTICO DE NÚCLEOS (Tu mejora infinita) ---
def obtener_nucleos_disponibles():
    return [name for _, name, _ in pkgutil.iter_modules(nucleos.__path__) if name.startswith('n')]

# --- PROCESAMIENTO INTELIGENTE (Cerebro n43) ---
@app.route('/procesar')
def procesar():
    comando = request.args.get('comando', '').lower()
    try:
        n43 = importlib.import_module("nucleos.n43_inteligencia_interpretativa")
        return {"respuesta": n43.procesar_comando(comando)}
    except Exception as e:
        return {"respuesta": f"Sistema activo, pero hubo un error: {str(e)}"}

# --- COMPATIBILIDAD VIEJA (Ejecución directa) ---
@app.route('/ejecutar/<nombre_modulo>/<nombre_funcion>')
def ejecutar(nombre_modulo, nombre_funcion):
    if nombre_modulo not in obtener_nucleos_disponibles():
        return {"estado": "error", "detalle": "Núcleo no detectado"}
    try:
        modulo = importlib.import_module(f"nucleos.{nombre_modulo}")
        funcion = getattr(modulo, nombre_funcion)
        return {"resultado": funcion()}
    except Exception as e:
        return {"resultado": "error", "detalle": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
