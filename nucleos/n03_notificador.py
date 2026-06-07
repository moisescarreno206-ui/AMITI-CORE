def generar_alerta(analisis_previo):
    # Formatea la salida para que sea fácil de leer (como un informe oficial)
    if analisis_previo["estado_sistema"] == "ALERTA_CRITICA":
        mensaje = "!!! ADVERTENCIA: AMITI ha detectado una anomalía de seguridad !!!"
    else:
        mensaje = "Estado del sistema: Normal. Todo bajo control."
        
    return {
        "reporte": mensaje,
        "detalles": analisis_previo
    }
  
