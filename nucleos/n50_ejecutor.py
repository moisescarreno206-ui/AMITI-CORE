# nucleos/n50_ejecutor.py
import importlib

# Diccionario maestro de capacidades (registra todos tus núcleos aquí)
CAPACIDADES = {
    "analisis": "n54_analizador_sentimental",
    "red": "n52_dominio_de_red",
    "reparacion": "n53_autonoma_reparadora",
    "arquitectura": "n48_arquitecto_autonomo",
    "errores": "n47_gestor_de_errores"
    # Puedes añadir cualquier otro núcleo de tu lista (n08 al n54) siguiendo este formato
}

def ejecutar_accion(comando, tipo):
    try:
        # 1. Identificar el núcleo necesario dinámicamente
        nombre_archivo = CAPACIDADES.get(tipo)
        if not nombre_archivo:
            return f"AMITI: No se encontró un núcleo experto para '{tipo}'."

        # 2. Carga dinámica segura
        modulo = importlib.import_module(f"nucleos.{nombre_archivo}")
        
        # 3. Ejecución polimórfica
        if hasattr(modulo, 'ejecutar'):
            return modulo.ejecutar(comando)
        elif hasattr(modulo, 'analizar_sentimiento'): # Compatibilidad legacy
            return modulo.analizar_sentimiento(comando)
            
        return f"Núcleo '{nombre_archivo}' invocado con éxito."

    except ImportError:
        return f"AMITI Error: El núcleo '{nombre_archivo}' no está en la carpeta 'nucleos/'."
    except Exception as e:
        return f"Error emergente detectado. Invocando n53_autonoma_reparadora: {str(e)}"
        
