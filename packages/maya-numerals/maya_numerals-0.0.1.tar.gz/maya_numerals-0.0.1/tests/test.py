import unittest
import maya_numerals
from maya_numerals import mn


class TestClient(unittest.TestCase):

    sample_numbers = [39, 4285, 16125]

    import importlib.resources
    import os

    def test_twoDigits(self):
        assert maya_numerals.mn.convert(TestClient.sample_numbers[0]) == ['ᴮ9', 'ᴮ1']

    def test_fourDigits(self):
        assert maya_numerals.mn.convert(TestClient.sample_numbers[1]) == ['ᴮ5', 'ᴮE', 'ᴮA']
    
    def test_fiveDigits(self):
        assert maya_numerals.mn.convert(TestClient.sample_numbers[2]) == ['ᴮ5', 'ᴮ6', 'ᴮ0', 'ᴮ2']


if __name__ == "__main__":
     unittest.main()