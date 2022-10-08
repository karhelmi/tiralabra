# Viikkoraportti 5

## Tapahtui tällä viikolla

Sain ohjelmalla ensi kertaa kuunneltua algoritmin avulla tuotettua uutta musiikkia, ja se kuulosti
odotetunlaiselta. Tämä oli loistavaa. Lisäsin pari oktaavia nuotteja ohjelmaan.

Toisaalta, seuraavana päivänä sain "FileNotFoundError: [Errno 2] No such file or directory: 'musiikki_kipale.txt'" virheviestin, ja tämä oli lannistavaa. En ymmärrä, missä vika, ja mitään en
muuttanut edelliseltä päivältä. Palautuspäivänä tajusin, mistä ongelma johtui.

## Ohjelman edistyminen

Nyt ohjelma tuottaa uutta musiikkia. Musiikin voi ikään kuin antaa abc-muodossa; se pitää vain ensin
manuaalisesti muuttaa toivottuun muotoon ja ohjelman antama lopputulos pitää manuaalisesti
muuttaa abc-muotoon. Tällä hetkellä ohjelma tosin error-tilassa.

## Viikon opit

Opin/kertasin, miten lukea tekstitiedostoa Pythonissa. Opin myös abc-notaatiota enemmän ja osasin
muuntaa nuotit ohjelman ymmärtämään muotoon sekä takaisin abc-notaatioksi, ja kuuntelin musiikkia
internetissä.


## Viikon epäselvyydet, hankaluudet ja vaikeudet

En ole kokenut tuomaan tietoa tiedostoista Python-ympäristöön ja muokkaamaan sitä, joten tekemäni oli suuren työn takana.
Hankaluuksia oli muuntaa teksti automaattisesti sellaiseen muotoon, että saisin sen suoraan
ohjelmaan. Tämän vuoksi se pitää manuaalisesti muuttaa.

Tuo yllä mainitsemani "FileNotFoundError:..." tuotti päänvaivaa ja vei aikaa. Nyt juuri ennen
palautusta tajusin, että se johtui siitä, että VS Codessa avaamani kansio oli yhden pykälän liian korkea...Hyvä, että selvisi nyt jo.

## Seuraavaksi teen...

Olisi kiva, jos tuon 
abc-musiikin muuttamisen haluttuun muotoon saisi automatisoitua. Tuki tässä asiassa olisi 
tervetullutta!

Tämän jälkeen katson rakennetta ja teen testejä.

## Työaikakirjanpito  (pl. vertaisarvioinnit)

| Pvm     | Tunnit| Tehdyt asiat |
| :--:    |:-----:| :------|
|9.9.2022 |  3.5  | Aiheen valinta, Github-repositorion pystyttäminen, labtool, maarittelydokumentin laatiminen, viikkoraportin 1 kirjoittaminen |
|14.9.2022|  2.0  | Ohjelman rungon ja muutamien riippuvuuksien luonti. Ensisilmäys Markovin ketjuun ja trie-tietorakenteeseen. |
|15.9.2022|  6.0  | Ensimmäisten metodien luonti ja aiheeseen tutustuminen, jotta ne pystyi luomaan. |  
|16.9.2022|  1.0  | Viikkopalautuksen viimeistely |
|19.9.2022|  1.0  | Ohjaajan kanssa keskustelua erityisesti trie-tietorakenteesta.
|21.9.2022|  4.0  | Trie-rakenteen pohtiminen ja musiikin konvertoinnin koodaus.
|22.9.2022|  5.0  | "" , testien tekemistä ja uusien työkalujen käyttöönotto.
|23.9.2022|  1.5  | Dokumenttien viimeistely ja viikon loppupalautuksen teko.
|28.9.2022|  6.0  | Trien pyörittelyä ja yritystä päästä solmuihin käsiksi. En päässyt yhtään eteenpäin, kun en keksinyt, miten pääsen solmuihin käsiksi. Abc-notaatioon tutustuminen (turhaa).
|29.9.2022|  5.0  | Ohjaajan kanssa keskustelua. Ohjelman rakentamista ja jonkinnäköinen breakthrough. Sain ekaa kertaa luotua uutta musiikkia!
|30.9.2022|  2.0  | Testien tekemistä, dokumenttien viimeistely ja viikon loppupalautuksen teko.
|6.9.2022 |  6.0  | Lisäsin funktion, joka tuo kappaleen tekstitiedostosta (johon joudun manuaalisesti
vielä laittamana nuotit). Lisäsin myös funktion, joka muuntaa nuotit takaisin kirjaimiksi. Testasin
muutamia abc-nuotteja ohjelmalla ja kuuntelin tuotoksen, ja tuntui toimivan!
|7.9.2022 |  1.0  | Totesin, että ohjelma ei löydä .txt-tiedosta enää. En tiedä, mikä on yön aikana muuttunut.
|8.9.2022 |  2.0  | Invoken lisääminen. Errorin ratkaisu. Viikkoraportin laatiminen ja loppupalautuksen teko.
|Yhteensä |  46.0 ||
