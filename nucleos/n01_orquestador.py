from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "nucleo": "01_ORQUESTADOR",
        "estado": "ACTIVO",
        "mensaje": "AMITI esta en linea y esperando conexiones."
    })

if __name__ == "__main__":
    app.run()
  
