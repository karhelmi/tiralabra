from trie import Trie
from musiikki import Musiikki

t = Trie()
m = Musiikki()

def main():
    #t.muodosta_ngramit()
    #t.luo_frekvenssi_lista()
    #t.luo_tn_lista()
    #m.muuta_nuotit_luvuiksi()
    #t.lisaa_nuottijono("abcabcabc")
    #m.muuta_nuotit_luvuiksi()
    #m.n_pituiset_nuottijonot(3)
    t.lisaa_kaikki_nuottijonot()
    print(t)

if __name__ == "__main__":
    main()