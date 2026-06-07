from nucleos.n01_orquestador import app

if __name__ == "__main__":
    # Esto permite que Gunicorn (el servidor de la nube) 
    # encuentre y ejecute nuestro Orquestador
    app.run()
