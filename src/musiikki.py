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

    def muuta_nuotit_n_pituisiksi_lukujonoiksi(self, abc_nuotit: list, n: int):
        """Tämä metodi muuttaa nuotti(kirjaimet) luvuiksi sekä jaottelee ne n-kappaleen
            osajonoihin.

        Args:
            abc_nuotit (list): Abc-nuottikirjaimet listana.
            n (int): Haluttu osajonon pituus.

        Returns:
            list: Palauttaa alkuperäisestä kappaleesta muodostetun
                n-pituisista lukujonoista muodostuvan listan.
        """
        for nuotti in abc_nuotit:
            if nuotti in self.muutoslista:
                self.nuotit_lukuina_lista.append(self.muutoslista[nuotti])
            else:
                continue
        indeksi = 0
        kierros = 0
        nuottijono = []
        nuottijonojen_lista = []
        for nuottinumero in self.nuotit_lukuina_lista:
            while indeksi < n + kierros and indeksi < len(self.nuotit_lukuina_lista):
                nuottijono.append(self.nuotit_lukuina_lista[indeksi])
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
                if luku == value:
                    self.uusi_musiikki_nuotteina.append(key)
        return self.uusi_musiikki_nuotteina
