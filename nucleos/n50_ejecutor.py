# nucleos/n50_ejecutor.py
import importlib

def ejecutar_accion(comando, tipo):
    try:
        # Carga dinámica: AMITI busca el módulo según el tipo
        modulo_nombre = f"nucleos.{tipo}"
        modulo = importlib.import_module(modulo_nombre)
        
        # Ejecuta la función principal del módulo
        if hasattr(modulo, 'ejecutar'):
            return modulo.ejecutar(comando)
        return f"Módulo {tipo} cargado, pero no tiene función 'ejecutar'."
        
    except ImportError:
        return f"Error: No se pudo cargar el núcleo {tipo}. Verifique que el archivo exista."
    except Exception as e:
        return f"AMITI Error crítico: {str(e)}"
        
