import sys
import os

# Esto fuerza a Python a incluir la carpeta actual en su lista de búsqueda
sys.path.append(os.getcwd())

from nucleos.n01_orquestador import app
from nucleos.n05_activador import iniciar_activador

# Iniciamos el activador
iniciar_activador()

# El servidor Gunicorn usará esta variable 'app'
if __name__ == "__main__":
    app.run()
    
