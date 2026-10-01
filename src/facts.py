"""Hechos base que representan la evidencia y los resultados del sistema experto."""

from experta import Fact


class Evidence(Fact):
    """Observacion o propiedad identificada en una muestra de roca."""


class Origin(Fact):
    """Dato o hipotesis sobre el origen geologico de una muestra."""


class Classification(Fact):
    """Resultado de clasificacion asignado a una muestra."""


class Recommendation(Fact):
    """Recomendacion de uso asociada a la clasificacion obtenida."""