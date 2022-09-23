import unittest
from trie import Trie

t = Trie()

#Aja testit terminaalissa (juurihakemistossa): "pytest src"
#Kerää testikattavuus: "coverage run --branch -m pytest src" JA raportti komentoriville: coverage report -m
#Ja visuaalinen testikattavuusraportti: coverage html
#Kaikissa src:n alahakemistoissa tulee olla __init__.py -tiedosto Coveragen vuoksi.

#class TestTrie(unittest.TestCase):
 #   def setUp(self):
  #      self.nuotit = ["c", "d", "e", "f", "g", "a", "h", "c", "d"]
   #     self.n = 2
    #    ngramit = list(zip(*[self.nuotit[i:] for i in range(self.n)]))
     #   for i in ngramit:
      #      self.ngram_osat = [" ".join(ngram) for ngram in ngramit]
        
    #def test_ngramin_muodostus_toimii(self):
     #   self.ngram_osat = t.muodosta_ngramit()

     #   self.assertEqual(self.ngram_osat, 
      #      ['c d', 'd e', 'e f', 'f g', 'g a', 'a h', 'h c', 'c d'])

   # def test_oikea_osien_maara(self):
    #    osien_maara = t.luo_frekvenssi_lista()
     #   maara = 0
      #  for value in osien_maara.values():
       #     maara += value

        #self.assertEqual(maara, 8)