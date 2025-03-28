from datetime import datetime

class Tarea:
    def __init__(self, nombre, descripcion, fecha, prioridad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.prioridad = prioridad
        self.completada = False

class GestorTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas, 1):
            estado = "✓" if tarea.completada else "✗"
            print(f"{i}. [{estado}] {tarea.nombre} ({tarea.prioridad}) - Fecha: {tarea.fecha}")

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# --- Programa principal ---
gestor = GestorTareas()

while True:
    print("\n=== MENÚ ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar como completada")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("\nNueva tarea:")
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        while not validar_fecha(fecha):
            print("¡Formato incorrecto! Usa YYYY-MM-DD")
            fecha = input("Fecha (YYYY-MM-DD): ")
        prioridad = input("Prioridad (alta/media/baja): ").lower()
        while prioridad not in ["alta", "media", "baja"]:
            print("¡Prioridad inválida!")
            prioridad = input("Prioridad (alta/media/baja): ").lower()
        
        nueva_tarea = Tarea(nombre, descripcion, fecha, prioridad)
        gestor.agregar_tarea(nueva_tarea)
        print("✅ ¡Tarea agregada!")
    
    elif opcion == "2":
        print("\n--- TAREAS ---")
        if not gestor.tareas:
            print("No hay tareas registradas.")
        else:
            gestor.mostrar_tareas()
    
    elif opcion == "3":
        gestor.mostrar_tareas()
        if gestor.tareas:
            num = int(input("Número de tarea a completar: ")) - 1
            if 0 <= num < len(gestor.tareas):
                gestor.tareas[num].completada = True
                print("✅ ¡Tarea completada!")
            else:
                print("❌ Número inválido")
    
    elif opcion == "4":
        print("¡Hasta luego! 👋")
        break
    
    else:
        print("❌ Opción no válida")