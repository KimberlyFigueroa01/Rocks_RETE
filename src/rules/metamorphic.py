"""Expert system rules for metamorphic rocks.

Three-level structure (RETE):
  - Level 1: origin inference (metamorphic).
  - Level 2: specific rock classification.
  - Level 3: usage recommendation.
"""

from experta import Rule, NOT, P, L

from src.facts import Evidence, Origin, Classification, Recommendation


class MetamorphicRules:
    """Mixin containing all classification rules for metamorphic rocks."""

    # -----------------------------------------------------------------------
    # LEVEL 1: Origin inference
    # -----------------------------------------------------------------------

    @Rule(Evidence(foliation='yes'),
          Evidence(directional_stress='yes'),
          NOT(Origin()), salience=2)
    def r1_metamorphic(self):
        """Foliation + directional stress => metamorphic origin."""
        print("R1_metamorphic: foliation + directional stress -> metamorphic origin")
        self.declare(Origin(type='metamorphic'))

    @Rule(Evidence(foliation='no'),
          Evidence(solid_state_recrystallization='yes'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          Evidence(fractional_crystallization='no'),
          NOT(Origin()), salience=5)
    def r2_metamorphic(self):
        """Solid-state recrystallization without sedimentary or igneous features => metamorphic origin."""
        print("R2_metamorphic: solid-state recrystallization without sedimentary or igneous features -> metamorphic origin")
        self.declare(Origin(type='metamorphic'))

    # -----------------------------------------------------------------------
    # LEVEL 2: Classification
    # -----------------------------------------------------------------------

    # Slate
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='slaty_foliation'),
          Evidence(grain_size='very_fine'),
          Evidence(protolith='shale'),
          NOT(Classification()), salience=3)
    def r3_metamorphic(self):
        """Metamorphic + slaty foliation + very fine grain + shale protolith => slate."""
        print("R3_metamorphic: slaty foliation + very fine grain + shale protolith -> slate")
        self.declare(Classification(rock='slate'))

    # Marble
    @Rule(Origin(type='metamorphic'),
          Evidence(foliation='no'),
          Evidence(hcl_reaction='effervescent'),
          Evidence(protolith='limestone'),
          NOT(Classification()), salience=3)
    def r4_metamorphic(self):
        """Metamorphic + no foliation + HCl effervescence + limestone protolith => marble."""
        print("R4_metamorphic: no foliation + effervescent HCl reaction + limestone protolith -> marble")
        self.declare(Classification(rock='marble'))

    @Rule(Origin(type='metamorphic'),
          Evidence(texture='massive_saccharoidal_recrystallization'),
          Evidence(hcl_reaction='effervescent'),
          NOT(Classification()), salience=2)
    def r5_metamorphic(self):
        """Metamorphic + massive saccharoidal recrystallization + HCl effervescence => marble."""
        print("R5_metamorphic: massive saccharoidal recrystallization + effervescent HCl reaction -> marble")
        self.declare(Classification(rock='marble'))

    # Gneiss
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='foliated_medium_to_coarse'),
          Evidence(banding='alternating_light_quartzofeldspathic_and_dark_mafic'),
          NOT(Classification()), salience=2)
    def r6_metamorphic(self):
        """Metamorphic + medium to coarse foliation + alternating bands => gneiss."""
        print("R6_metamorphic: medium-to-coarse foliation + alternating bands -> gneiss")
        self.declare(Classification(rock='gneiss'))

    @Rule(Origin(type='metamorphic'),
          Evidence(texture='gneissic_banding'),
          Evidence(metamorphism_grade='intense'),
          Evidence(protolith=L('granitic') | L('sedimentary')),
          NOT(Classification()), salience=3)
    def r7_metamorphic(self):
        """Metamorphic + gneissic banding + intense metamorphism + granitic or sedimentary protolith => gneiss."""
        print("R7_metamorphic: gneissic banding + intense metamorphism -> gneiss")
        self.declare(Classification(rock='gneiss'))

    # Quartzite
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='massive_non_foliated'),
          Evidence(mineralogy='recrystallized_interlocking_quartz'),
          Evidence(mohs_hardness=P(lambda x: x >= 6.5)),
          NOT(Classification()), salience=3)
    def r8_metamorphic(self):
        """Metamorphic + massive non-foliated texture + interlocking quartz + hardness >= 6.5 => quartzite."""
        print("R8_metamorphic: massive non-foliated texture + interlocking quartz + hardness >= 6.5 -> quartzite")
        self.declare(Classification(rock='quartzite'))

    @Rule(Origin(type='metamorphic'),
          Evidence(protolith='quartz_arenite'),
          Evidence(metamorphism_type=L('thermal') | L('regional')),
          NOT(Classification()), salience=2)
    def r9_metamorphic(self):
        """Metamorphic + quartz-arenite protolith + thermal or regional metamorphism => quartzite."""
        print("R9_metamorphic: quartz-arenite protolith + thermal or regional metamorphism -> quartzite")
        self.declare(Classification(rock='quartzite'))

    # -----------------------------------------------------------------------
    # LEVEL 3: Usage recommendation
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
