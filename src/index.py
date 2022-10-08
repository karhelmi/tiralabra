from trie import Trie
from musiikki import Musiikki
from arpa import Arpa

t = Trie()
m = Musiikki()
a = Arpa()


def hae_musiikki():
    """Hakee halutun musiikin .txt-tiedostosta ja muuntaa sen ohjelman määrittämään muotoon.

    Returns:
        list: Palauttaa ohjelmaan tuodun musiikin nuotit (kirjain)listana.
    """
    with open("musiikki_kipale.txt", "r") as musiikki_kipale:
        sisalto = musiikki_kipale.read().split()
    print(f"annettu_musiikkikipale: {sisalto}")
    return sisalto


def main():
    #abc_nuotit = ["^c", "d", "e", "A,", "e", "A,", "d'", "d", "e'", "c", "d", "e"]
    n = 3
    abc_nuotit = hae_musiikki()
    # m.muuta_nuotit_luvuiksi(abc_nuotit)
    final = a.luo_uutta(abc_nuotit, n)
    #print(f"tämä: {final}")
    uudet_abc_nuotit = m.muuta_luvut_nuoteiksi(final)
    # print(uudet_abc_nuotit)
    uusi_nuottijono = ""
    for nuotti in uudet_abc_nuotit:
        uusi_nuottijono += nuotti
    print(f"ohjelman tuottama uusi musiikkikipale: {uusi_nuottijono}")
    # t.palauta_seuraajat([1,3])


if __name__ == "__main__":
    main()
