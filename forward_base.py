
class ForwardChain:
    def _init_(self):
        self.clause_variable_list = ["High blood pressure and progression of disease",
                                                     "Fluid Collection",
                                                     "Inflammation",
                                                     "Poor blood circulation",
                                                     "Narrow blood vessels and chest pain",
                                                     "Elevated Cholesterol",
                                                     "Blood Clotting",
                                                     "Increased Heart Rate",
                                                     "Blockage in blood vessels"]
        self.treatment_list=["ACE INHIBITOR / ARB BLOCKERS",
                                               "DIURETICS / ALDOSTERONE ANTAGONISTS"
                                               "CORTICOSTEROIDS",
                                               "ACE INHIBITOR/ ANGIOTENSIN II RECEPTOR BLOCKERS",
                                               "NITRATES",
                                               "STATIN",
                                               "VAGAL MANEUVER",
                                               "CLOT PREVENTING DRUGS ( CLOPIDOGREL, TICAGRELOR)/ ASPIRIN",
                                               "ANTI-ARRYTHMIC DRUGS",
                                               "NITRATES/ OPEN HEART SURGERY"]                           
        self.diagnosis_list=["Heart Failure", "Cardiomyopathy", "Angina",
                            "Coronary Artery Disease", "Tachycardia", "Ventricular Tachycardia"]
     
        self.diagnosis_ailment = [{0, {0, 1}}, {1, {2, 3}}, {2, {4, 5, 6}}, {3, {0, 6}}, 
                         {4, {6, 7}}, {7, {7, 8}}]
        self.ailment_condition = {
            {"HIGH", "COLLECTED"},
            {"INFLAMED", "REDUCED"},
            {"NARROWED", "ELEVATED", "CLOT"},
            {"HIGH", "CLOT"},{"INCREASED", "CLOT"},
            {"INCREASED", "BLOCKAGE"}}