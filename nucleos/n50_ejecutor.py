# nucleos/n50_ejecutor.py
from nucleos.n51_arquitecto_supremo import potenciar_creacion
from nucleos.n52_dominio_de_red import exponer_dominio

def ejecutar_accion(comando, tipo):
    # ... (tus otras condiciones)
    elif tipo == "arquitecto_supremo":
        return potenciar_creacion(comando)
    elif tipo == "red":
        return exponer_dominio(comando)
