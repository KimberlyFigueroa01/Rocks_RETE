"""Expert system rules for sedimentary rocks.

Three-level structure (RETE):
  - Level 1: origin inference (sedimentary).
  - Level 2: specific rock classification.
  - Level 3: usage recommendation.
"""

from experta import Rule, OR, AND, NOT

from src.facts import Evidence, Origin, Classification, Recommendation


class SedimentaryRules:
    """Mixin containing all classification rules for sedimentary rocks."""

    # -----------------------------------------------------------------------
    # LEVEL 1: Origin inference
    # -----------------------------------------------------------------------

    @Rule(Evidence(texture='clastic'), salience=5)
    def r1_sedimentary(self):
        """Clastic texture => sedimentary origin."""
        print("R1_sedimentary: clastic texture -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    @Rule(Evidence(texture='non_clastic'), salience=5)
    def r2_sedimentary(self):
        """Non-clastic texture => sedimentary origin."""
        print("R2_sedimentary: non-clastic texture -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    # Ambiguous evidence: acid reaction also occurs in metamorphic marble.
    # Low salience + NOT(Origin()): only fires if no higher-confidence
    # rule (texture, plant remains, foliation) already set an origin.
    @Rule(AND(
        OR(Evidence(acid_reaction='strong'), Evidence(acid_reaction='weak')),
        Evidence(foliation='no'),
        NOT(Origin())
    ), salience=1)
    def r3_sedimentary(self):
        """Acid reaction + no foliation + no prior origin => sedimentary origin."""
        print("R3_sedimentary: acid reaction (strong/weak) + no foliation + no prior origin -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    @Rule(Evidence(plant_remains='yes'), salience=5)
    def r4_sedimentary(self):
        """Plant remains => sedimentary origin."""
        print("R4_sedimentary: plant remains -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    # -----------------------------------------------------------------------
    # LEVEL 2: Classification
    # -----------------------------------------------------------------------

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'), Evidence(clast_size='clay'),
          salience=5)
    def r5_sedimentary(self):
        """Sedimentary + clastic + clay => shale."""
        print("R5_sedimentary: sedimentary + clastic + clay -> shale")
        self.declare(Classification(rock='shale'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'), Evidence(clast_size='silt'),
          salience=5)
    def r6_sedimentary(self):
        """Sedimentary + clastic + silt => siltstone."""
        print("R6_sedimentary: sedimentary + clastic + silt -> siltstone")
        self.declare(Classification(rock='siltstone'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'), Evidence(clast_size='sand'),
          salience=5)
    def r7_sedimentary(self):
        """Sedimentary + clastic + sand => sandstone."""
        print("R7_sedimentary: sedimentary + clastic + sand -> sandstone")
        self.declare(Classification(rock='sandstone'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'),
          Evidence(clast_size='gravel'), Evidence(clast_shape='rounded'), salience=5)
    def r8_sedimentary(self):
        """Sedimentary + clastic + gravel + rounded => conglomerate."""
        print("R8_sedimentary: sedimentary + clastic + gravel + rounded -> conglomerate")
        self.declare(Classification(rock='conglomerate'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'),
          Evidence(clast_size='gravel'), Evidence(clast_shape='angular'), salience=5)
    def r9_sedimentary(self):
        """Sedimentary + clastic + gravel + angular => breccia."""
        print("R9_sedimentary: sedimentary + clastic + gravel + angular -> breccia")
        self.declare(Classification(rock='breccia'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='non_clastic'), Evidence(taste='salty'),
          salience=5)
    def r10_sedimentary(self):
        """Sedimentary + non-clastic + salty taste => halite."""
        print("R10_sedimentary: sedimentary + non-clastic + salty taste -> halite")
        self.declare(Classification(rock='halite'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='non_clastic'), Evidence(taste='none'),
          salience=5)
    def r11_sedimentary(self):
        """Sedimentary + non-clastic + no taste => gypsum."""
        print("R11_sedimentary: sedimentary + non-clastic + no taste -> gypsum")
        self.declare(Classification(rock='gypsum'))

    # Ambiguous evidence: strong acid reaction also applies to calcareous sandstone.
    # Low salience + NOT(Classification()): only fires if no prior classification was reached.
    @Rule(Origin(type='sedimentary'), Evidence(acid_reaction='strong'),
          NOT(Classification()), salience=1)
    def r12_sedimentary(self):
        """Sedimentary + strong acid reaction + no prior classification => limestone."""
        print("R12_sedimentary: sedimentary + strong acid reaction + no prior classification -> limestone")
        self.declare(Classification(rock='limestone'))

    @Rule(Origin(type='sedimentary'), Evidence(acid_reaction='weak'),
          NOT(Classification()), salience=1)
    def r13_sedimentary(self):
        """Sedimentary + weak acid reaction + no prior classification => dolomite."""
        print("R13_sedimentary: sedimentary + weak acid reaction + no prior classification -> dolomite")
        self.declare(Classification(rock='dolomite'))

    @Rule(Origin(type='sedimentary'), Evidence(plant_remains='yes'), salience=5)
    def r14_sedimentary(self):
        """Sedimentary + plant remains => coal."""
        print("R14_sedimentary: sedimentary + plant remains -> coal")
        self.declare(Classification(rock='coal'))

    # -----------------------------------------------------------------------
    # LEVEL 3: Usage recommendation
    # -----------------------------------------------------------------------

    @Rule(Classification(rock='shale'))
    def r15_sedimentary(self):
        print("R15_sedimentary: shale -> ceramics and bricks")
        self.declare(Recommendation(use='ceramics_and_bricks'))

    @Rule(Classification(rock='siltstone'))
    def r16_sedimentary(self):
        print("R16_sedimentary: siltstone -> fill material")
        self.declare(Recommendation(use='fill_material'))

    @Rule(Classification(rock='sandstone'))
    def r17_sedimentary(self):
        print("R17_sedimentary: sandstone -> construction, walls, facades")
        self.declare(Recommendation(use='construction_walls_facades'))

    @Rule(Classification(rock='conglomerate'))
    def r18_sedimentary(self):
        print("R18_sedimentary: conglomerate -> construction aggregate")
        self.declare(Recommendation(use='construction_aggregate'))

    @Rule(Classification(rock='breccia'))
    def r19_sedimentary(self):
        print("R19_sedimentary: breccia -> construction aggregate")
        self.declare(Recommendation(use='construction_aggregate'))

    @Rule(Classification(rock='halite'))
    def r20_sedimentary(self):
        print("R20_sedimentary: halite -> salt for industry and consumption")
        self.declare(Recommendation(use='salt_industry_and_consumption'))

    @Rule(Classification(rock='gypsum'))
    def r21_sedimentary(self):
        print("R21_sedimentary: gypsum -> cement and gypsum panels")
        self.declare(Recommendation(use='cement_and_gypsum_panels'))

    @Rule(Classification(rock='limestone'))
    def r22_sedimentary(self):
        print("R22_sedimentary: limestone -> cement and lime")
        self.declare(Recommendation(use='cement_and_lime'))

    @Rule(Classification(rock='dolomite'))
    def r23_sedimentary(self):
        print("R23_sedimentary: dolomite -> industrial and agricultural aggregate")
        self.declare(Recommendation(use='industrial_agricultural_aggregate'))

    @Rule(Classification(rock='coal'))
    def r24_sedimentary(self):
        print("R24_sedimentary: coal -> fuel")
        self.declare(Recommendation(use='fuel'))
