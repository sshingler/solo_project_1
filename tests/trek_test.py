import unittest 
from models.trek import Trek
from models.destination import Destination 

class TestTrek(unittest.TestCase):

    def setUp(self):
        self.trek = Trek ("Snowdon Ascent", 14.5, 1, "Reach the summit of Snowdon via Llanberris Path", False, "Test notes 123", "destination_1")
        

    def test_trek_has_name(self): 
        expected = "Snowdon Ascent"
        actual = self.trek.trek_name
        self.assertEqual(expected, actual)

    def test_trek_has_distance(self): 
        expected = 14.5 
        actual = self.trek.trek_distance
        self.assertEqual(expected, actual)

    def test_trek_has_days(self): 
        expected = 1 
        actual = self.trek.trek_days
        self.assertEqual(expected, actual)