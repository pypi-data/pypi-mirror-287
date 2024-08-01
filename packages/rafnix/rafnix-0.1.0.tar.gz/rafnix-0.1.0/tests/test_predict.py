import unittest
from rafnix.predict import predict_disease

class TestPredictDisease(unittest.TestCase):
    def test_predict_disease(self):
        data = [25, 1, 1, 0, 1, 0, 1, 1, 0, 0]
        result = predict_disease(data)
        self.assertEqual(result, 'Cold')

if __name__ == '__main__':
    unittest.main()
