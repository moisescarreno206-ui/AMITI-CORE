# nucleos/n44_calculo_logico.py

def procesar_calculo(comando):
    # Lógica simple para manejar operaciones
    try:
        # Esto evalúa la expresión matemática de forma segura
        # Ejemplo: "2+2" se convierte en 4
        resultado = eval(comando.replace('suma', '+').replace('resta', '-'))
        return f"Resultado: {resultado}"
    except:
        return "No pude calcular eso, intenta con números."
        
