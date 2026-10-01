"""Entry point for the rock classification expert system.

Usage example: classifies a sample with clastic texture and sand size
(expected result: sandstone -> use: construction).

To classify another sample, replace the Evidence facts declared
in ``main()`` with the properties observed in the lab.
"""

from src.engine import RockClassificationEngine
from src.facts import Evidence
from src.utils import print_working_memory_and_agenda


def main() -> None:
    """Initializes the engine, declares sample evidence, and runs the rules."""
    engine = RockClassificationEngine()
    engine.reset()

    # --- Evidence of the sample to classify ---
    # Modify these facts to classify different samples.
    engine.declare(Evidence(texture='clastic'))
    engine.declare(Evidence(clast_size='sand'))

    engine.run()

    print_working_memory_and_agenda(engine)


if __name__ == "__main__":
    main()
