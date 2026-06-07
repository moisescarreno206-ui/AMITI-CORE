import sys
import os
# Añade la carpeta actual al path de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from nucleos.n01_orquestador import app
from nucleos.n05_activador import iniciar_activador

iniciar_activador()

if __name__ == "__main__":
    app.run()
    
