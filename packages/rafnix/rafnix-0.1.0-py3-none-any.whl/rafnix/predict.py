from .model import DiseasePredictor

def predict_disease(data):
    predictor = DiseasePredictor('data/sickness_data.csv')
    return predictor.predict(data)
