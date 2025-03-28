from datetime import datetime

def validar_fecha(fecha_str):
    """Valida formato YYYY-MM-DD y que sea fecha futura"""
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        return fecha >= datetime.now()
    except ValueError:
        return False

def validar_prioridad(prioridad):
    """Valida que la prioridad sea válida"""
    return prioridad.lower() in ["alta", "media", "baja"]