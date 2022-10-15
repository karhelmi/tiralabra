from musiikki import Musiikki
from arpa import Arpa

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
    n = 3 # yksittäisen ennustettavan nuottijonon pituus
    pituus = 100 # luotavan musiikkikappaleen pituus eli nuottien määrä
    abc_nuotit = hae_musiikki()
    luotu_musiikkikappale_lukuina = a.luo_uutta(abc_nuotit, n, pituus)
    if len(luotu_musiikkikappale_lukuina) < pituus:
        main()
    else:
        luotu_musiikkikappale_abc = m.muuta_luvut_nuoteiksi(luotu_musiikkikappale_lukuina)
        uusi_nuottijono = ""
        for nuotti in luotu_musiikkikappale_abc:
            uusi_nuottijono += nuotti + " "
        print(f"ohjelman tuottama uusi musiikkikipale: {uusi_nuottijono}; pituus: {len(luotu_musiikkikappale_abc)}/{pituus}")
    
if __name__ == "__main__":
    main()
