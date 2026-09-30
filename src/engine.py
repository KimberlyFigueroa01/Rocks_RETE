"""Motor de inferencia del sistema experto."""

from experta import KnowledgeEngine


class RockClassificationEngine(KnowledgeEngine):
    """Motor Rete; las reglas de clasificacion se agregaran posteriormente."""

    # Guia para reglas futuras:
    # @Rule(Evidencia(propiedad="..."))
    # def evaluar_evidencia(self):
    #     """Deriva o declara nuevos hechos a partir de la evidencia."""
    #     pass
