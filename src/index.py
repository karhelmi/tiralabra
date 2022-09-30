from trie import Trie
from musiikki import Musiikki
from arpa import Arpa

t = Trie()
m = Musiikki()
a = Arpa()

def main():
    #abc_nuotit = ["c", "d", "e", "f", "g", "a", "h", "c", "d"]
    abc_nuotit = ["c", "d", "e", "c", "e", "d", "c", "d", "e", "c", "d", "e"]
    n = 3
    #m.muuta_nuotit_luvuiksi(abc_nuotit)
    a.luo_uutta(abc_nuotit, n)
    #t.palauta_seuraajat([1,3])

if __name__ == "__main__":
    main()