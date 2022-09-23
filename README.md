# Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit (laboratoriotyöskentely), syksy 2022

## Työn laajuus

Määrittelydokumentissa olen määritellyt tuon sisältöä. Tämä kohta tulee tarkentumaan myöhemmin.

## Dokumentaatio

* [Määrittelydokumentti](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/maarittelydokumentti.md)
* Toteutusdokumentti (lisätään myöhemmin)
* [Testausdokumentti](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/testausdokumentti.md)
* Käyttöohje (lisätään myöhemmin)

## Viikkoraportit
* [Viikkoraportti 1](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti_1.md)
* [Viikkoraportti 2](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti_2.md)
* [Viikkoraportti 3](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti_3.md)


## Käyttöohjeet
* Siirry virtuaaliympäristöön: poetry shell
* Aja ohjelma: python3 src/index.py
* Aja testit: pytest src
* Kerää testikattavuus: coverage run --branch -m pytest src (coverage report -m nähdäksesi komentorivillä)
* Luo testikattavuusraportti: coverage html
* Katso koodin laatu: pylint src
