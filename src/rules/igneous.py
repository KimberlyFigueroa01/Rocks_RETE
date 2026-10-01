"""Expert system rules for igneous rocks.

Three-level structure (RETE):
  - Level 1: origin inference (igneous).
  - Level 2: specific rock classification.
  - Level 3: usage recommendation.
"""

from experta import Rule, NOT, P

from src.facts import Evidence, Origin, Classification, Recommendation


class IgneousRules:
    """Mixin containing all classification rules for igneous rocks."""

    # -----------------------------------------------------------------------
    # LEVEL 1: Origin inference
    # -----------------------------------------------------------------------

    @Rule(Evidence(fractional_crystallization='yes'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          NOT(Origin()), salience=3)
    def r1_igneous(self):
        """Fractional crystallization (no fossils or stratification) => igneous origin."""
        print("R1_igneous: fractional crystallization -> igneous origin")
        self.declare(Origin(type='igneous'))

    @Rule(Evidence(crystalline_mosaic_texture='yes'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          NOT(Origin()), salience=3)
    def r2_igneous(self):
        """Crystalline mosaic texture (no fossils or stratification) => igneous origin."""
        print("R2_igneous: crystalline mosaic texture -> igneous origin")
        self.declare(Origin(type='igneous'))

    # Allows obsidian (glassy, no crystals) to reach Level 2.
    @Rule(Evidence(texture='glassy_amorphous'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          NOT(Origin()), salience=3)
    def r3_igneous(self):
        """Glassy-amorphous texture (no fossils or stratification) => igneous origin."""
        print("R3_igneous: glassy amorphous texture -> igneous origin")
        self.declare(Origin(type='igneous'))

    # -----------------------------------------------------------------------
    # LEVEL 2: Classification
    # -----------------------------------------------------------------------

    # Granite
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic_porphyritic'),
          Evidence(color='light'),
          Evidence(quartz='rich'),
          NOT(Classification()), salience=3)
    def r4_igneous(self):
        """Igneous + phaneritic-porphyritic texture + light color + rich quartz => granite."""
        print("R4_igneous: igneous + phaneritic porphyritic texture + light color + rich quartz -> granite")
        self.declare(Classification(rock='granite'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='felsic'),
          NOT(Classification()), salience=1)
    def r5_igneous(self):
        """Igneous + felsic composition => granite."""
        print("R5_igneous: felsic composition -> granite")
        self.declare(Classification(rock='granite'))

    # Rhyolite
    @Rule(Origin(type='igneous'),
          Evidence(texture='aphanitic'),
          Evidence(color='light'),
          Evidence(quartz='present'),
          NOT(Classification()), salience=3)
    def r6_igneous(self):
        """Igneous + aphanitic texture + light color + quartz present => rhyolite."""
        print("R6_igneous: aphanitic texture + light color + quartz present -> rhyolite")
        self.declare(Classification(rock='rhyolite'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='volcanic_equivalent_to_granite'),
          NOT(Classification()), salience=1)
    def r7_igneous(self):
        """Igneous + volcanic equivalent to granite composition => rhyolite."""
        print("R7_igneous: volcanic equivalent to granite -> rhyolite")
        self.declare(Classification(rock='rhyolite'))

    # Basalt
    @Rule(Origin(type='igneous'),
          Evidence(texture='aphanitic_volcanic'),
          Evidence(color='dark'),
          Evidence(density='high'),
          NOT(Classification()), salience=3)
    def r8_igneous(self):
        """Igneous + aphanitic volcanic texture + dark color + high density => basalt."""
        print("R8_igneous: aphanitic volcanic texture + dark color + high density -> basalt")
        self.declare(Classification(rock='basalt'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='mafic_ferromagnesian_rich'),
          Evidence(quartz='absent'),
          NOT(Classification()), salience=2)
    def r9_igneous(self):
        """Igneous + mafic ferromagnesian-rich composition + absent quartz => basalt."""
        print("R9_igneous: mafic ferromagnesian-rich composition + absent quartz -> basalt")
        self.declare(Classification(rock='basalt'))

    # Diorite
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic'),
          Evidence(quartz='absent'),
          Evidence(composition='intermediate_salt_and_pepper'),
          NOT(Classification()), salience=3)
    def r10_igneous(self):
        """Igneous + phaneritic texture + absent quartz + intermediate salt-and-pepper composition => diorite."""
        print("R10_igneous: phaneritic texture + absent quartz + intermediate salt-and-pepper composition -> diorite")
        self.declare(Classification(rock='diorite'))

    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic'),
          Evidence(color='intermediate'),
          Evidence(dominant_minerals='plagioclase_amphibole'),
          NOT(Classification()), salience=3)
    def r11_igneous(self):
        """Igneous + phaneritic texture + intermediate color + plagioclase-amphibole => diorite."""
        print("R11_igneous: phaneritic texture + intermediate color + plagioclase and amphibole -> diorite")
        self.declare(Classification(rock='diorite'))

    # Andesite
    @Rule(Origin(type='igneous'),
          Evidence(texture='aphanitic_fine_grained'),
          Evidence(color='medium_gray'),
          Evidence(quartz='not_dominant'),
          NOT(Classification()), salience=3)
    def r12_igneous(self):
        """Igneous + fine-grained aphanitic texture + medium gray + non-dominant quartz => andesite."""
        print("R12_igneous: fine-grained aphanitic texture + medium-gray color + non-dominant quartz -> andesite")
        self.declare(Classification(rock='andesite'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='intermediate_volcanic'),
          Evidence(phenocrysts='plagioclase_amphibole'),
          NOT(Classification()), salience=2)
    def r13_igneous(self):
        """Igneous + intermediate volcanic composition + plagioclase-amphibole phenocrysts => andesite."""
        print("R13_igneous: intermediate volcanic composition + plagioclase-amphibole phenocrysts -> andesite")
        self.declare(Classification(rock='andesite'))

    # Gabbro
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic'),
          Evidence(color='dark_green_to_black'),
          Evidence(dominant_minerals='ferromagnesian'),
          Evidence(quartz='absent'),
          NOT(Classification()), salience=4)
    def r14_igneous(self):
        """Igneous + phaneritic texture + dark green to black color + ferromagnesians + absent quartz => gabbro."""
        print("R14_igneous: phaneritic texture + dark color + ferromagnesian minerals + absent quartz -> gabbro")
        self.declare(Classification(rock='gabbro'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='mafic_plutonic'),
          Evidence(dominant_minerals='pyroxene_calcic_plagioclase'),
          NOT(Classification()), salience=2)
    def r15_igneous(self):
        """Igneous + mafic plutonic composition + pyroxene-calcic plagioclase => gabbro."""
        print("R15_igneous: mafic plutonic composition + pyroxene and calcic plagioclase -> gabbro")
        self.declare(Classification(rock='gabbro'))

    # Obsidian
    @Rule(Origin(type='igneous'),
          Evidence(texture='glassy_amorphous'),
          Evidence(cooling='instantaneous'),
          NOT(Classification()), salience=2)
    def r16_igneous(self):
        """Igneous + glassy-amorphous texture + instantaneous cooling => obsidian."""
        print("R16_igneous: glassy amorphous texture + instantaneous cooling -> obsidian")
        self.declare(Classification(rock='obsidian'))

    @Rule(Origin(type='igneous'),
          Evidence(fracture='conchoidal_perfect'),
          Evidence(luster='glassy'),
          NOT(Classification()), salience=2)
    def r17_igneous(self):
        """Igneous + perfect conchoidal fracture + glassy luster => obsidian."""
        print("R17_igneous: perfect conchoidal fracture + glassy luster -> obsidian")
        self.declare(Classification(rock='obsidian'))

    # Pegmatite
    @Rule(Origin(type='igneous'),
          Evidence(texture='pegmatitic'),
          Evidence(crystal_size_cm=P(lambda x: x > 2)),
          NOT(Classification()), salience=2)
    def r18_igneous(self):
        """Igneous + pegmatitic texture + crystals > 2 cm => pegmatite."""
        print("R18_igneous: pegmatitic texture + crystals larger than 2 cm -> pegmatite")
        self.declare(Classification(rock='pegmatite'))

    @Rule(Origin(type='igneous'),
          Evidence(giant_crystals='quartz_and_feldspar'),
          Evidence(environment='late_magmatic'),
          NOT(Classification()), salience=2)
    def r19_igneous(self):
        """Igneous + giant quartz and feldspar crystals + late-magmatic environment => pegmatite."""
        print("R19_igneous: giant quartz and feldspar crystals + late magmatic environment -> pegmatite")
        self.declare(Classification(rock='pegmatite'))

    # -----------------------------------------------------------------------
    # LEVEL 3: Usage recommendation
    # -----------------------------------------------------------------------

    @Rule(Origin(type='igneous'), Classification(rock='basalt'))
    def r20_igneous(self):
        print("R20_igneous: basalt -> crushed-stone aggregate recommendation")
        self.declare(Recommendation(use=(
            'Crushed stone aggregate for high-strength concrete and asphalt '
            'pavements (homogeneous, isotropic, uniform stress distribution)')))

    @Rule(Origin(type='igneous'), Classification(rock='granite'))
    def r21_igneous(self):
        print("R21_igneous: granite -> ornamental and structural stone recommendation")
        self.declare(Recommendation(use=(
            'Ornamental slabs, paving stones, building cladding and heavy '
            'foundation blocks (high hardness, low porosity, high compressive '
            'strength)')))
