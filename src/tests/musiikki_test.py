import unittest
from musiikki import Musiikki

m = Musiikki()

class TestMusiikki(unittest.TestCase):
    def setUp(self):
        pass

    def test_muuta_nuotit_lukuosajonoiksi_muutos_toimii(self):
        nuottikirjaimet = ["c", "D", "A,", "^c", "f'", "f"]
        n = 3
        nuotit_lukuina_lista = m.muuta_nuotit_n_pituisiksi_lukujonoiksi(nuottikirjaimet, n)

        self.assertEqual(nuotit_lukuina_lista,
                         [[16, 6, 1],[6,1,17],[1,17,33],[17,33,21]])

    def test_muuta_luvut_nuoteiksi_muutos_toimii(self):
        nuottiluvut = [1,2,3,39,27,15]
        nuotit_abcna_lista = m.muuta_luvut_nuoteiksi(nuottiluvut)

        self.assertEqual(nuotit_abcna_lista,
                         ["A,","_B,","B,","b'","b","B"])