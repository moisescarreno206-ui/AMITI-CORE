from flask import Flask, request, jsonify
from nucleos.n02_cognicion import analizar_seguridad
from nucleos.n03_notificador import generar_alerta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def orquestador():
    if request.method == 'POST':
        datos = request.json
        # 1. Cognición
        analisis = analizar_seguridad(str(datos))
        # 2. Notificación
        resultado_final = generar_alerta(analisis)
        return jsonify(resultado_final)
    
    return jsonify({"nucleo": "01_ORQUESTADOR", "estado": "ACTIVO", "mensaje": "Esperando comandos..."})
    
