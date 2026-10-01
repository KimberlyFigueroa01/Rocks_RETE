"""Motor de inferencia del sistema experto."""


from experta import KnowledgeEngine, Rule, OR, AND, NOT, P, L
from src.facts import Evidence, Origin, Classification, Recommendation


# ---------------------------------------------------------------------------
# Expert system engine
# ---------------------------------------------------------------------------

class RockClassifier(KnowledgeEngine):

    
    # SEDIMENTARY ROCKS (confirmed)
    

    # --- LEVEL 1: Inference of origin ---

    @Rule(Evidence(texture='clastic'), salience=5)
    def r1_sedimentary(self):
        print("R1_sedimentary: clastic texture -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    @Rule(Evidence(texture='non_clastic'), salience=5)
    def r2_sedimentary(self):
        print("R2_sedimentary: non-clastic texture -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    # Ambiguous evidence: acid reaction also occurs in metamorphic marble.
    # Low salience + NOT(Origin()) guard: only fires if no higher-confidence
    # rule (texture, plant remains, foliation) already set an origin.
    @Rule(AND(
        OR(Evidence(acid_reaction='strong'), Evidence(acid_reaction='weak')),
        Evidence(foliation='no'),
        NOT(Origin())
    ), salience=1)
    def r3_sedimentary(self):
        print("R3_sedimentary: acid reaction (strong/weak) + no foliation + no prior origin -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    @Rule(Evidence(plant_remains='yes'), salience=5)
    def r4_sedimentary(self):
        print("R4_sedimentary: plant remains -> sedimentary origin")
        self.declare(Origin(type='sedimentary'))

    # --- LEVEL 2: Classification ---

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'), Evidence(clast_size='clay'),
          salience=5)
    def r5_sedimentary(self):
        print("R5_sedimentary: sedimentary + clastic + clay -> shale")
        self.declare(Classification(rock='shale'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'), Evidence(clast_size='silt'),
          salience=5)
    def r6_sedimentary(self):
        print("R6_sedimentary: sedimentary + clastic + silt -> siltstone")
        self.declare(Classification(rock='siltstone'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'), Evidence(clast_size='sand'),
          salience=5)
    def r7_sedimentary(self):
        print("R7_sedimentary: sedimentary + clastic + sand -> sandstone")
        self.declare(Classification(rock='sandstone'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'),
          Evidence(clast_size='gravel'), Evidence(clast_shape='rounded'), salience=5)
    def r8_sedimentary(self):
        print("R8_sedimentary: sedimentary + clastic + gravel + rounded -> conglomerate")
        self.declare(Classification(rock='conglomerate'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='clastic'),
          Evidence(clast_size='gravel'), Evidence(clast_shape='angular'), salience=5)
    def r9_sedimentary(self):
        print("R9_sedimentary: sedimentary + clastic + gravel + angular -> breccia")
        self.declare(Classification(rock='breccia'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='non_clastic'), Evidence(taste='salty'),
          salience=5)
    def r10_sedimentary(self):
        print("R10_sedimentary: sedimentary + non-clastic + salty taste -> halite")
        self.declare(Classification(rock='halite'))

    @Rule(Origin(type='sedimentary'), Evidence(texture='non_clastic'), Evidence(taste='none'),
          salience=5)
    def r11_sedimentary(self):
        print("R11_sedimentary: sedimentary + non-clastic + no taste -> gypsum")
        self.declare(Classification(rock='gypsum'))

    # Ambiguous evidence: strong acid reaction also fits a calcareous sandstone
    # (clastic + sand + strong reaction) and, at the origin level, marble.
    # Low salience + NOT(Classification()) guard: only fires if no more
    # specific classification (e.g. sandstone) was already reached.
    @Rule(Origin(type='sedimentary'), Evidence(acid_reaction='strong'),
          NOT(Classification()), salience=1)
    def r12_sedimentary(self):
        print("R12_sedimentary: sedimentary + strong acid reaction + no prior classification -> limestone")
        self.declare(Classification(rock='limestone'))

    @Rule(Origin(type='sedimentary'), Evidence(acid_reaction='weak'),
          NOT(Classification()), salience=1)
    def r13_sedimentary(self):
        print("R13_sedimentary: sedimentary + weak acid reaction + no prior classification -> dolomite")
        self.declare(Classification(rock='dolomite'))

    @Rule(Origin(type='sedimentary'), Evidence(plant_remains='yes'), salience=5)
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

     # ==================================================================
    # ROCAS IGNEAS
    # ==================================================================

    @Rule(Evidence(fractional_crystallization='yes'),
          Evidence(fossils = 'no'),
          Evidence(stratification = 'no'),
          NOT(Origin()), salience=3)
    def R1_igneas(self):
        print("R1_igneas: fractional crystallization -> igneous origin")
        self.declare(Origin(type='igneous'))

    @Rule(Evidence(crystalline_mosaic_texture='yes'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          NOT(Origin()), salience=3)
    def R2_igneas(self):
        print("R2_igneas: crystalline mosaic texture -> igneous origin")
        self.declare(Origin(type='igneous'))
 
    # Adicion: permite que la obsidiana (vidrio, sin cristales) llegue al Nivel 2
    @Rule(Evidence(texture='glassy_amorphous'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          NOT(Origin()), salience=3)
    def R3_igneas(self):
        print("R3_igneas: glassy amorphous texture -> igneous origin")
        self.declare(Origin(type='igneous'))
 
    # ---- Nivel 2: clasificacion ---------------------------------------
    # Granito
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic_porphyritic'),
          Evidence(color='light'),
          Evidence(quartz='rich'),
          NOT(Classification()), salience=3)
    def R4_igneas(self):
        print("R4_igneas: igneous + phaneritic porphyritic texture + light color + rich quartz -> granite")
        self.declare(Classification(rock='granite'))
 
    @Rule(Origin(type='igneous'),
          Evidence(composition='felsic'),
          NOT(Classification()), salience=1)
    def R5_igneas(self):
        print("R5_igneas: felsic composition -> granite")
        self.declare(Classification(rock='granite'))
 
    # Riolita
    @Rule(Origin(type='igneous'),
          Evidence(texture='aphanitic'),
          Evidence(color='light'),
          Evidence(quartz='present'),
          NOT(Classification()), salience=3)
    def R6_igneas(self):
        print("R6_igneas: aphanitic texture + light color + quartz present -> rhyolite")
        self.declare(Classification(rock='rhyolite'))
 
    @Rule(Origin(type='igneous'),
          Evidence(composition='volcanic_equivalent_to_granite'),
          NOT(Classification()), salience=1)
    def R7_igneas(self):
        print("R7_igneas: volcanic equivalent to granite -> rhyolite")
        self.declare(Classification(rock='rhyolite'))
 
    # Basalto
    @Rule(Origin(type='igneous'),
          Evidence(texture='aphanitic_volcanic'),
          Evidence(color='dark'),
          Evidence(density='high'),
          NOT(Classification()), salience=3)
    def R8_igneas(self):
        print("R8_igneas: aphanitic volcanic texture + dark color + high density -> basalt")
        self.declare(Classification(rock='basalt'))
 
    @Rule(Origin(type='igneous'),
          Evidence(composition='mafic_ferromagnesian_rich'),
          Evidence(quartz='absent'),
          NOT(Classification()), salience=2)
    def R9_igneas(self):
        print("R9_igneas: mafic ferromagnesian-rich composition + absent quartz -> basalt")
        self.declare(Classification(rock='basalt'))
 
    # Diorita
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic'),
          Evidence(quartz='absent'),
          Evidence(composition='intermediate_salt_and_pepper'),
          NOT(Classification()), salience=3)
    def R10_igneas(self):
        print("R10_igneas: phaneritic texture + absent quartz + intermediate salt-and-pepper composition -> diorite")
        self.declare(Classification(rock='diorite'))
 
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic'),
          Evidence(color='intermediate'),
          Evidence(dominant_minerals='plagioclase_amphibole'),
          NOT(Classification()), salience=3)
    def R11_igneas(self):
        print("R11_igneas: phaneritic texture + intermediate color + plagioclase and amphibole -> diorite")
        self.declare(Classification(rock='diorite'))
 
    # Andesita
    @Rule(Origin(type='igneous'),
          Evidence(texture='aphanitic_fine_grained'),
          Evidence(color='medium_gray'),
          Evidence(quartz='not_dominant'),
          NOT(Classification()), salience=3)
    def R12_igneas(self):
        print("R12_igneas: fine-grained aphanitic texture + medium-gray color + non-dominant quartz -> andesite")
        self.declare(Classification(rock='andesite'))
 
    @Rule(Origin(type='igneous'),
          Evidence(composition='intermediate_volcanic'),
          Evidence(phenocrysts='plagioclase_amphibole'),
          NOT(Classification()), salience=2)
    def R13_igneas(self):
        print("R13_igneas: intermediate volcanic composition + plagioclase-amphibole phenocrysts -> andesite")
        self.declare(Classification(rock='andesite'))
 
    # Gabro
    @Rule(Origin(type='igneous'),
          Evidence(texture='phaneritic'),
          Evidence(color='dark_green_to_black'),
          Evidence(dominant_minerals='ferromagnesian'),
          Evidence(quartz='absent'),
          NOT(Classification()), salience=4)
    def R14_igneas(self):
        print("R14_igneas: phaneritic texture + dark color + ferromagnesian minerals + absent quartz -> gabbro")
        self.declare(Classification(rock='gabbro'))
 
    @Rule(Origin(type='igneous'),
          Evidence(composition='mafic_plutonic'),
          Evidence(dominant_minerals='pyroxene_calcic_plagioclase'),
          NOT(Classification()), salience=2)
    def R15_igneas(self):
        print("R15_igneas: mafic plutonic composition + pyroxene and calcic plagioclase -> gabbro")
        self.declare(Classification(rock='gabbro'))
 
    # Obsidiana
    @Rule(Origin(type='igneous'),
          Evidence(texture='glassy_amorphous'),
          Evidence(cooling='instantaneous'),
          NOT(Classification()), salience=2)
    def R16_igneas(self):
        print("R16_igneas: glassy amorphous texture + instantaneous cooling -> obsidian")
        self.declare(Classification(rock='obsidian'))
 
    @Rule(Origin(type='igneous'),
          Evidence(fracture='conchoidal_perfect'),
          Evidence(luster='glassy'),
          NOT(Classification()), salience=2)
    def R17_igneas(self):
        print("R17_igneas: perfect conchoidal fracture + glassy luster -> obsidian")
        self.declare(Classification(rock='obsidian'))
 
    # Pegmatita
    @Rule(Origin(type='igneous'),
          Evidence(texture='pegmatitic'),
          Evidence(crystal_size_cm=P(lambda x: x > 2)),
          NOT(Classification()), salience=2)
    def R18_igneas(self):
        print("R18_igneas: pegmatitic texture + crystals larger than 2 cm -> pegmatite")
        self.declare(Classification(rock='pegmatite'))
 
    @Rule(Origin(type='igneous'),
          Evidence(giant_crystals='quartz_and_feldspar'),
          Evidence(environment='late_magmatic'),
          NOT(Classification()), salience=2)
    def R19_igneas(self):
        print("R19_igneas: giant quartz and feldspar crystals + late magmatic environment -> pegmatite")
        self.declare(Classification(rock='pegmatite'))
 
    # ---- Nivel 3: recomendacion ---------------------------------------
    @Rule(Origin(type='igneous'), Classification(rock='basalt'))
    def R20_igneas(self):
        print("R20_igneas: basalt -> crushed-stone aggregate recommendation")
        self.declare(Recommendation(use=(
            'Crushed stone aggregate for high-strength concrete and asphalt '
            'pavements (homogeneous, isotropic, uniform stress distribution)')))
 
    @Rule(Origin(type='igneous'), Classification(rock='granite'))
    def R21_igneas(self):
        print("R21_igneas: granite -> ornamental and structural stone recommendation")
        self.declare(Recommendation(use=(
            'Ornamental slabs, paving stones, building cladding and heavy '
            'foundation blocks (high hardness, low porosity, high compressive '
            'strength)')))

    # ==================================================================
    # ROCAS METAMORFICAS
    # ==================================================================

     # ---- Nivel 1: origen ----------------------------------------------
    @Rule(Evidence(foliation='yes'),
          Evidence(directional_stress='yes'),
          NOT(Origin()), salience=2)
    def R1_metamorficas(self):
        print("R1_metamorficas: foliation + directional stress -> metamorphic origin")
        self.declare(Origin(type='metamorphic'))
 
    @Rule(Evidence(foliation='no'),
          Evidence(solid_state_recrystallization='yes'),
          Evidence(fossils='no'),
          Evidence(stratification='no'),
          Evidence(fractional_crystallization='no'),
          NOT(Origin()), salience=5)
    def R2_metamorficas(self):
        print("R2_metamorficas: solid-state recrystallization without sedimentary or igneous features -> metamorphic origin")
        self.declare(Origin(type='metamorphic'))
 
    # ---- Nivel 2: clasificacion ---------------------------------------
    # Pizarra
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='slaty_foliation'),
          Evidence(grain_size='very_fine'),
          Evidence(protolith='shale'),
          NOT(Classification()), salience=3)
    def R3_metamorficas(self):
        print("R3_metamorficas: slaty foliation + very fine grain + shale protolith -> slate")
        self.declare(Classification(rock='slate'))
 
    # Marmol
    @Rule(Origin(type='metamorphic'),
          Evidence(foliation='no'),
          Evidence(hcl_reaction='effervescent'),
          Evidence(protolith='limestone'),
          NOT(Classification()), salience=3)
    def R4_metamorficas(self):
        print("R4_metamorficas: no foliation + effervescent HCl reaction + limestone protolith -> marble")
        self.declare(Classification(rock='marble'))
 
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='massive_saccharoidal_recrystallization'),
          Evidence(hcl_reaction='effervescent'),
          NOT(Classification()), salience=2)
    def R5_metamorficas(self):
        print("R5_metamorficas: massive saccharoidal recrystallization + effervescent HCl reaction -> marble")
        self.declare(Classification(rock='marble'))
 
    # Gneis
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='foliated_medium_to_coarse'),
          Evidence(banding='alternating_light_quartzofeldspathic_and_dark_mafic'),
          NOT(Classification()), salience=2)
    def R6_metamorficas(self):
        print("R6_metamorficas: medium-to-coarse foliation + alternating bands -> gneiss")
        self.declare(Classification(rock='gneiss'))
 
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='gneissic_banding'),
          Evidence(metamorphism_grade='intense'),
          Evidence(protolith=L('granitic') | L('sedimentary')),
          NOT(Classification()), salience=3)
    def R7_metamorficas(self):
        print("R7_metamorficas: gneissic banding + intense metamorphism -> gneiss")
        self.declare(Classification(rock='gneiss'))
 
    # Cuarcita
    @Rule(Origin(type='metamorphic'),
          Evidence(texture='massive_non_foliated'),
          Evidence(mineralogy='recrystallized_interlocking_quartz'),
          Evidence(mohs_hardness=P(lambda x: x >= 6.5)),
          NOT(Classification()), salience=3)
    def R8_metamorficas(self):
        print("R8_metamorficas: massive non-foliated texture + interlocking quartz + hardness >= 6.5 -> quartzite")
        self.declare(Classification(rock='quartzite'))
 
    @Rule(Origin(type='metamorphic'),
          Evidence(protolith='quartz_arenite'),
          Evidence(metamorphism_type=L('thermal') | L('regional')),
          NOT(Classification()), salience=2)
    def R9_metamorficas(self):
        print("R9_metamorficas: quartz-arenite protolith + thermal or regional metamorphism -> quartzite")
        self.declare(Classification(rock='quartzite'))
 
    # ---- Nivel 3: recomendacion ---------------------------------------
    @Rule(Origin(type='metamorphic'), Classification(rock='slate'))
    def R10_metamorficas(self):
        print("R10_metamorficas: slate -> waterproof roofing and cladding recommendation")
        self.declare(Recommendation(use=(
            'Waterproof roofing tiles, waterproofing panels and facade '
            'cladding (smooth cleavage planes, very low permeability)')))
 
    @Rule(Origin(type='metamorphic'), Classification(rock='marble'))
    def R11_metamorficas(self):
        print("R11_metamorficas: marble -> architectural finishes and decorative stone recommendation")
        self.declare(Recommendation(use=(
            'Interior architectural finishes, decorative cladding, floor '
            'slabs and monumental elements (workability, mirror-like polish, '
            'aesthetics)')))

RockClassificationEngine = RockClassifier

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

