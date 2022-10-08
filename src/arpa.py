import random
from trie_solmu import TrieSolmu
from trie import Trie
from musiikki import Musiikki

t = Trie()
m = Musiikki()


class Arpa:
    """Luokka arvonnalle.
    """

    def __init__(self):
        pass

    def luo_uutta(self, abc_nuotit, n):
        """Suorittaa tarvittavat metodit, jotta ohjelma luo uutta musiikkia.

        Args:
            abc_nuotit (list): Tuotu kappale listana nuottikirjaimia.
            n (int): Nuottijonon pituus, jonka perusteella uutta musiikkia luodaan.
        """
        nuotit_lukuina_lista = m.muuta_nuotit_luvuiksi(abc_nuotit)
        #print(f"Musa_lukuina_lista: {nuotit_lukuina_lista}")
        n_nuottijonojen_lista = m.n_pituiset_nuottijonot(
            nuotit_lukuina_lista, n)
        #print(f"Nuottijonojen lista: {n_nuottijonojen_lista}")
        t.lisaa_n_nuottijono_triehen(n_nuottijonojen_lista)
        uusi_musiikki_kipale = self.arvo_solmut(n)
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
            #print(f"lista: {lista}")
        eka_solmu = random.choice(lista)
        # print(f"Eka solmu: {eka_solmu}"")
        return eka_solmu

    def arvo_solmut(self, n):
        """Arpoo seuraavat solmut ja valmistaa uuden musiikkikappaleen.
        """
        # n = 3 #!!!!!!!!!!!!!!!
        eka_solmu = self.arvo_eka_solmu()
        nuottijono = []
        musiikkikappale = []
        nuottijono.append(eka_solmu)
        musiikkikappale.append(eka_solmu)

        while len(musiikkikappale) < 100:
            seuraajat = t.palauta_seuraajat(nuottijono)
            #print(f"random-seuraajat: {seuraajat}")

            if seuraajat == False:
                #print(f"loppu {musiikkikappale}")
                return musiikkikappale
            else:
                # print(seuraajat[0])
                seuraava_solmu = random.choice(seuraajat[0])
                if len(nuottijono) < n - 1:
                    nuottijono.append(seuraava_solmu)
                else:
                    nuottijono.pop(0)
                    nuottijono.append(seuraava_solmu)
                #print(f"random-nuottijono: {nuottijono}")

                musiikkikappale.append(seuraava_solmu)

        print(f"lopullinen kipale: {musiikkikappale}")
        return musiikkikappale
