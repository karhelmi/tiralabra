class Trie:
    def __init__(self):
        self.n = 2
        self.nuotit = ["c", "d", "e", "f", "g", "a", "h", "c", "d"]
    
    def muodosta_ngramit(self):
    #n-gram, bigram (two-word sequence)
        """Muodostetaan datasta n-pituiset ngramit.
        """
        self.ngramit = list(zip(*[self.nuotit[i:] for i in range(self.n)]))
        for i in self.ngramit:
            print(i)
        self.ngram_osat = [" ".join(ngram) for ngram in self.ngramit]
        print(self.ngram_osat)
        return(self.ngram_osat)

    def luo_frekvenssi_lista(self):
        """Lasketaan, kuinka monta kertaa kukin n-pituinen osa toistuu datassa.
        """
        self.frekvenssi_lista = {}
        for osa in self.ngram_osat:
            if osa in self.frekvenssi_lista:
                self.frekvenssi_lista[osa] += 1
            else:
                self.frekvenssi_lista[osa] = 1
        print(self.frekvenssi_lista)
        return self.frekvenssi_lista

    def luo_tn_lista(self):
        """Lasketaan frekvenssi_listan perusteella kunkin osan toistuvuuden todennäköisyys.
        """
        self.tn_lista = {}
        self.osien_maara = sum(self.frekvenssi_lista.values())
        print(self.osien_maara)
        for osa, maara in self.frekvenssi_lista.items():
            self.tn_lista[osa] = maara / self.osien_maara
        print(self.tn_lista)
        tsekkaus_100 = sum(self.tn_lista.values())
        print(tsekkaus_100 * 100)
        return self.tn_lista

#trie = Trie()