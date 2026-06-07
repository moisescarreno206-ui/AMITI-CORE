from flask import Flask
# ... otros imports que ya tengas ...

app = Flask(__name__)

# Tu ruta principal actual
@app.route('/')
def home():
    return "AMITI está activa."

# AGREGA AQUÍ TU NUEVA RUTA DE PRUEBA
@app.route('/test-email')
def test_email():
    from nucleos.n03_notificador import probar_correo
    probar_correo()
    return "¡Prueba enviada! Revisa tu bandeja de entrada."

if __name__ == '__main__':
    app.run()
    
