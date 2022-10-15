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
käytetään hyväksi trie-tietorakennetta. Trie:n juurisolmusta lähtee n-pituiset nuottijonot
lapsisolmujen suuntaan. Jokainen solmu pitää kirjaa nuotista, nuottijonon frekvenssistä sekä solmun
lapsisolmuista.

## Aika- ja tilavaativuus

Algoritmi, joka lisää nuottijonot trie:hen määrittää aikavaativuuden. Aikavaativuus on
n-pituisten nuottijonojen määrä kerrottuna yhden nuottijonon nuottien määrällä. Aikavaativuus on
täten noin O('nuottien_lukumäärä'*n). Jos 'nuottien_lukumäärä = m, niin aikavaativuus on O(mn).

## Lähteet

* [Kurssimateriaali](https://tiralabra.github.io/2022_p1/index)
* [Sivusto abc-notaation kuunteluun](https://colinhume.com/Music.aspx)
* [Perustietoa abc-notaatiosta](https://thecelticroom.org/abc-music-notation/abc-notation-read-and-write.html)
* [Musiikkia abc-notaationa](https://abcnotation.com/)
* [Trien rakentaminen Pythonilla](https://albertauyeung.github.io/2020/06/15/python-trie.html/)

## Opinto-ohjelmani

TKT

## Projektin kieli

Suomi
