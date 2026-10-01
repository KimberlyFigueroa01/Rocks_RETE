"""Hechos base que representaran la evidencia y resultados del sistema."""


from experta import KnowledgeEngine, Fact, Rule, OR, AND


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



class RockClassifier(KnowledgeEngine):

    # SEDIMENTARY ROCKS
   

    # --- LEVEL 1: Inference of origin ---

    @Rule(Evidence(texture='clastic'))
    def r1_sedimentary(self):
        print("R1_sedimentary: clastic texture -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    @Rule(Evidence(texture='non_clastic'))
    def r2_sedimentary(self):
        print("R2_sedimentary: non-clastic texture -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    @Rule(AND(
        OR(Evidence(acid_reaction='strong'), Evidence(acid_reaction='weak')),
        Evidence(foliation='no')
    ))
    def r3_sedimentary(self):
        print("R3_sedimentary: acid reaction (strong/weak) + no foliation -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    @Rule(Evidence(plant_remains='yes'))
    def r4_sedimentary(self):
        print("R4_sedimentary: plant remains -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    # --- LEVEL 2: Classification ---

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'), Evidence(clast_size='clay'))
    def r5_sedimentary(self):
        print("R5_sedimentary: sedimentary + clastic + clay -> shale")
        self.declare(Classification(rock='shale'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'), Evidence(clast_size='silt'))
    def r6_sedimentary(self):
        print("R6_sedimentary: sedimentary + clastic + silt -> siltstone")
        self.declare(Classification(rock='siltstone'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'), Evidence(clast_size='sand'))
    def r7_sedimentary(self):
        print("R7_sedimentary: sedimentary + clastic + sand -> sandstone")
        self.declare(Classification(rock='sandstone'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'),
          Evidence(clast_size='gravel'), Evidence(clast_shape='rounded'))
    def r8_sedimentary(self):
        print("R8_sedimentary: sedimentary + clastic + gravel + rounded -> conglomerate")
        self.declare(Classification(rock='conglomerate'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'),
          Evidence(clast_size='gravel'), Evidence(clast_shape='angular'))
    def r9_sedimentary(self):
        print("R9_sedimentary: sedimentary + clastic + gravel + angular -> breccia")
        self.declare(Classification(rock='breccia'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='non_clastic'), Evidence(taste='salty'))
    def r10_sedimentary(self):
        print("R10_sedimentary: sedimentary + non-clastic + salty taste -> halite")
        self.declare(Classification(rock='halite'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='non_clastic'), Evidence(taste='none'))
    def r11_sedimentary(self):
        print("R11_sedimentary: sedimentary + non-clastic + no taste -> gypsum")
        self.declare(Classification(rock='gypsum'))

    @Rule(Origin(type='sedimentary'), Evidence(acid_reaction='strong'))
    def r12_sedimentary(self):
        print("R12_sedimentary: sedimentary + strong acid reaction -> limestone")
        self.declare(Classification(rock='limestone'))

    @Rule(Origin(type='sedimentary'), Evidence(acid_reaction='weak'))
    def r13_sedimentary(self):
        print("R13_sedimentary: sedimentary + weak acid reaction -> dolomite")
        self.declare(Classification(rock='dolomite'))

    @Rule(Origin(type='sedimentary'), Evidence(plant_remains='yes'))
    def r14_sedimentary(self):
        print("R14_sedimentary: sedimentary + plant remains -> coal")
        self.declare(Classification(rock='coal'))

    # --- LEVEL 3: Recommendation ---

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

    

#RUN
if __name__ == '__main__':
    engine = RockClassifier()
    engine.reset()
    engine.declare(Evidence(texture='clastic'))
    engine.declare(Evidence(clast_size='sand'))
    engine.run()

    print("\nFinal facts in working memory:")
    for fact in engine.facts.values():
        print(" -", fact)
