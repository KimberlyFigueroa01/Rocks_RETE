"""Pruebas iniciales del esqueleto del sistema experto."""

import unittest

from src.engine import RockClassificationEngine
from src.facts import Evidencia


class TestRockClassificationEngine(unittest.TestCase):
    """Comprueba que el motor puede iniciarse y aceptar un hecho base."""

    def test_engine_accepts_stub_fact(self) -> None:
        engine = RockClassificationEngine()
        engine.reset()
        engine.declare(Evidencia())
        engine.run()


if __name__ == "__main__":
    unittest.main()
