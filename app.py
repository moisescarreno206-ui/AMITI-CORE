import os
import traceback
from flask import Flask
from nucleos.n03_notificador import probar_correo

app = Flask(__name__)

@app.route('/')
def home():
    return "AMITI-CORE está operando correctamente."

@app.route('/test-email')
def test_email():
    try:
        # Intentamos ejecutar la función
        resultado = probar_correo()
        return f"Resultado exitoso: {resultado}"
    except Exception:
        # Si falla, nos muestra el error técnico aquí mismo
        return f"ERROR DETECTADO: {traceback.format_exc()}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
