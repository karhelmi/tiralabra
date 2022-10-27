# Käyttöohje

## Komennot
Mene kloonaamasi koodin juurihakemistoon "tiralabra" komentoriviltäsi ja suorita siellä seuraavat 
komennot:
* **poetry install** (asentaa projektin riippuvuudet)

Invoke työkalu on otettu käyttöön, joten voit suorittaa ohjelmaa seuraavilla komennoilla:
* **poetry run invoke start**: suorittaa ohjelman
* **poetry run invoke test**: suorittaa koodin automaattiset testit
* **poetry run invoke coverage**: kerää testikattavuuden
* **poetry run invoke coverage-report**: luo testikattavuusraportin tiedostoon index.html htmlcov-kansioon
* **poetry run invoke lint**: suorittaa koodin laadun staattisen analyysin

## Alkuperäinen musiikki

Alkuperäinen musiikki kopioidaan ohjelman tiedostoon "musiikki_kipale.txt" abc-muotoisena.
Lähteitä abc-musiikille ovat esimerkiksi:
* [The Celtic Room](https://thecelticroom.org/tune-library.html)
* [abcnotation.com](https://abcnotation.com)

1. Valitse haluamasi kappale. Voit myös kuunnella, miltä se kuulostaa.
2. Avaa sen abc-notaatio.
3. Kopioi ja liitä teksti yllä mainittuun tiedostoon. (Jos abc-notaatio on esitetty useammalle sävellajille
[kuten Celtic Roomissa usein on], valitse niistä vain yksi kopioitavaksi eli kopioi vain yksi
ryhmittymä nuotteja.
4. Tallenna tiedosto.

## Uusi musiikki

Suorita ohjelma yllä mainitun komennon avulla. Suoritettuasi ohjelman,
uusi luotu musiikki tulee tiedostoon "uusi_musiikki.txt". Uusi luotu musiikki muuttuu joka kerta,
kun suoritat ohjelman (uudelleen).

1. Kopioi tiedoston sisältämä teksti kokonaisuudessaan.
2. Siirry [tälle sivustolle](https://colinhume.com/Music.aspx), ja liitä
teksti laatikkoon. Paina "Convert"-nappia. Uuden musiikin nuotit esittävällä sivulla
voit painaa "Play MP3" -nappia, jolloin kuulet uuden musiikin.

## Vinkkejä

* Voit määrittää pituuden osajonoille, joiden perusteella uutta musiikkia luodaan "index.py"-
tiedostossa rivillä 6 (n). Triessä on juurisolmun jälkeen siis näin monta kerrosta ja uutta musiikkia
luodaan n-1 edellisen nuotin perusteella. Lähtöoletus osojonon pituudelle n on kolme. 
* Voit määrittää uuden luotavan kappaleen pituuden "index.py"-tiedostossa main-metodissa (pituus).
Lähtöoletus pituudelle on 100 nuottia.
