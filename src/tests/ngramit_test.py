import unittest
from trie import Trie

t = Trie()

class TestNgramit(unittest.TestCase):
    def setUp(self):
        self.nuotit = ["c", "d", "e", "f", "g", "a", "h", "c", "d"]
        self.n = 2
        #ngramit = list(zip(*[nuotit[i:] for i in range(n)]))
        #for i in ngramit:
         #   ngram_osat = [" ".join(ngram) for ngram in ngramit]
        
    def test_ngramin_muodostus_toimii(self):
        self.ngram_osat = t.muodosta_ngramit()

        self.assertEqual(self.ngram_osat, 
            ['c d', 'd e', 'e f', 'f g', 'g a', 'a h', 'h c', 'c d'])


    def test_oikea_osien_maara(self):
        osien_maara = t.luo_frekvenssi_lista(self.ngram_osat)

        self.assertEqual(osien_maara, 8)