import unittest 
from models.trek import Trek
from models.destination import Destination 

class TestDestination(unittest.TestCase):

    def setUp(self):
        self.destination = Destination ("Snowdonia National Park", "United Kingdom", "Europe")
        

    def test_destination_has_name(self): 
        expected = "Snowdonia National Park"
        actual = self.destination.destination_name 
        self.assertEqual(expected, actual)

    