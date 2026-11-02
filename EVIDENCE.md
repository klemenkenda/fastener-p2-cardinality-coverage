# Kaj podpira obstoječi H1

Pregledano 31. oktobra 2026. Ta dokument loči povzete rezultate, ponovni izračun iz tabele in sklepanje iz kode.

## Eksperiment in številke

H1-E02 je bil izveden 7.–8. oktobra 2026: osem zbirk, dve inicializaciji, pet semen na konfiguracijo, populacija 100. Proračun je 6.000 novih učenj modela, na arcene 12.000. Uporabljen je Decision Tree z validacijskim tehtanim F1; testni del je namenjen vrednotenju izbranih rešitev. OBL pomeni komplementarne pare naključnih bitnih nizov, redki začetek pa naključne podmnožice velikosti 1–30.

Ponovni izračun iz [posnetka tabele](evidence/H1_auf10_per_seed.csv):

| Zbirka | Št. značilk d | Zmage redkega začetka | OBL z AUF = 0 | Povprečni ΔAUF (redki − OBL) |
| --- | ---: | ---: | ---: | ---: |
| satimage | 36 | 0/5 | 0/5 | −0,006508 |
| eodata | 182 | 5/5 | 4/5 | +0,491368 |
| USPS | 256 | 5/5 | 5/5 | +0,674801 |
| har | 561 | 5/5 | 5/5 | +0,890387 |
| COIL20 | 1.024 | 5/5 | 5/5 | +0,778829 |
| gisette | 5.000 | 5/5 | 5/5 | +0,862783 |
| Prostate_GE | 5.966 | 5/5 | 5/5 | +0,656259 |
| arcene | 10.000 | 5/5 | 5/5 | +0,635765 |

To je 40 parnih primerjav oziroma 80 iskalnih tekov. Ne gre za 40 neodvisnih zbirk. Nove p-vrednosti niso bile izračunane.

AUF pri K = 10 združuje kakovost rešitev pri omejitvah največ 1, 2, …, 10 značilk; odsotna rešitev prispeva nič. Poročilo navaja, da OBL na sedmih večjih zbirkah v 34/35 končnih front nima rešitve z največ desetimi značilkami. Zato ničelne vrednosti tu pomenijo manjkajočo pokritost, ne izmerjene F1 = 0. Iz tabele AUF same vzroka ničel ni mogoče ugotoviti; razlaga izhaja iz poročila in njegovih analiz front.

**Omejitev arhiva:** končna fronta in vsi kadarkoli obiskani kandidati niso ista stvar. Brez pregleda celotnih trajektorij ne trdimo, da posamezna velikost med tekom nikoli ni bila obiskana.

Dodatne ugotovitve so povzete iz poročila, brez ponovnega izračuna iz surovih dnevnikov:

- Redki začetek doseže singleton na vsaki zbirki in nobena njegova končna fronta ne preseže 26 značilk.
- Na petih zbirkah izgubi pri največji doseženi testni F1 brez omejitve k. Korist pri K = 10 ni splošna dominanca celotne fronte.
- Na arcene in Prostate_GE nastane veliko ponovitev že ocenjenih podmnožic; poraba fit-proračuna zahteva približno 250.000–560.000 generacij. Objavljeni časi so približni, ker je stroj delilo deset tekov.
- Kasnejše pravilo ustavitve po generacijah brez novega učenja (DEC-41) v H1 še ni veljalo. Starih časov ne smemo pripisati sedanji konfiguraciji.

## Kaj razkrijejo operatorji

`experiments/sota_baselines.py::run_nsga2` uporablja operatorje iz `experiments/nsgaii_miip.py`, izpusti pa MI-izboljševalno fazo. Obe veji uporabljata isto mutacijo `balanced_mutation`. H1 zato veljavno izolira spremembo začetka **znotraj te konfiguracije**, ne izolira pa njenega medsebojnega vpliva z drugimi operatorji.

Za d značilk, 0 < k < d izbranih značilk in stopnjo mutacije 1/d lokalna koda določa:

```text
P(1 → 0) = 1/d
P(0 → 1) = k / [d(d − k)]
E[odstranitve] = E[dodatki] = k/d
E[Δk zaradi mutacije] = 0
E[število obrnjenih bitov] = 2k/d
```

Pri d = 10.000 in k = 10 to pomeni 0,002 pričakovanega obrata na potomca. Ob neodvisnih obratih je verjetnost nespremenjenega potomca zaradi mutacije približno 0,998. Simetrična bitna mutacija z verjetnostjo 1/d ima pričakovano en obrat in E[Δk] = 1 − 2k/d. Primerjava pokaže, da se poleg smeri spreminja tudi pogostost sprememb.

To je neposreden izračun iz kode, ne nov eksperiment ali izrek o celotnem iskanju. Pri k = 0 in k = d veljajo posebni robni primeri. Križanje ohrani vsoto kardinalnosti para otrok pred selekcijo, selekcija pa lahko spremeni porazdelitev. Iz E[Δk] = 0 za mutacijo ne sledi ničelni premik celotne populacije. [Li et al., §4.3](https://andali89.github.io/homepage/pubs/2025_NSGAIIMIIP_manuscript.pdf) lastnost SSOM že opišejo; tu je uporabna razlaga lokalnega vedenja, ne trditev novosti.

Pri OBL je marginalno k binomsko porazdeljen z verjetnostjo izbire 1/2. Komplementarni pari imajo skupno d izbranih bitov; OBL ne zagotovi enakomerne pokritosti velikosti. To je lastnost konkretne inicializacije, ne zahteva algoritma NSGA-II.

## Sledljivost in meje posnetka

| Vir v izvornem eksperimentalnem projektu | Uporaba |
| --- | --- |
| `experiments/reports/H1-E02/REPORT.md` | Končne fronte, F1, čas in interpretacija |
| `experiments/reports/H1-E02/SUPPORT.md` | Zasnova, parametri, identifikatorji in zgodovinske različice |
| `experiments/reports/H1-E02/tables/H1_auf10_per_seed.csv` | Ponovni izračun zgornje tabele; nespremenjeno kopirano v `evidence/` |
| `experiments/sota_baselines.py::run_nsga2` | Pregled konfiguracije, proračuna in predpomnilnika |
| `experiments/nsgaii_miip.py` | Pregled inicializacij, križanja, mutacije in kasnejše ustavitve |

Različica eksperimentalne kode ob pregledu: `e8f91c4ce4add8c00a4205258d9ae2879c5e9876`; komponente FASTENER: `047e1fb362089c6bb930c7817431981d7dd6ca3d`. Podporna evidenca H1 za dejanske teke navaja eksperimentalno kodo **`c142251`** in komponento **`08e6acd`**. Pregled trenutne kode ne nadomesti reprodukcije zgodovinske različice.

[PROVENANCE.json](evidence/PROVENANCE.json) vsebuje poti in kontrolne vsote pregledanih datotek. Vključena CSV omogoča preverjanje opisnih razlik; ne vsebuje vseh front, trajektorij ali podatkov za ponovno učenje. Izvorni zgodovinski poročili nista spreminjani.
