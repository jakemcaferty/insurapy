import unittest
import numpy as np

from insurapy import mortality as mort

class MortalityTest(unittest.TestCase):

    def setUp(self):
        self.rates = np.arange(10) * 0.1
        self.u_table = mort.MortalityTable(self.rates)
        self.c_table = mort.MortalityTable(self.rates, force='c')

    def test_ages(self):
        for i, age in enumerate(self.u_table.ages):
            self.assertEqual(age, i)

    def test_qx_px(self):
        self.assertEqual(self.u_table.qx[0], 0)
        self.assertEqual(self.u_table.px[0], 1)

    def test_nqx_u(self):
        self.assertEqual(self.u_table.nqx(3, 3), 0.79)
        self.assertEqual(self.u_table.nqx(0, 3), 0)
        self.assertAlmostEqual(self.u_table.nqx(3.5, 3), .853, 4)

    def test_npx_u(self):
        self.assertEqual(self.u_table.npx(3, 3), 0.21)
        self.assertEqual(self.u_table.npx(0, 3), 1)
        self.assertAlmostEqual(self.u_table.npx(3.5, 3), .147, 4)

    def test_nqx_c(self):
        self.assertEqual(self.c_table.nqx(3, 3), 0.79)
        self.assertEqual(self.c_table.nqx(0, 3), 0)
        self.assertAlmostEqual(self.c_table.nqx(3.5, 3), .8672, 4)

    def test_npx_c(self):
        self.assertEqual(self.c_table.npx(3, 3), 0.21)
        self.assertEqual(self.c_table.npx(0, 3), 1)
        self.assertAlmostEqual(self.c_table.npx(3.5, 3), .1328, 4)
        
    
if __name__ == "__main__":
    unittest.main()