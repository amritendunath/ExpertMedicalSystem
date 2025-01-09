class Base:
    def __init__(self):
        self.conclusion = [
             "Heart Failure", "Cardiomyopathy", "Angina", 
            "Coronary Artery Disease", "Tachycardia", "Ventricular Tachycardia"
        ]
        self.variables_list = [
            "Rapid/Irregular Heart Beats or Heart Palpitations", "Chest Pain",
            "Persistent Shortness of Breath", "Fatigue", "Dizziness", "Lightheadedness", "Weakness", 
            "Unexplained Sweating", "Fainting", "Weight Gain", "Edema", "Swollen Stomach", "Confusion", 
            "Chest Tightness", "Vomiting", "Restlessness", "Heart Attack", "Nausea", "Tightness in Neck", 
            "Cardiac Arrest", "Lung Congestion"
        ]
        self.symptoms_combination = [
            [0, 1, 6], [0, 12], [0, 20], [0, 10], [0, 11], [0, 18], [0, 19],
            [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 10], [1, 11], [1, 13],
            [1, 14], [1, 15], [1, 18], [1, 19], [1, 3, 7], [1, 3, 8], [1, 20],
            [1, 5, 6], [1, 5, 7], [1, 5, 9], [1, 12], [1, 6, 9], [1, 6, 7], [1, 6, 8],
            [1, 7], [1, 8, 9], [0, 16], [0, 17], [0, 7], [0, 8, 9], [1, 4, 7], [1, 4, 9]
        ]