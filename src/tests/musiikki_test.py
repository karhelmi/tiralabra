import unittest
from musiikki import Musiikki

m = Musiikki()

# Aja testit terminaalissa (juurihakemistossa): "pytest src"
# Kerää testikattavuus: "coverage run --branch -m pytest src" JA raportti komentoriville: coverage report -m
# Ja visuaalinen testikattavuusraportti: coverage html
# Kaikissa src:n alahakemistoissa tulee olla __init__.py -tiedosto Coveragen vuoksi.


class TestMusiikki(unittest.TestCase):
    def setUp(self):
        pass

    def test_nuotit_luvuiksi_muutos_toimii(self):
        nuottikirjaimet = ["c", "cis", "d", "dis", "e", "f"]
        numerolista = m.muuta_nuotit_luvuiksi(nuottikirjaimet)

        self.assertEqual(numerolista,
                         [1, 2, 3, 4, 5, 6])

    def test_n_pituinen_nuottijono_toimii(self):
        nuotit_lukuina_lista = [1, 2, 3, 4, 5, 6]
        n = 3

        n_pituiset_nuottijonot = m.n_pituiset_nuottijonot(
            nuotit_lukuina_lista, n)

        self.assertEqual(n_pituiset_nuottijonot,
                         [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
