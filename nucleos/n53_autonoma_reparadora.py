# nucleos/n53_autonoma_reparadora.py
def diagnosticar_error(mensaje):
    if "import" in mensaje.lower():
        return "Acción requerida: Verificar que no haya imports circulares en los archivos de nucleos."
    return "Acción: Revisar logs del sistema."
    
