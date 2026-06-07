# nucleos/n43_inteligencia_interpretativa.py
from nucleos import n44_calculo_logico, n45_memoria_sesion, n46_explorador_externo

def procesar_comando(comando):
    cmd = comando.lower()
    
    # Guardar en memoria
    n45_memoria_sesion.guardar_recuerdo(cmd)
    
    # Lógica de delegación
    if any(op in cmd for op in ["+", "-", "suma"]):
        return n44_calculo_logico.procesar_calculo(cmd)
    
    elif "hora" in cmd:
        return n46_explorador_externo.obtener_contexto_externo()
        
    elif "qué dije antes" in cmd:
        return f"Tus últimos mensajes: {n45_memoria_sesion.obtener_recuerdos()}"
        
    return "Procesando información con acceso total a memoria y contexto externo."
    
