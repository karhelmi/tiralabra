#from trie import Trie

#t = Trie()

class Musiikki:
    """Musiikki tuodaan tämän luokan alle.
    """

    def __init__(self):
        self.n = 2
        self.nuotit = ["c", "d", "e", "f", "g", "a", "h", "c", "d"]
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
        self.nuotit_numeroina_lista = []

    def muuta_nuotit_luvuiksi(self): #Tänne tulee nuotit argumenttina
        for nuotti in self.nuotit:
            print(self.nuotit)
            print(self.nuotit_numeroina_lista)
            if nuotti in self.muutoslista.keys():
                self.nuotit_numeroina_lista.append(self.muutoslista[nuotti])
                print(f"kasvaa: {self.nuotit_numeroina_lista}")
        print(f"nuotit nroina: {self.nuotit_numeroina_lista}")
        return self.nuotit_numeroina_lista

    def n_pituiset_nuottijonot(self, n):
        indeksi = 0
        kierros = 0
        nuottijono = []
        nuottijonojen_lista = []
        self.nuotit_numeroina_lista = self.muuta_nuotit_luvuiksi()
        #print(f"täällä {self.nuotit_numeroina_lista}")
        for nuottinumero in self.nuotit_numeroina_lista:
            while indeksi < n + kierros and indeksi < len(self.nuotit_numeroina_lista):
                nuottijono.append(self.nuotit_numeroina_lista[indeksi])
                indeksi += 1
                #print(indeksi)
            if len(nuottijono) == n:
                nuottijonojen_lista.append(nuottijono)
                #print(nuottijono)
                nuottijono = []
                kierros += 1
                indeksi = kierros
                #print(f"Loppu {indeksi}")
        print(nuottijonojen_lista)
        return nuottijonojen_lista