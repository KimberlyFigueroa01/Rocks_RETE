"""Pruebas del sistema experto de clasificacion de rocas."""

import unittest

from src.engine import RockClassificationEngine
from src.facts import Evidence, Classification, Recommendation


class TestSedimentaryRules(unittest.TestCase):
    """Verifica la clasificacion de rocas sedimentarias."""

    def _run(self, *evidences):
        """Inicializa el motor, declara las evidencias y lo ejecuta."""
        engine = RockClassificationEngine()
        engine.reset()
        for ev in evidences:
            engine.declare(ev)
        engine.run()
        return engine

    def test_sandstone(self):
        """Textura clastica + arena => arenisca."""
        engine = self._run(
            Evidence(texture='clastic'),
            Evidence(clast_size='sand'),
        )
        classifications = [
            dict(f) for f in engine.facts.values()
            if isinstance(f, Classification)
        ]
        self.assertTrue(
            any(c.get('rock') == 'sandstone' for c in classifications),
            f"Se esperaba 'sandstone', se obtuvo: {classifications}",
        )

    def test_coal(self):
        """Restos vegetales => carbon."""
        engine = self._run(Evidence(plant_remains='yes'))
        classifications = [
            dict(f) for f in engine.facts.values()
            if isinstance(f, Classification)
        ]
        self.assertTrue(
            any(c.get('rock') == 'coal' for c in classifications),
            f"Se esperaba 'coal', se obtuvo: {classifications}",
        )

    def test_sandstone_recommendation(self):
        """Arenisca genera recomendacion de construccion."""
        engine = self._run(
            Evidence(texture='clastic'),
            Evidence(clast_size='sand'),
        )
        recommendations = [
            dict(f) for f in engine.facts.values()
            if isinstance(f, Recommendation)
        ]
        self.assertTrue(
            any(r.get('use') == 'construction_walls_facades' for r in recommendations),
            f"Se esperaba 'construction_walls_facades', se obtuvo: {recommendations}",
        )


class TestEngineStartup(unittest.TestCase):
    """Verifica que el motor arranca correctamente sin errores."""

    def test_engine_resets_cleanly(self):
        """El motor puede reiniciarse y ejecutarse sin hechos."""
        engine = RockClassificationEngine()
        engine.reset()
        engine.run()


if __name__ == "__main__":
    unittest.main()
