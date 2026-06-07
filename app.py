import traceback # Añade esto arriba en los imports de app.py

@app.route('/test-email')
def test_email():
    try:
        from nucleos.n03_notificador import probar_correo
        resultado = probar_correo()
        return f"Éxito: {resultado}"
    except Exception:
        # Esto te mostrará el error detallado en la pantalla de tu celular
        return f"Error detallado: {traceback.format_exc()}"
        
