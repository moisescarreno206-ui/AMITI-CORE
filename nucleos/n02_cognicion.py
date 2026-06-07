def analizar_seguridad(datos_entrada):
    amenazas_conocidas = ["intento_acceso", "fallo_clave", "actividad_sospechosa"]
    estado = "SEGURO"
    for amenaza in amenazas_conocidas:
        if amenaza in datos_entrada:
            estado = "ALERTA_CRITICA"
            break
    return {
        "analisis": "completado",
        "estado_sistema": estado,
        "nucleo_origen": "02_COGNICION"
    }
  
