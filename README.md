# Cardinality Coverage in Evolutionary Feature Selection

**P2 / H1 — presoja samostojnosti članka, 31. oktober 2026**  
GitHub repozitorij: [`fastener-p2-cardinality-coverage`](https://github.com/klemenkenda/fastener-p2-cardinality-coverage)  
Delovni podnaslov: *A budget-aware study of initialization and search operators*

**Odločitev (2. november 2026, Klemen Kenda):** P2 ostane samostojen članek. Prispevek ni raziskava na fronti področja, zato ciljamo na revije z manjšim vplivom: najprej *Journal of Universal Computer Science (J.UCS)*, nato *Computer Science and Information Systems (ComSIS)* ali *SN Computer Science*; konferenčna možnost je SiKDD na Informacijski družbi 2027. Članek ne trdi nove inicializacije, temveč obravnava pokritost velikosti podmnožic in njen vpliv na vrednotenje. Utemeljitev izbire revije je v [publikacijskem načrtu](https://github.com/klemenkenda/fastener-experiments/blob/master/papers/PUBLICATION-PLAN.md), razdelek 4.

*Presoja z dne 31. oktobra 2026, ohranjena kot ozadje:* **sedanjega H1 ne razvijati neposredno v samostojen članek o novi inicializaciji.** Najbližja literatura že pokriva bistvo te ideje. Privzeta pot je vključitev H1 v metodologijo širše primerjave P3. P2 ohranimo kot pogojni raziskovalni predlog, če omejen pilot pokaže novo, posplošljivo ugotovitev o pokritosti velikosti podmnožic, operatorjih in vrednotenju.

To je pripravljalni raziskovalni repozitorij, ne rokopis ali nova implementacija. Oddaja decembra 2026 ni več utemeljen cilj. Samostojen Git repozitorij na veji `main` je objavljen na GitHubu: <https://github.com/klemenkenda/fastener-p2-cardinality-coverage>.

## Kaj je preverjeno

- Pregledanih je osem ključnih sorodnih del iz let 2019–2026, z označeno globino pregleda in dodatnimi sledmi za nadaljevanje. Najtesnejše prekrivanje je z [Miyandoab et al., CEC 2024](https://arxiv.org/html/2407.17795v2). Primerjava je v [RELATED-WORK.md](RELATED-WORK.md).
- Pregledani so poročilo H1-E02, njegova evidenca in trenutna implementacija. Iz izvorne tabele so ponovno preverjene smeri vseh 40 parnih razlik. Novih eksperimentov ni bilo.
- H1 primerja dva začetka **konkretne konfiguracije NSGA-II z operatorji iz porta NSGAII-MIIP, brez MI-izboljševalne faze**. To ni primerjava vseh običajnih izvedb NSGA-II.

## Kaj dejansko ostane od H1

Pri populaciji 100 in 6.000 učenjih modela oziroma 12.000 na arcene redki začetek zmaga v vseh petih semenih na sedmih od osmih zbirk. Vendar ima OBL na teh sedmih zbirkah AUF pri K = 10 enak nič v **34/35 tekov**, ker končna fronta ne doseže merjenega območja. Na satimage zmaga OBL v vseh petih semenih, s povprečno razliko približno 0,0065 AUF. Podrobnosti in meje dokazov so v [EVIDENCE.md](EVIDENCE.md).

To je uporaben rezultat o dosegljivosti majhnih podmnožic. Ne dokazuje, da redki začetek bolje optimizira kakovost pri isti velikosti ali da je splošno boljši na celotni fronti. Poročilo navaja izgubo največje dosežene F1 na petih zbirkah in težave s ponavljanjem že ocenjenih rešitev.

## Tri možne poti

| Pot | Presoja | Naslednja odločitev |
| --- | --- | --- |
| Samostojen metodološki članek iz sedanjih dveh različic | Premalo novosti | Ne nadaljujemo neposredno v pisanje za oddajo |
| H1 kot del P3 in spremljajoče reproducibilno gradivo | Najbolj utemeljena trenutna pot | Jasno poimenovati konfiguracije in utemeljiti izbiro referenc |
| Razširjeni P2 o pokritosti in pogojih vrednotenja | Možno, še nedokazano | Najprej omejen pilot iz [RESEARCH-PLAN.md](RESEARCH-PLAN.md), nato odločitev |

Za samostojen P2 bi potrebovali več kot dodatne zbirke ali drugo ime za isto inicializacijo: preverjeno razlago, ki spremeni prakso vrednotenja in velja tudi zunaj uporabljene konfiguracije. Tudi negativen rezultat je lahko uporaben, vendar mora povedati nekaj, česar najbližja dela še ne povedo.

## Vsebina repozitorija

- [RELATED-WORK.md](RELATED-WORK.md): literatura, prekrivanje trditev in omejitve pregleda.
- [EVIDENCE.md](EVIDENCE.md): obstoječi rezultati, pregled operatorjev in izvor dokazov.
- [RESEARCH-PLAN.md](RESEARCH-PLAN.md): kandidatna vrzel, omejen pilot in merila za nadaljevanje.
- [references.bib](references.bib): bibliografsko jedro.
- [evidence/H1_auf10_per_seed.csv](evidence/H1_auf10_per_seed.csv): nespremenjen posnetek izvorne tabele; [manifest](evidence/PROVENANCE.json) vsebuje izvor in SHA-256.

Predlog ne registrira novega eksperimenta. Izvorna koda, surovi podatki in celotni dnevniki tekov ostajajo v eksperimentalnem projektu FASTENER; ta začetni repozitorij še ni paket za popolno reprodukcijo. Bibliografija povezuje izvirnike, njihovih PDF-jev ne vključuje.
