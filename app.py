import os
from flask import Flask, jsonify
from nucleos.n03_notificador import generar_alerta, alertas_pendientes

app = Flask(__name__)

@app.route('/')
def home():
    return "AMITI-CORE: Sistema operativo y núcleo 03 activos."

@app.route('/test-alerta')
def test_alerta():
    """Ruta para simular una alerta crítica y ver si se registra."""
    alerta_falsa = {"estado_sistema": "ALERTA_CRITICA", "detalles": "Prueba de buzón exitosa"}
    resultado = generar_alerta(alerta_falsa)
    return jsonify({"resultado": resultado, "alertas_en_buzon": len(alertas_pendientes)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
