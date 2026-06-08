# nucleos/n53_autonoma_reparadora.py

def diagnosticar_error(mensaje_error):
    """
    Núcleo de auto-reparación. 
    Analiza errores y devuelve instrucciones de corrección.
    """
    mensaje_error = mensaje_error.lower()
    
    if "circular import" in mensaje_error:
        return "Acción: Romper dependencia. Mover importación al interior de la función en el archivo afectado."
    elif "no module named" in mensaje_error:
        return "Acción: Verificar nombre de archivo en GitHub y ejecutar 'Clear build cache' en Render."
    elif "invalid syntax" in mensaje_error:
        return "Acción: Revisar caracteres invisibles o errores de indentación en la línea indicada."
    
    return "Acción: Registro de error crítico enviado a logs."
  
