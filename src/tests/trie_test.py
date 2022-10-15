import unittest
from trie import Trie
from trie_solmu import TrieSolmu

t = Trie()

# Aja testit terminaalissa (juurihakemistossa): "pytest src"
# Kerää testikattavuus: "coverage run --branch -m pytest src" JA raportti komentoriville: coverage report -m
# Ja visuaalinen testikattavuusraportti: coverage html
# Kaikissa src:n alahakemistoissa tulee olla __init__.py -tiedosto Coveragen vuoksi.


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.testi_solmu = TrieSolmu("")

    def test_nuottijonon_lisäys_triehen_toimii(self):
        nuottijonojen_lista = [[1,3,5], [1,4,5],[1,6,8]]
        ykkosen_lapsisolmut = []
        t.lisaa_n_nuottijonot_triehen(nuottijonojen_lista)
        self.testi_solmu[0].palauta_lapsisolmut()

        self.assertEqual(ykkosen_lapsisolmut,
            [3,4,6])
