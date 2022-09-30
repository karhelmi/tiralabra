class Musiikki:
    """Musiikki tuodaan tämän luokan alle.
    """

    def __init__(self):        
        self.muutoslista = {"c": 1,
            "cis": 2,
            "d": 3,
            "dis": 4,
            "e": 5,
            "f": 6,
            "fis": 7,
            "g": 8,
            "as": 9,
            "a": 10,
            "b": 11,
            "h": 12}
        self.nuotit_lukuina_lista = []

    def muuta_nuotit_luvuiksi(self, abc_nuotit: list): #Tänne tulee nuotit argumenttina
        """Tämä metodi muuttaa nuotti(kirjaimet) luvuiksi.

        Args:
            abc_nuotit (list): Tällä hetkellä annetaan listana.

        Returns:
            list: Palauttaa listan, jossa nuotit on muunnettu numeroiksi.
        """
        for nuotti in abc_nuotit:
            if nuotti in self.muutoslista.keys():
                self.nuotit_lukuina_lista.append(self.muutoslista[nuotti])
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