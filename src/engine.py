"""Motor de inferencia del sistema experto de clasificacion de rocas.

Ensambla los tres grupos de reglas (sedimentarias, igneas, metamorficas)
mediante herencia multiple para que el motor Rete de Experta construya
una unica red de condicion compartida.
"""

from experta import KnowledgeEngine

from src.rules.sedimentary import SedimentaryRules
from src.rules.igneous import IgneousRules
from src.rules.metamorphic import MetamorphicRules


class RockClassificationEngine(SedimentaryRules, IgneousRules, MetamorphicRules, KnowledgeEngine):
    """Motor de clasificacion de rocas basado en el algoritmo Rete.

    Hereda los tres mixins de reglas y la clase base de Experta.
    El orden de herencia (MRO de Python) coloca primero los mixins de reglas
    y KnowledgeEngine al final, respetando la convencion de Experta.
    """
