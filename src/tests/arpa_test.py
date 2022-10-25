import unittest
from arpa import Arpa

a = Arpa(3)

class TestArpa(unittest.TestCase):
    def setUp(self):
        pass

    def test_uuden_musiikin_luonti_pituus_halutun_rajoissa(self):
        abc_nuotit = ["c", "D", "A,", "^c", "f'", "f"]
        pituus = 10
        luotu_musiikki_kappale = a.luo_uutta(abc_nuotit, pituus)

        self.assertLessEqual(len(luotu_musiikki_kappale),
                         10)