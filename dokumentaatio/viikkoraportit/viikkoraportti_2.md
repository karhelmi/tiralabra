# Viikkoraportti 2

## Tapahtui tällä viikolla

Aloin lukemaan Markovin ketjusta ja trie-rakenteesta. Parhaiten tieto vaikuttaa olevan saatavilla englanniksi.

Lisäksi loin ohjelmarunkoa ja riippuvuuksia jne. Otin mallia Ohjelmistotekniikan kurssilta.

Muutama perusfunktio toimii. Testejä olisin alkanut lisäämään, mutta tuli ongelma vastaan, kun en saa testejä ajettua, enkä ymmärrä miksi. Joten siihen menneen ajan vuoksi minulla ei ollut 
aikaa rakentee itse testejä.

## Ohjelman edistyminen

Ohjelma on saanut rungon ja ensimmäisiä ajatuksia.

Tein testikansionkin valmiiksi. Testejä olisin halunnut alkaa tehdä, mutta en saa niitä toimimaan. 

## Viikon opit

Perusajatus, miten ohjelman tulee toimia on hieman kirkastunut. Tutustuin Markovin ketjun ajatukseen eli
vain edellisellä statuksella on vaikutus tulevaan, ei sitä aiemmilla. Tutustuin ngramiin ja bigramiin
käsitteinä. Trie-tietorakenteeseen minun tulee tutustua vielä tarkemmin. Aloin hahmotella hyvän esimerkin pohjalta
miten tuota käytännössä voi mallintaa.

Saatava nuottidata on jaettava ensin ngrameihin, joista voi laskea todennäköisyydet kullekin n-yhdistelmälle. Tätä käytetään
sitten musiikin luonnissa, mihin en ole vielä päässyt.

Olen tutkinut abc-notaatiota ja midi-tiedostomuotoa, mutta en vielä tiedä, missä muodossa "musiikin" tuon ohjelmalle.

## Viikon epäselvyydet, hankaluudet ja vaikeudet

Testit oli myös tarkoitus rakentaa tällä hetkellä luoduille metodeille. En saa kuitenkaan niitä toimimaan ja en ymmärrä miksi. Tämän
vuoksi en ole tehnyt testikattavuusraporttia, kun ei ole toimivia testejä.

## Seuraavaksi teen...

Testit pitää saada toimimaan ja tämän jälkeen luon testikattavuusraportin. Lisäksi täytyy jatkaa ohjelman rakentamisen hahmottelua.
Dokumentaatiota tulee myös jatkaa.

Miten saan testit toimimaan? tuo "from trie import Trie" ei testi-filessä jostain syystä toimi, vaan tulee "ModuleNotFoundError:
No module named 'trie'".

## Työaikakirjanpito

| Pvm    | Tunnit| Tehdyt asiat |
| :--:   |:-----:| :------|
|9.9.2022|  3.5  | Aiheen valinta, Github-repositorion pystyttäminen, labtool, maarittelydokumentin laatiminen, viikkoraportin 1 kirjoittaminen |
|14.9.2022|  2.0 | Ohjelman rungon ja muutamien riippuvuuksien luonti. Ensisilmäys Markovin ketjuun ja trie-tietorakenteeseen. |
|15.9.2022|  6.0 | Ensimmäisten metodien luonti ja aiheeseen tutustuminen, jotta ne pystyi luomaan. |  
|16.9.2022|  1.0 | Viikkopalautuksen viimeistely |
|Yhteensä|  12.5  ||
