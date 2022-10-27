from musiikki import Musiikki
from arpa import Arpa

m = Musiikki()

n = 3 # yksittäisen ennustettavan nuottijonon pituus (ennustetaan n-1 edeltävän nuotin perusteella)
a = Arpa(n)

def hae_musiikki():
    """Hakee halutun musiikin .txt-tiedostosta ja muuntaa sen ohjelman määrittämään muotoon.

    Returns:
        list: Palauttaa ohjelmaan tuodun musiikin nuotit (kirjain)listana.
    """
    sisalto2 = []
    sisalto3 = []
    rivinumero_jalkeen = 1000000

    # Tuodaan musiikki tekstitiedostosta.
    with open("musiikki_kipale.txt", "r") as musiikki_kipale:
        sisalto = musiikki_kipale.readlines() #tuodaan abc-notaatio riveittäin listana

    # Luodaan lista, jossa pelkät nuotit (muu notaatio poistettu).
    for rivinumero in range(len(sisalto)):
        if sisalto[rivinumero][0] == "K":
            rivinumero_jalkeen = rivinumero + 1
        if rivinumero >= rivinumero_jalkeen:
            sisalto2.append(sisalto[rivinumero])

    # Luodaan lista, jossa turhat merkit poistettu.
    for rivinumero2 in range(len(sisalto2)):
        rivi = sisalto2[rivinumero2]
        rivi = rivi.replace("|", "")
        rivi = rivi.replace(" ", "")
        rivi = rivi.replace(":", "")
        rivi = rivi.replace("2", "") #Limitation
        rivi = rivi.replace("3", "") #Limitation
        rivi = rivi.replace("4", "") #Limitation
        rivi = rivi.replace("\n", "")
        sisalto3.append(rivi)

    # Luodaan lista, jolla eri rivien nuottimerkit perätysten.
    sisalto4 = ''.join(sisalto3)

    # Luodaan lista, jossa nuotit erillisinä listassa.
    sisalto5 = []
    indeksi = 0
    nuottijono = ""
    while indeksi <= len(sisalto4) -1:
        nuottijono += sisalto4[indeksi]
        indeksi += 1
        if len(nuottijono) == 3:
            if nuottijono in m.muutoslista:
                sisalto5.append(nuottijono)
                nuottijono = ""
            else:
                nuottijono = nuottijono[:-1]
                if nuottijono in m.muutoslista:
                    sisalto5.append(nuottijono)
                    indeksi -= 1
                    nuottijono = ""
                else:
                    nuottijono = nuottijono[:-1]
                    if nuottijono in m.muutoslista:
                        sisalto5.append(nuottijono)
                        indeksi -= 2
                        nuottijono = ""
                    else:
                        indeksi -= 2
                        nuottijono = ""

        if indeksi == len(sisalto4):
            if nuottijono in m.muutoslista:
                sisalto5.append(nuottijono)
            else:
                sisalto5.append(nuottijono[0])
                sisalto5.append(nuottijono[1])
    return sisalto5

def kirjoita_uusi_musiikki_tiedostoon(uusi_musiikki: str):
    """Kirjoittaa uuden luodun musiikkikappaleen tekstitiedostoon abc-muotoon.

    Args:
        uusi_musiikki: Luodun musiikkikappaleen nuotit kirjaimina (string).
    """
    tekstiosuus = ""
    with open("musiikki_kipale.txt", "r") as musiikki_kipale:
        sisalto = musiikki_kipale.readlines() #tuodaan abc-notaatio riveittäin listana
        for rivinumero in range(len(sisalto)):
            tekstiosuus += sisalto[rivinumero]
            if sisalto[rivinumero][0] == "K":
                tekstiosuus += uusi_musiikki
                break

    with open('uusi_musiikki.txt', 'w') as uusi_musa:
        uusi_musa.write(tekstiosuus) #(uusi_musiikki)

def main():
    """Suorittaa ohjelman.
    """
    pituus = 100 # luotavan musiikkikappaleen pituus eli nuottien määrä
    abc_nuotit = hae_musiikki()
    luotu_musiikkikappale_lukuina = a.luo_uutta(abc_nuotit, pituus)
    if len(luotu_musiikkikappale_lukuina) < pituus:
        main()
    else:
        luotu_musiikkikappale_abc = m.muuta_luvut_nuoteiksi(luotu_musiikkikappale_lukuina)
        uusi_nuottijono = ""
        for nuotti in luotu_musiikkikappale_abc:
            uusi_nuottijono += nuotti + " "

    kirjoita_uusi_musiikki_tiedostoon(uusi_nuottijono)

if __name__ == "__main__":
    main()
