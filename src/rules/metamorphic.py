"""Reglas del sistema experto para rocas metamorficas.

Estructura de tres niveles (RETE):
  - Nivel 1: inferencia del origen (metamorfico).
  - Nivel 2: clasificacion de la roca especifica.
  - Nivel 3: recomendacion de uso.
"""

from experta import Rule, NOT, P, L

from src.facts import Evidence, Origin, Classification, Recommendation


class MetamorphicRules:
    """Mixin con todas las reglas de clasificacion de rocas metamorficas."""

    # -----------------------------------------------------------------------
    # NIVEL 1: Inferencia de origen
    # -----------------------------------------------------------------------

    @Rule(Evidence(foliation='yes'),
          Evidence(directional_stress='yes'),
          NOT(Origin()), salience=2)
    def r1_metamorphic(self):
        """Foliacion + estres direccional => origen metamorfico."""
        print("R1_metamorphic: foliation + directional stress -> metamorphic origin")
        self.declare(Origin(type='metamorphic'))

    @Rule(Evidence(foliation='no'),
          Evidence(solid_state_recrystallization='yes'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          Evidence(fractional_crystallization='no'),
          NOT(Origin()), salience=5)
    def r2_metamorphic(self):
        """Recristalizacion en estado solido sin rasgos sedimentarios ni igneos => origen metamorfico."""
        print("R2_metamorphic: solid-state recrystallization without sedimentary or igneous features -> metamorphic origin")
        self.declare(Origin(type='metamorphic'))

    # -----------------------------------------------------------------------
    # NIVEL 2: Clasificacion
    # -----------------------------------------------------------------------

    # Pizarra
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='slaty_foliation'),
          Evidence(grain_size='very_fine'),
          Evidence(protolith='shale'),
          NOT(Classification()), salience=3)
    def r3_metamorphic(self):
        """Metamorfica + foliacion pizarrosa + grano muy fino + protolito lutita => pizarra."""
        print("R3_metamorphic: slaty foliation + very fine grain + shale protolith -> slate")
        self.declare(Classification(rock='slate'))

    # Marmol
    @Rule(Origin(type='metamorphic'),
          Evidence(foliation='no'),
          Evidence(hcl_reaction='effervescent'),
          Evidence(protolith='limestone'),
          NOT(Classification()), salience=3)
    def r4_metamorphic(self):
        """Metamorfica + sin foliacion + efervescencia HCl + protolito caliza => marmol."""
        print("R4_metamorphic: no foliation + effervescent HCl reaction + limestone protolith -> marble")
        self.declare(Classification(rock='marble'))

    @Rule(Origin(type='metamorphic'),
          Evidence(texture='massive_saccharoidal_recrystallization'),
          Evidence(hcl_reaction='effervescent'),
          NOT(Classification()), salience=2)
    def r5_metamorphic(self):
        """Metamorfica + recristalizacion masiva sacaroidal + efervescencia HCl => marmol."""
        print("R5_metamorphic: massive saccharoidal recrystallization + effervescent HCl reaction -> marble")
        self.declare(Classification(rock='marble'))

    # Gneis
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='foliated_medium_to_coarse'),
          Evidence(banding='alternating_light_quartzofeldspathic_and_dark_mafic'),
          NOT(Classification()), salience=2)
    def r6_metamorphic(self):
        """Metamorfica + foliacion grano medio a grueso + bandas alternas => gneis."""
        print("R6_metamorphic: medium-to-coarse foliation + alternating bands -> gneiss")
        self.declare(Classification(rock='gneiss'))

    @Rule(Origin(type='metamorphic'),
          Evidence(texture='gneissic_banding'),
          Evidence(metamorphism_grade='intense'),
          Evidence(protolith=L('granitic') | L('sedimentary')),
          NOT(Classification()), salience=3)
    def r7_metamorphic(self):
        """Metamorfica + bandas gneisicas + metamorfismo intenso + protolito granitico o sedimentario => gneis."""
        print("R7_metamorphic: gneissic banding + intense metamorphism -> gneiss")
        self.declare(Classification(rock='gneiss'))

    # Cuarcita
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='massive_non_foliated'),
          Evidence(mineralogy='recrystallized_interlocking_quartz'),
          Evidence(mohs_hardness=P(lambda x: x >= 6.5)),
          NOT(Classification()), salience=3)
    def r8_metamorphic(self):
        """Metamorfica + textura masiva sin foliar + cuarzo entrelazado + dureza >= 6.5 => cuarcita."""
        print("R8_metamorphic: massive non-foliated texture + interlocking quartz + hardness >= 6.5 -> quartzite")
        self.declare(Classification(rock='quartzite'))

    @Rule(Origin(type='metamorphic'),
          Evidence(protolith='quartz_arenite'),
          Evidence(metamorphism_type=L('thermal') | L('regional')),
          NOT(Classification()), salience=2)
    def r9_metamorphic(self):
        """Metamorfica + protolito cuarzo-arenita + metamorfismo termico o regional => cuarcita."""
        print("R9_metamorphic: quartz-arenite protolith + thermal or regional metamorphism -> quartzite")
        self.declare(Classification(rock='quartzite'))

    # -----------------------------------------------------------------------
    # NIVEL 3: Recomendacion de uso
    # -----------------------------------------------------------------------

    @Rule(Origin(type='metamorphic'), Classification(rock='slate'))
    def r10_metamorphic(self):
        print("R10_metamorphic: slate -> waterproof roofing and cladding recommendation")
        self.declare(Recommendation(use=(
            'Waterproof roofing tiles, waterproofing panels and facade '
            'cladding (smooth cleavage planes, very low permeability)')))

    @Rule(Origin(type='metamorphic'), Classification(rock='marble'))
    def r11_metamorphic(self):
        print("R11_metamorphic: marble -> architectural finishes and decorative stone recommendation")
        self.declare(Recommendation(use=(
            'Interior architectural finishes, decorative cladding, floor '
            'slabs and monumental elements (workability, mirror-like polish, '
            'aesthetics)')))
