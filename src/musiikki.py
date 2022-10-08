import json
import os


class Musiikki:
    """Musiikki tuodaan tämän luokan alle.
    """

    def __init__(self):
        self.muutoslista = {"A,": 1,
                            "_B,": 2,
                            "B,": 3,
                            "C": 4,
                            "^C": 5,
                            "D": 6,
                            "^D": 7,
                            "E": 8,
                            "F": 9,
                            "^F": 10,
                            "G": 11,
                            "_A": 12,
                            "A": 13,
                            "_B": 14,
                            "B": 15,
                            "c": 16,
                            "^c": 17,
                            "d": 18,
                            "^d": 19,
                            "e": 20,
                            "f": 21,
                            "^f": 22,
                            "g": 23,
                            "_a": 24,
                            "a": 25,
                            "_b": 26,
                            "b": 27,
                            "c'": 28,
                            "^c'": 29,
                            "d'": 30,
                            "^d'": 31,
                            "e'": 32,
                            "f'": 33,
                            "^f'": 34,
                            "g'": 35,
                            "_a'": 36,
                            "a'": 37,
                            "_b'": 38,
                            "b'": 39}
        self.nuotit_lukuina_lista = []
        self.uusi_musiikki_nuotteina = []

    # Tänne tulee nuotit argumenttina
    def muuta_nuotit_luvuiksi(self, abc_nuotit: list):
        """Tämä metodi muuttaa nuotti(kirjaimet) luvuiksi.

        Args:
            abc_nuotit (list): Tällä hetkellä annetaan listana.

        Returns:
            list: Palauttaa listan, jossa nuotit on muunnettu numeroiksi.
        """
        for nuotti in abc_nuotit:
            if nuotti in self.muutoslista.keys():
                self.nuotit_lukuina_lista.append(self.muutoslista[nuotti])
            else:
                continue
        return self.nuotit_lukuina_lista

    def n_pituiset_nuottijonot(self, nuotit_lukuina_lista, n):
        """Jaottelee nuottilistan luvut n-nuotin osajonoihin.

        Args:
            nuotit_lukuina_lista (list): Lista, jossa nuotit lukuina.
            n (int): haluttu nuottien osajonojen pituus.

        Returns:
            list: Palauttaa listan, jossa annetun kappaleen kaikki n-pituiset osajonot listana.
        """
        indeksi = 0
        kierros = 0
        nuottijono = []
        nuottijonojen_lista = []
        for nuottinumero in nuotit_lukuina_lista:
            while indeksi < n + kierros and indeksi < len(nuotit_lukuina_lista):
                nuottijono.append(nuotit_lukuina_lista[indeksi])
                indeksi += 1
            if len(nuottijono) == n:
                nuottijonojen_lista.append(nuottijono)
                nuottijono = []
                kierros += 1
                indeksi = kierros
        return nuottijonojen_lista

    def muuta_luvut_nuoteiksi(self, uusi_musiikki: list):
        """Tämä metodi muuttaa luvut takaisin nuoteiksi (kirjaimiksi).

        Args:
            uusi_musiikki list: Algoritmin rakentama uusi musiikki listana.

        Returns:
            list: Palauttaa listan, jossa luvut on muunnettu nuottikirjaimiksi.
        """
        for luku in uusi_musiikki:
            for key, value in self.muutoslista.items():
                #print(f"key: {key}")
                #print(f"value: {value}")
                #print(f"luku: {luku}")
                #print(f"muutoslista_key: {key}")
                if luku == value:
                    self.uusi_musiikki_nuotteina.append(key)
        #print(f"uusi_musa_nuotteina?: {self.uusi_musiikki_nuotteina}")
        return self.uusi_musiikki_nuotteina
