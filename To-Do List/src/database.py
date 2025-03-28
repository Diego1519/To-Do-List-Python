import sqlite3 def 

def crear_tablas():
    conexion = sqlite3.connect("tareas.db")
    cursor = conexion.cursor()
    cursos.execute('''
    CREATE TABLE IF NOT EXISTE tareas(
        id INTEFER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        descripcion TEXT,
        fecha_limite TEXT,
        prioridad TEXT,
        completada BOOLEAN
    )
''')
conexion.commit()
conexion.close

#Llamar esta funcion al inicio del programa 
crear_tabla()