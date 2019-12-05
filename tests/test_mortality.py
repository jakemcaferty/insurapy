import unittest
import numpy as np

from insurapy import mortality as mort

class MortalityTest(unittest.TestCase):

    def setUp(self):
        self.rates = np.arange(10) * 0.1
        self.table = mort.MortalityTable(self.rates)
        self.u_table = mort.MortalityTable(self.rates)

    def test_ages(self):
        for i, age in enumerate(self.table.ages):
            self.assertEqual(age, i)

    def test_qx_px(self):
        self.assertEqual(self.table.qx[0], 0)
        self.assertEqual(self.table.px[0], 1)

    def test_qx_update(self):
        self.u_table.qx[0] = 0.5
        self.assertEqual(self.u_table.qx[0], 0.5)
        self.assertEqual(self.u_table.px[0], 0.5)

    def test_nqx(self):
        self.assertEqual(self.table.nqx(3, 3), 0.79)

    def test_npx(self):
        self.assertEqual(self.table.npx(3, 3), 0.21)
    
if __name__ == "__main__":
    unittest.main()