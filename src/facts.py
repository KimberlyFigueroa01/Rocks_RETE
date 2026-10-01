"""Base facts representing the evidence and results of the expert system."""

from experta import Fact


class Evidence(Fact):
    """Observation or property identified in a rock sample."""


class Origin(Fact):
    """Data or hypothesis regarding the geological origin of a sample."""


class Classification(Fact):
    """Classification result assigned to a sample."""


class Recommendation(Fact):
    """Recommendation associated with the classification obtained."""