"""Hechos base que representaran la evidencia y resultados del sistema."""


from experta import KnowledgeEngine


class Evidence(Fact):
    """Observation or property identified in a rock sample."""
    pass


class Origin(Fact):
    """Data or hypothesis regarding the geological origin of a sample."""
    pass


class Classification(Fact):
    """Classification result assigned to a sample."""
    pass


class Recommendation(Fact):
    """Recommendation associated with the classification obtained."""
    pass



