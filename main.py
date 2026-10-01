"""Punto de entrada del sistema experto de clasificacion de rocas.

Ejemplo de uso: clasifica una muestra con textura clastica y tamano arena
(resultado esperado: arenisca / sandstone -> uso: construccion).

Para clasificar otra muestra, reemplaza los hechos de Evidence declarados
en ``main()`` con las propiedades observadas en el laboratorio.
"""

from src.engine import RockClassificationEngine
from src.facts import Evidence
from src.utils import print_working_memory_and_agenda


def main() -> None:
    """Inicializa el motor, declara evidencias de muestra y ejecuta las reglas."""
    engine = RockClassificationEngine()
    engine.reset()

    # --- Evidencias de la muestra a clasificar ---
    # Modifica estos hechos para clasificar distintas muestras.
    engine.declare(Evidence(texture='clastic'))
    engine.declare(Evidence(clast_size='sand'))

    engine.run()

    print_working_memory_and_agenda(engine)


if __name__ == "__main__":
    main()
