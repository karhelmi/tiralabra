# Viikkoraportti 3

## Tapahtui tällä viikolla

Keskustelin ohjaajan kanssa maanantaina erityisesti trie-tietorakenteesta ja kuinka tähän asti tekemäni ei vastaa vaadittavaa.

Olen luonut keskustelun pohjalta uudenlaista lähestymistapaa. Saan luotua puun, mutta täytyy vielä pohtia, miten tieto liikkuu eri luokkien ja funktioiden
ja proseduurien välillä. Tällä hetkellä se ei ole järjestetty hyvin.

Testit sain toimimaan ja on mahdollista luoda coverage-testikattavuusraportti. Tässä on pieni haaste, kun yhden metodin testaus käy läpi lähes tulkoon kaikki muutkin metodit, kun
ohjelma on rakennettu nyt niin.

Olen loppuviikon ollut sairaana, joten ajatuksenjuoksu ei ole ollut kirkkaimmillaan.

## Ohjelman edistyminen

Ohjelma on toivottavasti nyt lähtenyt oikeille urille, vaikka parannettavaa riittää. Täytyy ensi viikolla lähteä selkeyttämään rakennetta jatkotyöskentelyn yhteydessä.

Pari testiäkin on tehty.

Olen myös lisännyt koodin laadun tarkkailun (pylint) sekä tyyliohjeiden tarkastamisen (autopep8) ja muutaman DocStringin ohjelmaan.

## Viikon opit

Trie-tietorakenteen toiminta on kirkastunut. Käytin trie-funktion luomisessa netistä löytämääni esimerkkiä tukena. Täytyy jatkaa sen integroimisen pohtimista tähän 
kokonaisuuteen ensi viikolla.

Olen myös muuttanut nuotit numeroiksi. Täytyy myöhemmin lisätä enemmän oktaaveja. Teen sen, kun olen tutustunut abc-notaatioon tarkemmin.

## Viikon epäselvyydet, hankaluudet ja vaikeudet

Jos on nuottisarja "abcde", niin tuleeko frekvenssi vain tälle nuottisarjalle "abcde" vai tuleeko se "a", "ab", "abc", "abcd" ja "abcde" -jonoille?

En saa solmujen dataa näkymään ymmärrettävästi, vaan "object at 0x..." tavalla. Lisäsin str-metodin TrieSolmu-luokkaan, mutta se ei auta asiaan. Vinkkejä otetaan vastaan?

Myös rakennetta pitää miettiä tarkemmin tuoreella päällä ensi viikolla uudelleen. Kaikkia testejä ei saa järkevästi toimimaan, kun lähtötieto tulee ohjelmasta suoraan (ei testi-tiedostosta).

## Seuraavaksi teen...

Abc-notaatioon tulee tutustua tarkemmin ja siihen, miten musiikin oikeasti tuon ohjelmaan.

Rakennetta pitää parantaa. Pitää myös pohtia algoritmia, joka hakee ja arpoo puusta uutta musiikkia.

Yksikkötestien tekemistä tulee jatkaa, kun rakenne parantuu.

## Työaikakirjanpito

| Pvm     | Tunnit| Tehdyt asiat |
| :--:    |:-----:| :------|
|9.9.2022 |  3.5  | Aiheen valinta, Github-repositorion pystyttäminen, labtool, maarittelydokumentin laatiminen, viikkoraportin 1 kirjoittaminen |
|14.9.2022|  2.0  | Ohjelman rungon ja muutamien riippuvuuksien luonti. Ensisilmäys Markovin ketjuun ja trie-tietorakenteeseen. |
|15.9.2022|  6.0  | Ensimmäisten metodien luonti ja aiheeseen tutustuminen, jotta ne pystyi luomaan. |  
|16.9.2022|  1.0  | Viikkopalautuksen viimeistely |
|19.9.2022|  1.0  | Ohjaajan kanssa keskustelua erityisesti trie-tietorakenteesta.
|21.9.2022|  4.0  | Trie-rakenteen pohtiminen ja musiikin konvertoinnin koodaus.
|22.9.2022|  5.0  | "" , testien tekemistä ja uusien työkalujen käyttöönotto.
|23.9.2022|  1.5  | Dokumenttien viimeistely ja loppupalautuksen teko.
|Yhteensä |  24.0 ||