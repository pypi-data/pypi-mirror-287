import unittest
from rafnix.model import DiseasePredictor

class TestDiseasePredictor(unittest.TestCase):
    def setUp(self):
        self.predictor = DiseasePredictor('data/sickness_data.csv')
    
    def test_predict(self):
        data = [25, 1, 1, 0, 1, 0, 1, 1, 0, 0]
        result = self.predictor.predict(data)
        self.assertEqual(result, 'Cold')

if __name__ == '__main__':
    unittest.main()
