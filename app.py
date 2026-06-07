import sys
import os
sys.path.append(os.getcwd())

from nucleos.n01_orquestador import app
from nucleos.n05_activador import iniciar_activador

# Iniciamos el activador
iniciar_activador()

if __name__ == "__main__":
    app.run()
    
