class Tarea:
    def __init__(self, nombre, descripcion, fecha_limite, prioridad, completada=False):
        self.nombre = nombre 
        self.descripcion = descripcion 
        self.fecha_limite = fecha_limite  #Usar formato "YYYY-MM-DD"
        self.prioridad = prioridad #"alta", "media", "baja"
        self.completada = completada 

    def marcar_completada(self):
        self.completada = True 

class GestorTareas:
    def __init__(self):
        self.tareas = [] # Lista para almanecar tareas 

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def listar_tareas(self, filtro_prioridad=None, filtro_completadas=None):
        #Filtrado logico aqui 
        pass