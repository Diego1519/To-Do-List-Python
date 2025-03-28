from datetime import datetime

def formatear_fecha(fecha_str):
    """Convierte 'YYYY-MM-DD' a formato legible (ej: '31-Dic-2024')"""
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    return fecha.strftime("%d-%b-%Y")

def prioridad_a_emoji(prioridad):
    """Devuelve emoji según prioridad"""
    emojis = {"alta": "🔥", "media": "⚠️", "baja": "🐢"}
    return emojis.get(prioridad, "")