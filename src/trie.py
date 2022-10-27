from trie_solmu import TrieSolmu

class Trie:
    """Luokka trie-tietorakenteelle.
    """

    def __init__(self):
        self.juuri = TrieSolmu("")

    def lisaa_n_nuottijonot_triehen(self, n_nuottijonojen_lista: list):
        """Lisää n-pituisen nuottijonon trie-rakenteeseen.

        Args:
            n_nuottijonojen_lista: Lista, jossa kaikki
            musiikkikappaleen n-pituiset nuottijonot.
        """
        for nuottijono in n_nuottijonojen_lista:
            solmu = self.juuri

            for nuotti in nuottijono:
                if nuotti in solmu.lapsisolmut:
                    solmu.nuottijonon_frekvenssi += 1
                    solmu = solmu.lapsisolmut[nuotti] #Määrittää seuraavan solmun kyseiseksi nuotiksi
                else:
                    uusi_solmu = TrieSolmu(nuotti)
                    solmu.lapsisolmut[nuotti] = uusi_solmu
                    uusi_solmu.nuottijonon_frekvenssi += 1
                    solmu = uusi_solmu

    def palauta_seuraajat(self, nuottijono: list):
        """Metodi etsii annetun nuottijonon viimeisen nuotin lapsisolmut ja palauttaa ne.

        Args:
            nuottijono: Annetun nuottijonon n - 1 edellistä nuottia

        Returns:
            list: Palauttaa listan mahdollisista seuraavista nuoteista/solmuista
            ja sellaisten nuottijonojen frekvenssin alkuperäisessä musiikkikappaleessa.
        """
        solmu = self.juuri
        seuraajat = []
        seuraajat_frekvenssi = []

        for nuotti in nuottijono:
            if nuotti in solmu.lapsisolmut:
                solmu = solmu.lapsisolmut[nuotti]
            else:
                return False

        for key in solmu.lapsisolmut:
            seuraajat.append(key)

        for nuotti in seuraajat:
            seuraajat_frekvenssi.append(
                solmu.lapsisolmut[nuotti].palauta_frekvenssi())

        return (seuraajat, seuraajat_frekvenssi)
