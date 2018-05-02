'''''
aguaclara_research tests.
'''''

import unittest
from aguaclara_research.Environmental_Processes_Analysis import *


class TestEPA(unittest.TestCase):
    '''''
    Test aguaclara_research's Environmental_Processes_Analysis
    '''''

    def test_Hplus_concentration_from_pH(self):
        '''''
        Test function that converts pH to molarity of H+
        '''''
        answer = invpH(8.25)
        self.assertEqual(answer, 5.623413251903491e-09*u.mol/u.L)

        answer = invpH(10)
        self.assertEqual(answer, 1e-10*u.mol/u.L)
