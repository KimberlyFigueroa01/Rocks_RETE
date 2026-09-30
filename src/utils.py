"""Utilidades de salida para inspeccionar el estado del motor."""

from experta import KnowledgeEngine


def print_working_memory_and_agenda(engine: KnowledgeEngine) -> None:
    """Muestra marcadores para la memoria de trabajo y la agenda.

    Esta funcion es un punto de extension: la inspeccion concreta de la agenda
    se completara cuando se definan las reglas y el formato de salida deseado.
    """
    print("Memoria de trabajo: (pendiente de implementar)")
    print("Agenda: (pendiente de implementar)")
