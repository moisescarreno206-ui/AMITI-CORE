# nucleos/n50_ejecutor.py
# ... otros imports ...
from nucleos.n53_autonoma_reparadora import diagnosticar_error 

def ejecutar_accion_segura(comando, tipo):
    try:
        # Aquí iría tu lógica normal (procesar_calculo, etc.)
        # ...
        return "Ejecución exitosa"
    except Exception as e:
        # Si falla, AMITI se autodiagnostica
        error_info = str(e)
        return f"AMITI detectó un error: {error_info}. {diagnosticar_error(error_info)}"
        
