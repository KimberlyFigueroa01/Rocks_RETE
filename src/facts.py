"""Hechos base que representaran la evidencia y resultados del sistema."""

from experta import Fact


class Evidencia(Fact):
    """Observacion o propiedad identificada en una muestra de roca."""

    pass


class Origen(Fact):
    """Dato o hipotesis sobre el origen geologico de una muestra."""

    pass


class Clasificacion(Fact):
    """Resultado de clasificacion asignado a una muestra."""

    pass


class Recomendacion(Fact):
    """Recomendacion asociada a la clasificacion obtenida."""

    pass
