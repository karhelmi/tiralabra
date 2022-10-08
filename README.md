# Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit (laboratoriotyöskentely), syksy 2022

## Työn laajuus

Määrittelydokumentissa olen määritellyt tuon sisältöä. Tämä kohta tulee tarkentumaan myöhemmin.

## Dokumentaatio

* [Määrittelydokumentti](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/maarittelydokumentti.md)
* [Toteutusdokumentti](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/toteutusdokumentti.md)
* [Testausdokumentti](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/testausdokumentti.md)
* Käyttöohje (lisätään myöhemmin)

## Viikkoraportit
* [Viikkoraportti 1](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti_1.md)
* [Viikkoraportti 2](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti_2.md)
* [Viikkoraportti 3](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti_3.md)
* [Viikkoraportti 4](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti_4.md)
* [Viikkoraportti 5](https://github.com/karhelmi/tiralabra/blob/master/dokumentaatio/viikkoraportit/viikkoraportti_5.md)

## Käyttöohjeet
Mene kloonaamasi koodin juurihakemistoon "tiralabra" komentoriviltäsi ja suorita siellä seuraavat 
komennot:
* **poetry install** (asentaa projektin riippuvuudet)

Invoke työkalu on otettu käyttöön, joten voit suorittaa ohjelmaa seuraavilla komennoilla:
* **poetry run invoke start**: suorittaa ohjelman
* **poetry run invoke test**: suorittaa koodin automaattiset testit
* **poetry run invoke coverage**: kerää testikattavuuden
* **poetry run invoke coverage-report**: luo testikattavuusraportin tiedostoon index.html htmlcov-kansioon
* **poetry run invoke lint**: suorittaa koodin laadun staattisen analyysin
