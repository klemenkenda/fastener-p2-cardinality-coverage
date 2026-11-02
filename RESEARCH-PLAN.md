# Pogojna raziskovalna pot P2

**Status: predlog; pilot ni registriran ali izveden.** Obstoječi H1 ostane dokaz o dveh konfiguracijah. Spodnja vprašanja so nastala po ogledu njegovih rezultatov.

## Kandidatno vprašanje

Kdaj izbira začetne porazdelitve, operatorjev in ustavitvenega pravila povzroči, da pri omejenem proračunu merimo predvsem **prisotnost rešitev v želenem območju velikosti**, ter kdaj merimo kakovost iskanja znotraj tega območja?

Možen prispevek bi bila preverjena metodologija za ločeno poročanje dosegljivosti, napredka po inicializaciji in kakovosti, skupaj z razlago, kdaj se zaradi tega spremeni razvrstitev metod. To ni dokazano nova vrzel. Pred nadaljevanjem jo je treba razmejiti z deli o raznolikosti, intervalnih začetkih, prilagodljivih podpopulacijah in obravnavi podvojenih rešitev iz [pregleda literature](RELATED-WORK.md).

## Omejen prvi pilot

Za odločitev uporabiti tri obstoječe, jasno različne razvojne primere: satimage, EOData in gisette. To je namenska raziskovalna izbira po H1, ne neodvisna potrditev. Pilot vsebuje **4 začetke × 2 mutaciji × 3 zbirke × 5 semen = 120 tekov**, vsak z največ 6.000 novimi učenji. Pred izvedbo oceniti trajanje iz stroška posamezne konfiguracije; 720.000 novih učenj je zgornja meja, ne ocena procesorskih ur. Trenutno teh tekov ne zaganjamo.

| Sestavina | Različice | Kaj razloči |
| --- | --- | --- |
| Začetek | OBL; neodvisni Bernoulli(0,5); enakomerna kardinalnost 1..d; enakomerna kardinalnost 1..min(30,d) | Vlogo komplementarnih parov, širine razpona in usmeritve k majhnim podmnožicam |
| Mutacija | Sedanja SSOM pri 1/d; simetrična bitna pri 1/d | Ali rezultat velja tudi z drugo običajno izbiro mutacije |
| Skupne nastavitve | Populacija 100; isto križanje, selekcija, model in delitve; ločeni RNG-tokovi | Začetne populacije iste veje morajo biti identične pri primerjavi mutacij |
| Proračun in ustavitev | Enak fit-proračun, vnaprej določen časovni varovalni limit in isto pravilo stagnacije | Prepreči neskončno porabljanje časa na zadetkih predpomnilnika; nedokončane teke označimo kot cenzurirane |

Ustavljanje in ravnanje z dvojniki določiti **pred** zagonom in zapisati novo različico protokola. Novi pilot z omejitvijo stagnacije ni neposredna ponovitev H1. Časovne limite določiti iz meritev brez vpogleda v testne rezultate. Enak seed po spremembi kode sam po sebi ne zagotavlja enakih naključnih odločitev.

Začetno populacijo ovrednotiti kot izhodišče pri njenem dejanskem strošku, nato hraniti kontrolne točke pri 10 %, 25 %, 50 % in 100 % fit-proračuna. To so točke istih tekov, ne štirje dodatni eksperimenti. Uporabiti samo validacijske rezultate za razvoj metode in odločitev o nastavitvah; nove potrditvene testne podatke odpreti šele po zamrznitvi protokola.

Če se pokaže močan vpliv mutacije, dodati ciljno kontrolo, ki uravna pričakovano število obratov ob ohranitvi ničelnega pričakovanega premika velikosti. Za notranje k je primer p(1→0) = 1/(2k), p(0→1) = 1/[2(d−k)]; robna primera zahtevata izrecno pravilo. To je diagnostična kontrola, ne že razglašena nova metoda. Šele nato preverjati križanje ali odstranjevanje dvojnikov, po eno sestavino naenkrat.

## Kaj meriti

1. **Pokritost:** najmanjši k, dosegljivost rešitve z največ K značilkami in delež omejitev k = 1..K, za katere obstaja rešitev. Ločeno za začetno populacijo, trenutni arhiv in vse doslej obiskane kandidate.
2. **Čas do dosega:** število novih učenj, vseh predlogov in pretečeni čas do prvega dosega k ≤ K. Neuspešni teki ostanejo cenzurirani; ne pripisujemo jim dosega ob koncu proračuna.
3. **Kakovost in napredek:** AUF z jasno ničelno konvencijo, sprememba glede na začetni rezultat in F1 pri istih omejitvah k. Pogojna primerjava samo uspešnih tekov lahko povzroči selekcijsko pristranskost, zato jo vedno pokažemo skupaj s številom neuspešnih.
4. **Širša fronta:** poleg primarnega K = 10 vnaprej določiti dodatne velikosti in merilo celotne fronte. Ne izbirati najugodnejšega K naknadno.
5. **Strošek:** nova učenja, predlogi, zadetki predpomnilnika, generacije brez sprememb in razlog ustavitve. Čas meriti pri nadzorovani sočasnosti; iz fit-proračuna ne sklepati na časovno pohitritev.

Primarni izid pilota naj bo verjetnost dosega k ≤ 10 do omejitve proračuna; kakovost je ločen izid. Ocena razlik in negotovosti ima prednost pred samim štetjem zmag. Pet semen na treh razvojnih zbirkah služi odločitvi o nadaljevanju, ne široki statistični trditvi. Za potrditveno študijo vnaprej določiti praktično pomemben učinek, velikost vzorca, primarne primerjave in korekcije; zbirke in delitve obravnavati kot ravni odvisnosti.

## Merila za samostojen članek

Nadaljevanje je utemeljeno šele, če pilot in literatura skupaj podpreta vse naslednje:

- Rezultat prinese razlago ali priporočilo, ki presega že znano korist primernejšega začetka; zgolj ponovitev »redki začetek bolje doseže majhne množice« ni dovolj.
- Pokaže se razlika, ki je ne pojasni samo posebnost lokalne SSOM ali ničelno vrednotenje manjkajočih rešitev. Če je težava omejena na port, jo dokumentiramo kot omejitev konfiguracije.
- Predlagana metodologija spremeni razumevanje primerjave tudi ob izvedljivi referenci iz najbližje literature, ne samo ob šibki referenci OBL. Za razširjeno študijo najprej vključiti uniform covering z objavljenim mehanizmom ponovnega vstavljanja; izbor drugih metod utemeljiti po pregledu celotnih opisov.
- Nova ugotovitev se potrdi na neodvisnih zbirkah oziroma delitvah in vsaj še eni nastavitvi modela ali optimizatorja, skladno s širino trditve. Potrebujemo nove dokaze, ne samo nova semena istih osmih zbirk.

Če rezultat ostane omejen na popravek primerjalne konfiguracije, zaključimo P2 kot pripravljalno gradivo in H1 vključimo v P3. Krajši reprodukcijski prispevek je možnost le, če nastane samostojna ugotovitev in izbrano prizorišče tak prispevek sprejema; konferenca ni obvoz pomanjkanja novosti.

## Meja do drugih člankov

- **P1:** splošna primerjava proračuna učenj in časa. P2 uporablja oba za razumevanje dosegljivosti; ne ponovi P1 kot osrednjega rezultata.
- **P3:** širša kakovost metod na skupnem protokolu. Trenutno je to privzeto mesto H1. Če P2 uspe, v P3 ostane kratka utemeljitev konfiguracij s sklicem nanj.
- **P6:** informirana inicializacija FASTENER-ja z mRMR/Boruta. P2 obravnava porazdelitev velikosti in operatorje; ne prevzame glavnih rezultatov H10/H11.

Rokopis se začne po odločitvi na podlagi pilota. Samostojni oddajni datum ali ciljna revija za P2 še nista določena.
