"""Tests for the rock classification expert system."""

import unittest

from src.engine import RockClassificationEngine
from src.facts import Evidence, Classification, Recommendation


class TestSedimentaryRules(unittest.TestCase):
    """Verifies the classification of sedimentary rocks."""

    def _run(self, *evidences):
        """Initializes the engine, declares the evidence, and runs it."""
        engine = RockClassificationEngine()
        engine.reset()
        for ev in evidences:
            engine.declare(ev)
        engine.run()
        return engine

    def test_sandstone(self):
        """Clastic texture + sand => sandstone."""
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
            f"Expected 'sandstone', got: {classifications}",
        )

    def test_coal(self):
        """Plant remains => coal."""
        engine = self._run(Evidence(plant_remains='yes'))
        classifications = [
            dict(f) for f in engine.facts.values()
            if isinstance(f, Classification)
        ]
        self.assertTrue(
            any(c.get('rock') == 'coal' for c in classifications),
            f"Expected 'coal', got: {classifications}",
        )

    def test_sandstone_recommendation(self):
        """Sandstone generates construction recommendation."""
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
            f"Expected 'construction_walls_facades', got: {recommendations}",
        )


class TestEngineStartup(unittest.TestCase):
    """Verifies that the engine starts correctly without errors."""

    def test_engine_resets_cleanly(self):
        """The engine can reset and run without facts."""
        engine = RockClassificationEngine()
        engine.reset()
        engine.run()


if __name__ == "__main__":
    unittest.main()
