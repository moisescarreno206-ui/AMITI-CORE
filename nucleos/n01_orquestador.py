from flask import Flask, request, jsonify
# Importamos directamente desde el mismo nivel
from nucleos.n02_cognicion import analizar_seguridad

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def orquestador():
    if request.method == 'POST':
        datos = request.json
        # Analizamos los datos con el nuevo núcleo 02
        resultado = analizar_seguridad(str(datos))
        return jsonify(resultado)
    
    return jsonify({"nucleo": "01_ORQUESTADOR", "estado": "ACTIVO", "mensaje": "Esperando datos de seguridad."})
    
