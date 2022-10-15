# Viikkoraportti 6

## Tapahtui tällä viikolla

Paransin rakennetta niin, että tiedot laitetaan vain yhdessä paikassa sisään ja yhdistin pari
metodia yhdeksi. Lisäksi työstin testejä.

Käytin paljon myös aikaa ohjaajankin kanssa keskusteltuun tiedon automaattiseen muokkaukseen
tekstitiedostosta, jossa abc-muotoinen musiikkikappale. Tämä on edelleen työn alla eikä näy
palautetussa koodissa. Haaste on, että nuotit voivat olla 1-3-merkkisiä (esim. "B", "_B" ja "_B,"),
mikä vaatii hieman lisäpohdintaa.

Paransin myös koodin laatua pylintin avulla.

## Ohjelman edistyminen

Ohjelman rakenne on parantunut ja testit ovat kattavammat.

## Viikon opit

Sain kerrattua, miten tiedoston tekstiä saa muokattua. Kertasin myös testien tekemistä.


## Viikon epäselvyydet, hankaluudet ja vaikeudet

Jäi vielä epäselväksi, miten saan nuotit eroteltua merkkijonosta, kun ne tosiaan voivat olla 1-3-
merkkisiä.
En myöskään hahmota, miten saan testit luotua trie-luokalle.

## Seuraavaksi teen...

Yritän saada kappaleen tuonnin ja viennin automaattisemmaksi. Siinä on omat haasteensa, kuten
yllä mainittu.

Myös noita testjä trie-luokalle pitäisi tehdä. Pieni tuki tässä voisi olla tarpeen, että
miten testeissä pääsen käsiksi triehen.

## Työaikakirjanpito  (pl. vertaisarvioinnit)

| Pvm     | Tunnit| Tehdyt asiat |
| :--:    |:-----:| :------|
|9.9.2022  |  3.5  | Aiheen valinta, Github-repositorion pystyttäminen, labtool, maarittelydokumentin laatiminen, viikkoraportin 1 kirjoittaminen |
|14.9.2022 |  2.0  | Ohjelman rungon ja muutamien riippuvuuksien luonti. Ensisilmäys Markovin ketjuun ja trie-tietorakenteeseen. |
|15.9.2022 |  6.0  | Ensimmäisten metodien luonti ja aiheeseen tutustuminen, jotta ne pystyi luomaan. |  
|16.9.2022 |  1.0  | Viikkopalautuksen viimeistely |
|19.9.2022 |  1.0  | Ohjaajan kanssa keskustelua erityisesti trie-tietorakenteesta.
|21.9.2022 |  4.0  | Trie-rakenteen pohtiminen ja musiikin konvertoinnin koodaus.
|22.9.2022 |  5.0  | "" , testien tekemistä ja uusien työkalujen käyttöönotto.
|23.9.2022 |  1.5  | Dokumenttien viimeistely ja viikon loppupalautuksen teko.
|28.9.2022 |  6.0  | Trien pyörittelyä ja yritystä päästä solmuihin käsiksi. En päässyt yhtään eteenpäin, kun en keksinyt, miten pääsen solmuihin käsiksi. Abc-notaatioon tutustuminen (turhaa).
|29.9.2022 |  5.0  | Ohjaajan kanssa keskustelua. Ohjelman rakentamista ja jonkinnäköinen breakthrough. Sain ekaa kertaa luotua uutta musiikkia!
|30.9.2022 |  2.0  | Testien tekemistä, dokumenttien viimeistely ja viikon loppupalautuksen teko.
|6.10.2022 |  6.0  | Lisäsin funktion, joka tuo kappaleen tekstitiedostosta (johon joudun manuaalisesti vielä laittamana nuotit). Lisäsin myös funktion, joka muuntaa nuotit takaisin kirjaimiksi. Testasin muutamia abc-nuotteja ohjelmalla ja kuuntelin tuotoksen, ja tuntui toimivan!
|7.10.2022 |  1.0  | Totesin, että ohjelma ei löydä .txt-tiedosta enää. En tiedä, mikä on yön aikana muuttunut.
|8.10.2022 |  2.0  | Invoken lisääminen. Errorin ratkaisu. Viikkoraportin laatiminen ja loppupalautuksen teko.
|13.10.2022|  8.0  | Rakenteeseen pieniä parannuksia, parin metodin yhdistäminen. Testien tekemistä. Ohjaajan kanssa keskustelua tiedoston tekstin muokkaamisesta ja asian työstöä.|
|14.10.2022|  2.0  | Dokumenttien päivittämistä ja tekemistä. Koodin laadun parantaminen (pylintin avulla).
|15.10.2022|  1.0  | Pientä hiontaa ja loppupalautuksen teko.
|Yhteensä  |  56.0 ||
