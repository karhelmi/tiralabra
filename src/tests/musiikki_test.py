import unittest
from musiikki import Musiikki

m = Musiikki()

#Aja testit terminaalissa (juurihakemistossa): "pytest src"
#Kerää testikattavuus: "coverage run --branch -m pytest src" JA raportti komentoriville: coverage report -m
#Ja visuaalinen testikattavuusraportti: coverage html
#Kaikissa src:n alahakemistoissa tulee olla __init__.py -tiedosto Coveragen vuoksi.

class TestMusiikki(unittest.TestCase):
    def setUp(self):
        pass
    
   # def test_nuotit_luvuiksi_muutos_toimii(self):
    #    numerolista = m.muuta_nuotit_luvuiksi()
        
     #   self.assertEqual(numerolista, 
      #      [1, 3, 5, 6, 8, 10, 12, 1, 3])

    def test_n_pituinen_nuottijono_toimii(self):
        nuottijonojen_lista = m.n_pituiset_nuottijonot(3)
        
        self.assertEqual(nuottijonojen_lista,
            [[1, 3, 5], [3, 5, 6], [5, 6, 8], [6, 8, 10], [8, 10, 12], [10, 12, 1], [12, 1, 3]])