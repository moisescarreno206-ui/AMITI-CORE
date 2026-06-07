from nucleos.n01_orquestador import app
from nucleos.n05_activador import iniciar_activador

# Inicia el corazón de AMITI justo al arrancar
iniciar_activador()

if __name__ == "__main__":
    app.run()
    
