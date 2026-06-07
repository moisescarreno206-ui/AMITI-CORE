# nucleos/n44_calculo_logico.py

import re

def calcular(expresion):
    """Núcleo 44: Procesador matemático y lógico."""
    # Intentamos extraer números de la frase
    numeros = re.findall(r'\d+', expresion)
    
    if "cuánto es" in expresion or "+" in expresion:
        if len(numeros) >= 2:
            resultado = int(numeros[0]) + int(numeros[1])
            return f"El resultado de la operación es {resultado}."
            
    return "Estoy analizando la operación, pero necesito una estructura más clara para procesarla."
