from trie_solmu import TrieSolmu
from musiikki import Musiikki

m = Musiikki()

class Trie:
    """Luokka trie-tietorakenteelle.
    """

    def __init__(self):
        self.juuri = TrieSolmu("")


    def lisaa_kaikki_nuottijonot(self):
        """Hakee koko nuottijonojen listan ja lisää ne n-pituinen nuottijono
           kerrallaan trie-rakenteeseen.
        """
        
        nuottijonojen_lista = m.n_pituiset_nuottijonot(3)
        #print(f"nuottijonojen lista: {nuottijonojen_lista}")
        for nuottijono in nuottijonojen_lista:
            #print(f"lisää nuottijono {nuottijono}")
            self.lisaa_nuottijono(nuottijono)

    def lisaa_nuottijono(self, nuottijono):
        """Lisätään n-pituinen nuottijono trie-tietorakenteeseen.

        Args:
            nuottijono (list): n-pituinen nuottijono
        """

        solmu = self.juuri
        for nuotti in nuottijono:
            if nuotti in solmu.lapsisolmut:
                solmu = solmu.lapsisolmut[nuotti] #määrittää seuraavan solmun kyseiseksi nuotiksi
                print(f"on jo: {solmu}")
            else:
                uusi_solmu = TrieSolmu(nuotti)
                solmu.lapsisolmut[nuotti] = uusi_solmu
                print(f"solmun lapsisolmut: {solmu.lapsisolmut}")
                solmu = uusi_solmu
                #print(f"uusi_solmu: {solmu}")

        solmu.vika_nuotti = True

        solmu.nuottijonon_frekvenssi += 1
#        print(f"frekvenssi: {solmu.nuottijonon_frekvenssi}")
#        print(f"nuotti: {solmu.nuotti}")
#        print(f"lapsisolmut: {solmu.lapsisolmut}")
#        print(f"vika_nuotti: {solmu.vika_nuotti}")
        return solmu.lapsisolmut