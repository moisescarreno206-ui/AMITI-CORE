# Dentro de tu n43, ajusta la lógica de delegación así:
from nucleos import n47_gestor_de_errores

# ... en tu función procesar_comando ...
try:
    if "2+2" in cmd:
        return n44_calculo_logico.procesar_calculo(cmd)
    # ... resto de tu lógica ...
except Exception as e:
    return n47_gestor_de_errores.manejar_error(str(e))
    
