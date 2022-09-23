import unittest
from trie import Trie

t = Trie()

#Aja testit terminaalissa (juurihakemistossa): "pytest src"
#Kerää testikattavuus: "coverage run --branch -m pytest src" JA raportti komentoriville: coverage report -m
#Ja visuaalinen testikattavuusraportti: coverage html
#Kaikissa src:n alahakemistoissa tulee olla __init__.py -tiedosto Coveragen vuoksi.

class TestTrie(unittest.TestCase):
    def setUp(self):
        pass
    
    #def test_nuottijonon_lisäys_triehen_toimii(self):
     #   nuottijonojen_lista = [[1,3,5], [3,5,6],[5,6,8]]
      #  t.lisaa_kaikki_nuottijonot()
        
      #  self.assertEqual(nuottijonojen_lista,
       #     [[1, 3, 5], [3, 5, 6], [5, 6, 8], [6, 8, 10], [8, 10, 12], [10, 12, 1], [12, 1, 3]])