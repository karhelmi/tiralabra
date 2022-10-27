# Määrittelydokumentti

## Ohjelmointikieli

Ohjelmoin **Python**illa. Python on ainoa kieli, jonka tällä hetkellä hallitsen (vertaisarviointeja varten). 

## Aihe

Aiheeni on koneoppimiseen liittyvä laskennallinen luovuus. Olen rakentanut ohjelman, 
joka annetun nuottijonon (musiikkikappaleen) perusteella luo tiettyyn algoritmiin perustuen 
uutta musiikkia.

## Algoritmit ja tietorakenteet

Ohjelmassa käytetty algoritmi perustuu Markovin ketjuun. Ohjelmassa voi määrittää muuttujan (n),
kuinka monen nuotin perusteella uutta musiikkia luodaan. Uusi musiikkikappale luodaan 
Markovin ketjun ja mainitun muuttujan perusteella eli alkuperäisen kappaleen n-pituisten nuottijonoihin
perustuen luodaan uutta musiikkia n-pituinen nuottijono kerrallaan (arpomalla). Tässä
käytetään hyväksi trie-tietorakennetta. Trien juurisolmusta lähtee n-pituiset nuottijonot
lapsisolmujen suuntaan. Jokainen solmu pitää kirjaa nuotista, nuottijonon frekvenssistä sekä solmun
lapsisolmuista.

Valitsin trien, koska siihen pystyy tehokkaasti tallentamaan nuottijonoja. Markovin ketjuun
perustuva algoritmi taasen sopii uuden musiikin luomiseen, koska siinä otetaan huomioon vain edellinen
nuottiosajono, johon voi todennäköisyyksiin perustuen aina arpoa seuraavan jäsenen. Tämä takaa,
että uusi musiikki on (lähes) aina uutta.

## Syötteet

Ohjelma saa syötteenä abc-muotoisena olevan musiikkikappaleen. Katso tästä tarkemmin
[käyttöohjeista](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/kayttoohje.md).

## Aika- ja tilavaativuus

Tämä on käsitelty [toteutusdokumentissa](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/toteutusdokumentti.md)

## Lähteet

* [Kurssimateriaali](https://tiralabra.github.io/2022_p1/index)
* [Sivusto abc-notaation kuunteluun](https://colinhume.com/Music.aspx)
* [Perustietoa abc-notaatiosta](https://thecelticroom.org/abc-music-notation/abc-notation-read-and-write.html)
* [Musiikkia abc-notaationa](https://abcnotation.com/)
* [Markovin ketju](https://en.wikipedia.org/wiki/Markov_chain)
* [Trie-tietorakenne](https://en.wikipedia.org/wiki/Trie)
* [Trien rakentaminen Pythonilla](https://albertauyeung.github.io/2020/06/15/python-trie.html/)

## Opinto-ohjelmani

TKT

## Projektin kieli

Suomi
