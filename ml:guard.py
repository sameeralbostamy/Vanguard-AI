from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

class AKIGuard:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
    
    def train_on_synthetic_data(self):
        """Generates 2k patients and trains the model."""
        n = 2000
        age = np.random.randint(20, 90, n)
        weight = np.random.uniform(50, 120, n)
        creatinine = np.random.uniform(0.5, 3.0, n)
        dose = weight * 15
        
        # Simple rule for synthetic labels: 
        # High Risk if Dose/Weight ratio is high but Kidneys are slow
        crcl = ((140 - age) * weight) / (72 * creatinine)
        aki_risk = np.where((dose / crcl) > 12, 1, 0)
        
        X = pd.DataFrame({'age': age, 'weight': weight, 'creatinine': creatinine, 'dose': dose})
        self.model.fit(X, aki_risk)
        print("Safety Guard model trained on 2,000 synthetic patient records.")

    def predict_risk(self, age, weight, creatinine, dose):
        input_data = pd.DataFrame([[age, weight, creatinine, dose]], 
                                  columns=['age', 'weight', 'creatinine', 'dose'])
        return self.model.predict_proba(input_data)[0][1]