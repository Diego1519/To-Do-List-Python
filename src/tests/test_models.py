import unittest
from datetime import date
from src.models import Tarea, GestorTareas

class TestTarea(unittest.TestCase):
    def setUp(self):
        # Tarea de ejemplo para todas las pruebas
        self.tarea = Tarea(
            nombre="Estudiar Python",
            descripcion="Completar el módulo de POO",
            fecha_limite="2024-12-31",
            prioridad="alta"
        )

    def test_creacion_tarea(self):
        """Verifica que una tarea se crea correctamente."""
        self.assertEqual(self.tarea.nombre, "Estudiar Python")
        self.assertEqual(self.tarea.descripcion, "Completar el módulo de POO")
        self.assertEqual(self.tarea.fecha_limite, "2024-12-31")
        self.assertEqual(self.tarea.prioridad, "alta")
        self.assertFalse(self.tarea.completada)  # Por defecto debe ser False

    def test_marcar_completada(self):
        """Prueba que marcar_completada() cambia el estado a True."""
        self.tarea.marcar_completada()
        self.assertTrue(self.tarea.completada)

    def test_str_representation(self):
        """Verifica que el método __str__ muestra la info correcta."""
        self.assertIn("Estudiar Python", str(self.tarea))
        self.assertIn("alta", str(self.tarea))

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()
        self.tarea1 = Tarea("Tarea 1", "Desc 1", "2024-06-15", "media")
        self.tarea2 = Tarea("Tarea 2", "Desc 2", "2024-06-20", "alta")

    def test_agregar_tarea(self):
        """Prueba que agregar_tarea() añade una tarea a la lista."""
        self.gestor.agregar_tarea(self.tarea1)
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertIn(self.tarea1, self.gestor.tareas)

    def test_eliminar_tarea(self):
        """Prueba eliminar una tarea existente."""
        self.gestor.agregar_tarea(self.tarea1)
        self.gestor.agregar_tarea(self.tarea2)
        self.gestor.eliminar_tarea(0)  # Eliminar la primera tarea
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertNotIn(self.tarea1, self.gestor.tareas)

    def test_listar_tareas_filtradas(self):
        """Prueba el filtrado por prioridad."""
        self.gestor.agregar_tarea(self.tarea1)
        self.gestor.agregar_tarea(self.tarea2)
        tareas_altas = self.gestor.listar_tareas(filtro_prioridad="alta")
        self.assertEqual(len(tareas_altas), 1)
        self.assertEqual(tareas_altas[0].nombre, "Tarea 2")

if __name__ == "__main__":
    unittest.main()