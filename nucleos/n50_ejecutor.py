# nucleos/n50_ejecutor.py
import importlib
import pkgutil
import nucleos

def ejecutar_accion(comando, tipo):
    """
    AMITI: Ejecutor dinámico universal.
    Escanea la carpeta nucleos y ejecuta el archivo correspondiente.
    """
    try:
        # Importación dinámica: intenta cargar el núcleo según el 'tipo'
        modulo_nombre = f"nucleos.{tipo}"
        modulo = importlib.import_module(modulo_nombre)
        
        # Compatibilidad: busca funciones estándar 'ejecutar' o nombres antiguos
        if hasattr(modulo, 'ejecutar'):
            return modulo.ejecutar(comando)
        elif hasattr(modulo, 'analizar_sentimiento'): # Compatibilidad con n54 viejo
            return modulo.analizar_sentimiento(comando)
            
        return f"Núcleo {tipo} cargado, pero no define una acción ejecutable."
    
    except ImportError:
        return f"Error: Núcleo '{tipo}' no encontrado. AMITI requiere que el archivo exista en la carpeta."
    except Exception as e:
        return f"AMITI Error crítico en núcleo: {str(e)}"
        
