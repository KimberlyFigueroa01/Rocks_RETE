"""Punto de entrada para ejecutar el esqueleto del sistema experto."""

from src.engine import RockClassificationEngine
from src.facts import Evidencia
from src.utils import print_working_memory_and_agenda


def main() -> None:
    """Inicializa el motor, declara un hecho de prueba y ejecuta las reglas."""
    engine = RockClassificationEngine()
    engine.reset()
    engine.declare(Evidencia())
    engine.run()
    print_working_memory_and_agenda(engine)


if __name__ == "__main__":
    main()
