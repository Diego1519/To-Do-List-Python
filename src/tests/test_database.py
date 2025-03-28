import unittest
import sqlite3
from src.database import crear_tabla, agregar_tarea

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        crear_tabla(self.conn)

    def test_crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tareas'")
        self.assertIsNotNone(cursor.fetchone())

    def test_agregar_tarea(self):
        agregar_tarea(self.conn, "Tarea Test", "Desc", "2024-12-31", "alta")
        cursor = self.conn.cursor()
        cursor.execute("SELECT nombre FROM tareas")
        self.assertEqual(cursor.fetchone()[0], "Tarea Test")

if __name__ == "__main__":
    unittest.main()