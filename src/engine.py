"""Inference engine for the rock classification expert system.

Assembles the three rule groups (sedimentary, igneous, metamorphic)
using multiple inheritance so that Experta's Rete engine builds
a single shared condition network.
"""

from experta import KnowledgeEngine

from src.rules.sedimentary import SedimentaryRules
from src.rules.igneous import IgneousRules
from src.rules.metamorphic import MetamorphicRules


class RockClassificationEngine(SedimentaryRules, IgneousRules, MetamorphicRules, KnowledgeEngine):
    """Rock classification engine based on the Rete algorithm.

    Inherits the three rule mixins and Experta's base class.
    The inheritance order (Python's MRO) places the rule mixins first
    and KnowledgeEngine at the end, respecting Experta's convention.
    """
