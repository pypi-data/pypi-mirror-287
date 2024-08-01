import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

class DiseasePredictor:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.model = RandomForestClassifier(random_state=42)
        self.scaler = StandardScaler()
        self._prepare_data()
    
    def _prepare_data(self):
        features = self.df.drop('illness', axis=1)
        labels = self.df['illness']
        scaled_features = self.scaler.fit_transform(features)
        X_train, X_test, y_train, y_test = train_test_split(scaled_features, labels, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
    
    def predict(self, data):
        scaled_data = self.scaler.transform([data])
        return self.model.predict(scaled_data)[0]
