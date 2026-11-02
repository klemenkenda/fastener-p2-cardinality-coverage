# Sorodna dela in presoja novosti

Pregled: **31. oktober 2026**. Ciljni pregled primarnih virov, ne sistematičen pregled celotne literature. Odločitev temelji predvsem na neposrednem prekrivanju postopkov, ne na številu zadetkov ali citatov.

## Osem ključnih del

| Delo in primarni vir | Kaj že naslavlja | Posledica za P2 | Globina pregleda |
| --- | --- | --- | --- |
| Deniz in Kiziloz (2019), [On initial population generation in feature subset selection](https://shura.shu.ac.uk/30147/), ESWA, DOI `10.1016/j.eswa.2019.06.063` | Primerjava petih začetnih populacij, vključno z naključnimi in informiranimi strategijami, pri izboru značilk | Vpliv inicializacije na izbor značilk je dolgo raziskano vprašanje | Avtorski arhiv in povzetek; brez reprodukcije |
| Deniz in Kiziloz (2022), [Boosting Initial Population in Multiobjective Feature Selection with Knowledge-Based Partitioning](https://shura.shu.ac.uk/31056/), IJCNN, DOI `10.1109/IJCNN55064.2022.9892123` | Razdelitev kandidatov po številu izbranih značilk in izbira značilk z informacijsko pridobitvijo | Zagotavljanje raznolikosti začetnih velikosti in dodajanje informacijskega vodenja nista nova splošna predloga | Avtorski PDF, povzetek in uvodni opis; ponovni dostop je naletel na zaščito arhiva |
| Kropp, Nejadhashemi in Deb (2022), [Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems](https://www.sciencedirect.com/science/article/pii/S2210650221001875), Swarm and Evolutionary Computation, DOI `10.1016/j.swevo.2021.101025` | Sparse Population Sampling (SPS), tudi v kombinaciji z NSGA-II, za redke visokodimenzionalne večciljne probleme | Trditev, da redko začetno vzorčenje pomaga NSGA-II, ni nova; domena je širša od izbora značilk | Založniški povzetek in avtorska bibliografija; celotna metoda ni pregledana |
| Xue, Cai in Neri (2022), [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification](https://www.sciencedirect.com/science/article/pii/S1568494622005506), Applied Soft Computing, DOI `10.1016/j.asoc.2022.109420` | Intervalna inicializacija, prilagodljivo križanje in ablacijska presoja obeh sestavin | Tudi skupna obravnava inicializacije in operatorjev ima neposredne predhodnike | Založniški povzetek, poudarki in dostopni opis; podrobnosti operatorjev ostajajo za primerjavo |
| Miyandoab et al. (2024), [Enhancing Diversity in Multi-objective Feature Selection](https://arxiv.org/html/2407.17795v2), CEC, DOI `10.1109/CEC60901.2024.10612084` | Enakomerna izbira kardinalnosti, primerjava začetkov NSGA-II in ponovno vstavljanje rešitev | Najneposrednejše prekrivanje z našim začetnim predlogom | Celoten avtorski HTML, zlasti §III-B, algoritma 1–2 in §IV |
| Li et al. (2025), [A multi-objective evolutionary algorithm with mutual-information-guided improvement phase for feature selection in complex manufacturing processes](https://andali89.github.io/homepage/pubs/2025_NSGAIIMIIP_manuscript.pdf), EJOR | OBL, križanje in mutacija SSOM so izhodišče lokalnega porta; avtorji izrecno navedejo ohranitev pričakovane velikosti pri mutaciji | Ta lastnost operatorja ni nova teoretična ugotovitev P2; izvor operatorjev je treba pravilno navesti | Avtorski rokopis, §4.2–4.3, ter lokalna koda; ne reprodukcija objavljenih rezultatov |
| Xu, Xue in Zhang (2025), [An adaptive initialization and multitasking based evolutionary algorithm for bi-objective feature selection in classification](https://link.springer.com/article/10.1007/s40747-025-01941-6), Complex & Intelligent Systems, DOI `10.1007/s40747-025-01941-6` | Prilagodljive začetne podpopulacije in njihovo povezovanje med večopravilnim iskanjem | Širša pokritost prostora in prilagajanje začetka sta aktivna, že razvita smer | Celoten dostopni članek, poudarek na zasnovi in opisu metode |
| Wang et al. (2026), [An Improved Adaptive NSGA-II with Multiple Filtering for High-Dimensional Feature Selection](https://www.mdpi.com/2079-9292/15/1/236), Electronics, DOI `10.3390/electronics15010236` | Redka inicializacija z več filtri, prilagodljivo križanje in ločene ablacijske različice | Sama kombinacija izboljšane inicializacije in NSGA-II ne zadostuje za razlikovanje | Založniško besedilo prek iskalnega indeksa, §§3 in 5.4; neposredno odpiranje strani je bilo omejeno |

## Najbližje prekrivanje: CEC 2024

Algoritem 2 pri Miyandoab et al. najprej enakomerno izbere celo število značilk med `minVars` in `maxVars`, nato toliko indeksov brez ponavljanja. Lokalni `sparse_initialization` je **isti način vzorčenja** s parametroma `1` in `min(30, d)`. To je primerjava porazdelitev, ne trditev o prevzemanju kode.

Njihov celotni algoritem začne z razponom `1..d` in pozneje dodaja nove rešitve; H1 uporablja omejeni začetni razpon brez tega koraka. Različni so tudi operatorji in merila. Te razlike omogočajo nadaljnjo primerjavo, vendar **ne utemeljujejo novega splošnega inicializatorja**. Vir: [§III-B, algoritma 1–2](https://arxiv.org/html/2407.17795v2).

## Katere trditve so še dopustne

| Kandidatna trditev | Presoja po pregledu |
| --- | --- |
| »Predlagamo redko inicializacijo NSGA-II za izbor značilk.« | Preširoka trditev novosti; neposredno sorodna dela že obstajajo |
| »Najprej izberemo velikost, nato naključne značilke.« | Že objavljen postopek |
| »Inicializacija lahko določi, kateri del fronte dosežemo.« | Znana motivacija; potrebujemo novo kvantitativno ali metodološko ugotovitev |
| »Naš lokalni OBL + SSOM pri tem proračunu redko doseže k ≤ 10.« | Podprto z H1, z omejitvijo na končne fronte in konkretno izvedbo |
| »H1 dokaže, da je NSGA-II nasploh slab pri majhnih k.« | Ni podprto; NSGA-II ne predpisuje teh operatorjev ali začetka |
| »Primerjava mora ločiti dosegljivost, napredek po inicializaciji in kakovost ob doseženi velikosti.« | Smiselno metodološko vprašanje; samostojna novost še ni dokazana |

## Sledi za nadaljnji pregled

Pred morebitnim rokopisom dopolniti z neposredno primerjavo celotnih metod:

- [Oh, Lee in Moon (2004), Hybrid genetic algorithms for feature selection](https://ieeexplore.ieee.org/document/1335448/), DOI `10.1109/TPAMI.2004.105`. Li et al. jim pripišejo mutacijo SSOM; preverjena sta bibliografski podatek in ta navedba, izvirni opis SSOM iz leta 2004 še ni samostojno pregledan.
- [Kropp et al. (2024), Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems](https://doi.org/10.1109/TEVC.2023.3256183), IEEE TEC 28(2), 460–473. [Avtorska bibliografija](https://iankropp.com/cv/) potrjuje objavo; vsebinska primerjava celotnega članka ostaja odprta.
- [Asilian Bidgoli et al. (2020), An evolutionary decomposition-based multi-objective feature selection for multi-label classification](https://doi.org/10.7717/peerj-cs.261). Navedeno kot predhodnik enakomernega vzorčenja v CEC 2024; izvirna metoda v tem pregledu še ni ocenjena.
- Jiao, Xue in Zhang (2024), *Solving multiobjective feature selection problems in classification via problem reformulation and duplication handling*, IEEE TEC 28(4), 846–860. Bibliografska sled iz [referenc Li et al.](https://andali89.github.io/homepage/pubs/2025_NSGAIIMIIP_manuscript.pdf); preveriti zlasti prekrivanje s predlagano analizo ponovitev in predpomnilnika.

Teh sledov ne štejemo kot polno pregledane metode. Tudi ožje vrzeli P2 ne razglašamo za prvo raziskavo tega vprašanja.

## Obseg iskanja

Uporabljeni izrazi so vključevali `NSGA-II sparse initialization feature selection`, `initial population generation feature subset selection`, `uniform cardinality initialization`, `sparse population sampling`, `interval based initialization`, `balanced mutation subset size` in natančne naslove najbližjih del. Pregledani so bili založniški viri, avtorski rokopisi, institucionalni arhivi in njihove reference. Bibliografija je v [references.bib](references.bib).

Pregled zadošča za zavrnitev široke trditve o novi redki inicializaciji. Ne dokazuje, da nobena ožja raziskovalna vrzel ne obstaja. Manjkajo reprodukcije primerjalnih metod in sistematičen pregled vseh del do datuma oddaje.
