import random
from trie import Trie
from musiikki import Musiikki

t = Trie()
m = Musiikki()

class Arpa:
    """Luokka arvonnalle.
    """

    def __init__(self):
        pass

    def luo_uutta(self, abc_nuotit, n, pituus):
        """Suorittaa tarvittavat metodit, jotta ohjelma luo uutta musiikkia.

        Args:
            abc_nuotit (list): Tuotu kappale listana nuottikirjaimia.
            n (int): Nuottijonon pituus, jonka perusteella uutta musiikkia luodaan.
        """
        nuottijonojen_lista = m.muuta_nuotit_n_pituisiksi_lukujonoiksi(abc_nuotit, n)
        t.lisaa_n_nuottijonot_triehen(nuottijonojen_lista)
        uusi_musiikki_kipale = self.arvo_solmut(n, pituus)
        return uusi_musiikki_kipale

    def arvo_eka_solmu(self):
        """Arpoo juurisolmun lapsisolmuista ensimmäisen solmun eli nuotin.

        Returns:
            int: Palauttaa arvotun ensimmäisen nuotin numerona.
        """
        solmu = t.juuri
        lista = []
        for key in solmu.lapsisolmut:
            lista.append(key)
        eka_solmu = random.choice(lista)
        return eka_solmu

    def arvo_solmut(self, n, pituus):
        """Arpoo seuraavat solmut ja valmistaa uuden musiikkikappaleen.
        """
        eka_solmu = self.arvo_eka_solmu()
        nuottijono = []
        musiikkikappale = []
        nuottijono.append(eka_solmu)
        musiikkikappale.append(eka_solmu)

        while len(musiikkikappale) < pituus:
            seuraajat = t.palauta_seuraajat(nuottijono)

            if seuraajat is False:
                #print(f"loppu {musiikkikappale}")
                return musiikkikappale
            seuraava_solmu = random.choice(seuraajat[0])
            if len(nuottijono) < n - 1:
                nuottijono.append(seuraava_solmu)
            else:
                nuottijono.pop(0)
                nuottijono.append(seuraava_solmu)

            musiikkikappale.append(seuraava_solmu)

        print(f"lopullinen kipale: {musiikkikappale}")
        return musiikkikappale
        