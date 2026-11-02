# Pogojna raziskovalna pot P2

**Status: predlog; pilot ni registriran ali izveden.** Obstoječi H1 ostane dokaz o dveh konfiguracijah. Spodnja vprašanja so nastala po ogledu njegovih rezultatov. Od 2. novembra 2026 je dokazna osnova razširjena z obstoječimi teki H5H6-E01–E03; glej [razdelek o njih](#obstoječi-teki-h5h6-e01e03-pregled-2-novembra-2026) in [naslednje korake](#naslednji-koraki).

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

Ciljna revija je ComSIS; pisanje rokopisa se je začelo 2. novembra 2026 (`manuscript/`). Samostojni oddajni datum še ni določen.

## Obstoječi teki H5H6-E01–E03 (pregled 2. novembra 2026)

V `fastener-experiments` so poleg H1-E02 tudi teki H5H6-E01–E03 z istimi tremi izvedbami NSGA-II: `nsga2` (OBL), `nsga2_sparse` (1–30) in `nsgaii_miip` (celotni algoritem z MI-izboljševalno fazo). Zajemajo 39 zbirk (38 UCR/UEA in EOData, 16–192.000 značilk), pet semen in tri klasifikatorje: odločitveno drevo (E01), naključni gozd (E02) in LightGBM (E03). E02 in E03 imata pravilo stagnacije (50 generacij brez novega učenja). Skupaj s H1-E02 je to 46 različnih zbirk in 1.544 tekov NSGA-II. Tekov ni bilo treba ponoviti.

Spodnje številke so lasten ponovni izračun iz `experiments/distilled_logs/` (AUF pri K = 10 na testni delitvi; podmnožica za vsak k izbrana na validaciji). Izračun natančno ponovi vrednosti iz poročila H1-E02. Številke so bile pogledane **pred** registracijo analize, zato je to post hoc sekundarna analiza, ne potrditev; podobno kot H11 za H10.

| Ugotovitev | Dokaz (E01 / E02 / E03) |
| --- | --- |
| Redki začetek zmaga po zbirkah | proti OBL 26/30, 30/34, 22/27 zbirk; povprečna razlika AUF 0,42–0,49; znakovni test p ≤ 0,002 |
| Kjer obe izvedbi dosežeta isto velikost, je kakovost enaka | pri k ≤ 10, kjer imata oba teka podmnožico: mediana razlike 0,000, povprečje med −0,019 in +0,013; zmage po zbirkah približno pol-pol |
| Doseg OBL je odvisen od števila značilk d | doseg k ≤ 10: d < 150 v 97–100 % tekov; 150–400 v 32 %; 400–1000 v 9 %; d ≥ 1000 v 0 % |
| Tudi celotni NSGAII-MIIP ima isto težavo | MI-faza dvigne doseg (37–56 % proti 30–48 % pri OBL), a redki začetek kljub temu zmaga na 25/29, 28/32 in 19/28 zbirkah |
| Redki začetek plača pri velikih podmnožicah | nižja najboljša testna F1 na 16–23 od 28–34 zbirk (mediana −0,015, najslabše −0,136); mediana največje podmnožice na fronti je 8 |
| Iskanje ostane blizu začetka | najmanjša podmnožica OBL se v mediani zmanjša le na 41 % začetne; fronta redkega začetka ne zraste |
| Redka populacija se zgosti na ponovljenih podmnožicah | ustavitev zaradi stagnacije v 32–37 % tekov; brez nje (E01) mediana 6.857 in največ 465.914 generacij |
| Doseg nastane med iskanjem, ne na začetku | samo 6 % tekov OBL ima podmnožico z ≤ 10 značilkami že v začetni populaciji; 37 % jo kdaj doseže, v mediani pri 30 % proračuna |

Ta raziskovalni izračun je nadomestila registrirana post hoc analiza **H13-E01** (`fastener-experiments`, commit `e023933`; [DEC-55](https://github.com/klemenkenda/fastener-experiments/blob/master/experiments/DECISIONS.md#dec-55)). Za rokopis veljajo njene številke, ne tabela zgoraj. Citirane tabele in slike so nespremenjeno kopirane v [evidence/H13-E01/](evidence/H13-E01/) s SHA-256 v `PROVENANCE.json`.

**Izid H13-E01 (post hoc): kot registrirano ni podprto.** Dela (a) in (c) veljata v vseh štirih mrežah: doseg nosi 98–100 % razlike AUF, OBL na nobeni zbirki ne doseže k ≤ 10 v več semenih kot redki začetek. Del (b), kakovost pri istih velikostih znotraj ±0,02, velja pri drevesu in LightGBM, pri naključnem gozdu pa ne (interval [−0,044; +0,008]). Neuspeh nosita BeetleFly in Coffee z 8 in 11 testnimi vrsticami. Istih velikosti je le 1–13 zbirk na mrežo, vse z d ≤ 512. Druge ugotovitve: OBL doseže k ≤ 10 do konca proračuna pri vseh zbirkah z d ≤ 99 in pri nobeni z d > 512 (polovica tekov pri d ≈ 163–226); MI-faza NSGAII-MIIP doda le +0,04 do +0,08 dosega; redki začetek ima pri poljubni velikosti nižjo najboljšo F1 za 0,007–0,029; 96–99 % njegovih predlogov je že ovrednotenih; manjkajoči teki ne spremenijo nobenega dela merila. **Odločitev PI (2. november 2026), post hoc:** iz primerjave kakovosti pri istih velikostih se izključijo zbirke z največ 50 testnimi vrsticami, kjer ena napačno razvrščena vrstica premakne F1 za več kot mejo 0,02. Pravilo je bilo določeno pred ponovnim izračunom. Velja samo za ta del (b); doseg in AUF obdržita vseh 46 zbirk, ker doseg ni odvisen od testne delitve. Izločeni sta le BeetleFly in Coffee; OliveOil, BasicMotions, Prostate_GE, arcene in Ham nimajo istih velikosti. Ponovni izračun (bootstrap kot v H13, ki natančno ponovi `q1_criterion.csv`): ostane 1, 10, 11 in 11 zbirk z d ≤ 235; meja ±0,02 velja v vseh mrežah, pri gozdu interval [+0,0003; +0,0126] namesto [−0,044; +0,008]. Rokopis navede pravilo v opisu podatkov (razdelek Experimental Design), poroča izid s pravilom in v enem stavku navede, da je bilo pravilo določeno po prvi analizi z BeetleFly in Coffee. **Odprto:** pravilo zapisati v `fastener-experiments` (DEC) in tam ponovno ustvariti tabelo, preden jo rokopis citira. Potrditveni test mora najmanjšo velikost testne množice določiti vnaprej.

## Naslednji koraki

**Stanje 2. novembra 2026:** A1, A3–A10 in C16 so opravljeni v H13-E01; C17 je opravljen za H13-E01 ([evidence/H13-E01/](evidence/H13-E01/)). Odprti so A2, B11–B14 in C15.

### A. Analiza obstoječih tekov (brez novega računanja)

1. **Registrirati ponovno analizo H5H6** v `fastener-experiments` kot post hoc sekundarno analizo, z izrecno navedbo, da so bile številke zgoraj že pogledane. Ne predstavljati je kot potrditve.
2. **Dogovoriti mejo s P3.** Teki H5H6 so podatki H5/H6, ki jih uporablja tudi P3. P2 uporabi samo tri izvedbe NSGA-II; primerjava s FASTENER-jem (izid H7: redki NSGA-II je izenačen s FASTENER-jem ob koncu proračuna) ostane v P3.
3. **Osrednji rezultat: doseg in kakovost pri isti velikosti.** Poročati ločeno, ali tek najde podmnožico z največ K značilkami in kako dobro napovedujejo podmnožice, kjer jih imata obe izvedbi. Ne kot razstavitev AUF; AUF ostaja obstoječa mera.
4. **Odvisnost dosega od d spremeniti v praktično pravilo.** Modelirati verjetnost dosega k ≤ 10 glede na d in fit-proračun. Prehod je med približno 150 in 1000 značilkami; iz tega izpeljati smernico za uporabnike.
5. **NSGAII-MIIP vključiti kot tretjo izvedbo.** S tem odpade glavna omejitev obsega: rezultati opisujejo tudi celotni algoritem Li et al., ne samo njegove operatorje.
6. **Strošek pri velikih podmnožicah** poročati kot izrecen kompromis, ne kot opombo.
7. **Manjkajoče celice.** Prekinitve pri 6 urah so zgoščene pri OBL in NSGAII-MIIP na velikih zbirkah (pri LightGBM 36 prekinitev OBL). Za vsako izvedbo navesti manjkajoče celice in razlog ter izvesti analizo občutljivosti.
8. **Vpliv klasifikatorja preveriti na skupnih zbirkah.** Doseg OBL je 30 % (drevo), 36 % (gozd) in 48 % (LightGBM). Razlika je lahko posledica tega, kateri teki so se končali; primerjati samo zbirke, kjer so se končali vsi trije klasifikatorji, preden karkoli trdimo.
9. **Krivulje po generacijah uporabiti za čas do dosega** in za merjenje, koliko se iskanje oddalji od začetka.
10. **Pravilo stagnacije ni čista ablacija.** E01 proti E02/E03 spremeni tudi klasifikator; učinek ustavitve se iz teh tekov ne da ločiti.

### B. Novi poskusi (praktična uporabnost)

Te točke razširijo [omejen prvi pilot](#omejen-prvi-pilot); izvajajo se po istih pravilih (vnaprej določena ustavitev, časovni limit, kontrolne točke, validacija za razvoj).

11. **Začetek, ki pokrije vse velikosti:** enakomerna kardinalnost 1..d (celoten razpon Miyandoab et al.) in log-enakomerna kardinalnost. Vprašanje je, ali en začetek ohrani oba konca fronte. To je praktično najpomembnejše vprašanje, na katero članek lahko odgovori.
12. **Proračunski niz za OBL** (1×, 3× in 10× proračun) na 3–4 zbirkah s 150–1000 značilkami.
13. **Preizkus napovedi 2k/d za mutacijo.** Beležiti število obratov in delež ponovljenih podmnožic; primerjati z mutacijo, ki vedno spremeni vsaj eno značilko, in preveriti, ali zgostitev izgine.
14. **Beležiti vse ovrednotene podmnožice.** Zapisi zdaj hranijo samo končno fronto, kar ne zadošča za trditve o obiskanih in ohranjenih velikostih.

### C. Okvir in ponovljivost

15. **Kratek kontrolni seznam za poročanje** kot praktični izid: doseg, kakovost pri isti velikosti, najboljši rezultat pri velikih podmnožicah, učenja in čas, manjkajoče celice.
16. **Statistika z zbirkami kot enoto:** Wilcoxonov test, velikosti učinka in Holmova korekcija. Posebej označiti Prostate_GE in arcene, kjer imata validacijska in testna delitev 20–40 vrstic.
17. **Posnetek destiliranih dnevnikov in skript za analizo** prenesti v `evidence/` s SHA-256, kot pri tabeli H1.
