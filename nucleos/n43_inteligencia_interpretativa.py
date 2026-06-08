from nucleos.n50_ejecutor import ejecutar_accion
from nucleos.n49_vigilante import vigilar_sistema
from nucleos.n46_analizador_sentimental import analizar_texto

def procesar_comando(cmd):
    comando = cmd.lower()
    
    # Vigilancia
    if "ADVERTENCIA" in vigilar_sistema(comando):
        return "AMITI: Problema detectado."
        
    # Despacho al ejecutor
    if any(op in comando for op in ["+", "-"]):
        return ejecutar_accion(comando, "calculo")
    
    if any(p in comando for p in ["crear", "mejora"]):
        return ejecutar_accion(comando, "arquitecto")
        
    return "AMITI: Comando recibido."
    
