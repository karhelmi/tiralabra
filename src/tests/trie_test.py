import unittest
from trie import Trie
from trie_solmu import TrieSolmu

t = Trie()

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.testi_juurisolmu = TrieSolmu("")
        testi_solmu = self.testi_juurisolmu
        nuottijonojen_lista = [[1,3,5], [1,4,5],[1,6,8]]
        for nuottijono in nuottijonojen_lista:
            for nuotti in nuottijono:
                uusi_testi_solmu = TrieSolmu(nuotti)
                testi_solmu.lapsisolmut[nuotti] = uusi_testi_solmu
                uusi_testi_solmu.nuottijonon_frekvenssi += 1
                testi_solmu = uusi_testi_solmu

    def test_nuottijonon_lisäys_triehen_toimii(self):
        pass
        #nuottijonojen_lista = [[1,3,5], [1,4,5],[1,6,8]]
        #ykkosen_lapsisolmut = []
        #t.lisaa_n_nuottijonot_triehen(nuottijonojen_lista)
        #for key, value in t.juuri.lapsisolmut.items():
        #    if key == 1:
        #        ykkosen_lapsisolmut = value #??? Miksi tämä ei ole lapsisolmut listana???

        #self.assertEqual(ykkosen_lapsisolmut,
        #    [3,4,6])