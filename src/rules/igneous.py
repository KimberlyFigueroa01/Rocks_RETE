"""Reglas del sistema experto para rocas igneas.

Estructura de tres niveles (RETE):
  - Nivel 1: inferencia del origen (igneo).
  - Nivel 2: clasificacion de la roca especifica.
  - Nivel 3: recomendacion de uso.
"""

from experta import Rule, NOT, P

from src.facts import Evidence, Origin, Classification, Recommendation


class IgneousRules:
    """Mixin con todas las reglas de clasificacion de rocas igneas."""

    # -----------------------------------------------------------------------
    # NIVEL 1: Inferencia de origen
    # -----------------------------------------------------------------------

    @Rule(Evidence(fractional_crystallization='yes'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          NOT(Origin()), salience=3)
    def r1_igneous(self):
        """Cristalizacion fraccionada (sin fosiles ni estratificacion) => origen igneo."""
        print("R1_igneous: fractional crystallization -> igneous origin")
        self.declare(Origin(type='igneous'))

    @Rule(Evidence(crystalline_mosaic_texture='yes'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          NOT(Origin()), salience=3)
    def r2_igneous(self):
        """Textura mosaico cristalino (sin fosiles ni estratificacion) => origen igneo."""
        print("R2_igneous: crystalline mosaic texture -> igneous origin")
        self.declare(Origin(type='igneous'))

    # Permite que la obsidiana (vidrio, sin cristales) llegue al Nivel 2.
    @Rule(Evidence(texture='glassy_amorphous'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          NOT(Origin()), salience=3)
    def r3_igneous(self):
        """Textura vitrea-amorfa (sin fosiles ni estratificacion) => origen igneo."""
        print("R3_igneous: glassy amorphous texture -> igneous origin")
        self.declare(Origin(type='igneous'))

    # -----------------------------------------------------------------------
    # NIVEL 2: Clasificacion
    # -----------------------------------------------------------------------

    # Granito
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic_porphyritic'),
          Evidence(color='light'),
          Evidence(quartz='rich'),
          NOT(Classification()), salience=3)
    def r4_igneous(self):
        """Igneo + textura fanerica-porfiritica + color claro + cuarzo rico => granito."""
        print("R4_igneous: igneous + phaneritic porphyritic texture + light color + rich quartz -> granite")
        self.declare(Classification(rock='granite'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='felsic'),
          NOT(Classification()), salience=1)
    def r5_igneous(self):
        """Igneo + composicion felsica => granito."""
        print("R5_igneous: felsic composition -> granite")
        self.declare(Classification(rock='granite'))

    # Riolita
    @Rule(Origin(type='igneous'),
          Evidence(texture='aphanitic'),
          Evidence(color='light'),
          Evidence(quartz='present'),
          NOT(Classification()), salience=3)
    def r6_igneous(self):
        """Igneo + textura afanitica + color claro + cuarzo presente => riolita."""
        print("R6_igneous: aphanitic texture + light color + quartz present -> rhyolite")
        self.declare(Classification(rock='rhyolite'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='volcanic_equivalent_to_granite'),
          NOT(Classification()), salience=1)
    def r7_igneous(self):
        """Igneo + composicion equivalente volcanica al granito => riolita."""
        print("R7_igneous: volcanic equivalent to granite -> rhyolite")
        self.declare(Classification(rock='rhyolite'))

    # Basalto
    @Rule(Origin(type='igneous'),
          Evidence(texture='aphanitic_volcanic'),
          Evidence(color='dark'),
          Evidence(density='high'),
          NOT(Classification()), salience=3)
    def r8_igneous(self):
        """Igneo + textura afanitica volcanica + color oscuro + alta densidad => basalto."""
        print("R8_igneous: aphanitic volcanic texture + dark color + high density -> basalt")
        self.declare(Classification(rock='basalt'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='mafic_ferromagnesian_rich'),
          Evidence(quartz='absent'),
          NOT(Classification()), salience=2)
    def r9_igneous(self):
        """Igneo + composicion mafica ferromagnesiana + sin cuarzo => basalto."""
        print("R9_igneous: mafic ferromagnesian-rich composition + absent quartz -> basalt")
        self.declare(Classification(rock='basalt'))

    # Diorita
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic'),
          Evidence(quartz='absent'),
          Evidence(composition='intermediate_salt_and_pepper'),
          NOT(Classification()), salience=3)
    def r10_igneous(self):
        """Igneo + textura fanerica + sin cuarzo + composicion intermedia sal-pimienta => diorita."""
        print("R10_igneous: phaneritic texture + absent quartz + intermediate salt-and-pepper composition -> diorite")
        self.declare(Classification(rock='diorite'))

    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic'),
          Evidence(color='intermediate'),
          Evidence(dominant_minerals='plagioclase_amphibole'),
          NOT(Classification()), salience=3)
    def r11_igneous(self):
        """Igneo + textura fanerica + color intermedio + plagioclasa-anfibola => diorita."""
        print("R11_igneous: phaneritic texture + intermediate color + plagioclase and amphibole -> diorite")
        self.declare(Classification(rock='diorite'))

    # Andesita
    @Rule(Origin(type='igneous'),
          Evidence(texture='aphanitic_fine_grained'),
          Evidence(color='medium_gray'),
          Evidence(quartz='not_dominant'),
          NOT(Classification()), salience=3)
    def r12_igneous(self):
        """Igneo + textura afanitica grano fino + gris medio + cuarzo no dominante => andesita."""
        print("R12_igneous: fine-grained aphanitic texture + medium-gray color + non-dominant quartz -> andesite")
        self.declare(Classification(rock='andesite'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='intermediate_volcanic'),
          Evidence(phenocrysts='plagioclase_amphibole'),
          NOT(Classification()), salience=2)
    def r13_igneous(self):
        """Igneo + composicion volcanica intermedia + fenocristales plagioclasa-anfibola => andesita."""
        print("R13_igneous: intermediate volcanic composition + plagioclase-amphibole phenocrysts -> andesite")
        self.declare(Classification(rock='andesite'))

    # Gabro
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic'),
          Evidence(color='dark_green_to_black'),
          Evidence(dominant_minerals='ferromagnesian'),
          Evidence(quartz='absent'),
          NOT(Classification()), salience=4)
    def r14_igneous(self):
        """Igneo + textura fanerica + color verde oscuro a negro + ferromagnesianos + sin cuarzo => gabro."""
        print("R14_igneous: phaneritic texture + dark color + ferromagnesian minerals + absent quartz -> gabbro")
        self.declare(Classification(rock='gabbro'))

    @Rule(Origin(type='igneous'),
          Evidence(composition='mafic_plutonic'),
          Evidence(dominant_minerals='pyroxene_calcic_plagioclase'),
          NOT(Classification()), salience=2)
    def r15_igneous(self):
        """Igneo + composicion mafica plutotica + piroxeno-plagioclasa calcica => gabro."""
        print("R15_igneous: mafic plutonic composition + pyroxene and calcic plagioclase -> gabbro")
        self.declare(Classification(rock='gabbro'))

    # Obsidiana
    @Rule(Origin(type='igneous'),
          Evidence(texture='glassy_amorphous'),
          Evidence(cooling='instantaneous'),
          NOT(Classification()), salience=2)
    def r16_igneous(self):
        """Igneo + textura vitrea-amorfa + enfriamiento instantaneo => obsidiana."""
        print("R16_igneous: glassy amorphous texture + instantaneous cooling -> obsidian")
        self.declare(Classification(rock='obsidian'))

    @Rule(Origin(type='igneous'),
          Evidence(fracture='conchoidal_perfect'),
          Evidence(luster='glassy'),
          NOT(Classification()), salience=2)
    def r17_igneous(self):
        """Igneo + fractura concoidal perfecta + lustre vitreo => obsidiana."""
        print("R17_igneous: perfect conchoidal fracture + glassy luster -> obsidian")
        self.declare(Classification(rock='obsidian'))

    # Pegmatita
    @Rule(Origin(type='igneous'),
          Evidence(texture='pegmatitic'),
          Evidence(crystal_size_cm=P(lambda x: x > 2)),
          NOT(Classification()), salience=2)
    def r18_igneous(self):
        """Igneo + textura pegmatitica + cristales > 2 cm => pegmatita."""
        print("R18_igneous: pegmatitic texture + crystals larger than 2 cm -> pegmatite")
        self.declare(Classification(rock='pegmatite'))

    @Rule(Origin(type='igneous'),
          Evidence(giant_crystals='quartz_and_feldspar'),
          Evidence(environment='late_magmatic'),
          NOT(Classification()), salience=2)
    def r19_igneous(self):
        """Igneo + cristales gigantes de cuarzo y feldespato + ambiente tardo-magmatico => pegmatita."""
        print("R19_igneous: giant quartz and feldspar crystals + late magmatic environment -> pegmatite")
        self.declare(Classification(rock='pegmatite'))

    # -----------------------------------------------------------------------
    # NIVEL 3: Recomendacion de uso
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
