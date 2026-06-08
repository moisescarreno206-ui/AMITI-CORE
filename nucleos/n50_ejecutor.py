# nucleos/n50_ejecutor.py
import importlib

# Diccionario maestro: define qué núcleo resuelve qué problema
CAPACIDADES = {
    "analisis": "n54_analizador_sentimental",
    "red": "n52_dominio_de_red",
    "reparacion": "n53_autonoma_reparadora",
    "arquitectura": "n48_arquitecto_autonomo",
    "errores": "n47_gestor_de_errores",
    "memoria": "n45_memoria",
    "logica": "n44_calculo_logico",
    "vigilancia": "n49_vigilante"
    # Puedes añadir cualquier otro núcleo aquí para expansión futura
}

def ejecutar_accion(comando, tipo):
    try:
        # 1. Identificar el núcleo necesario
        nombre_archivo = CAPACIDADES.get(tipo)
        if not nombre_archivo:
            return f"AMITI: No se encontró un núcleo experto para {tipo}."

        # 2. Carga dinámica del núcleo
        modulo = importlib.import_module(f"nucleos.{nombre_archivo}")
        
        # 3. Ejecución polimórfica (busca la función principal)
        if hasattr(modulo, 'ejecutar'):
            return modulo.ejecutar(comando)
        elif hasattr(modulo, 'analizar_sentimiento'): # Legacy support
            return modulo.analizar_sentimiento(comando)
            
        return f"Núcleo {nombre_archivo} invocado, pero requiere configuración de ejecución."

    except ImportError:
        return f"AMITI Error: El núcleo {nombre_archivo} no está presente en la carpeta."
    except Exception as e:
        # Aquí el n47 (gestor de errores) debería tomar control si falla la ejecución
        return f"Error emergente detectado. Invocando diagnóstico: {str(e)}"
