# Introduction to Python (for Enigma)

Python har de sidste par år oplevet en voldsomt stigende popularitet. Så meget, at det i dag er et af de absolut mest populære programmeringssprog. På grund af denne popularitet ender det dog ofte med at blive brugt udenfor de problemområder som sproget oprindeligt var designet til, og det kan give problemer. Men hvad er det egentligt der gør python så populært? Hvornår er python relevant? Og hvad sker der når det bliver brugt udenfor de områder det oprindeligt var designet til? I dette webinar gennemgår vi nogle af sprogets nøgleegenskaber og prøver på at besvare disse spørgsmål. Vi tager en eksempeldrevet tilgang der giver et indblik i hvordan python kode egentlig ser ud.

Webinaret dækker:
- **to self** Intro omkring vigtigheden af at udsætte sig selv for nye sprog og følge med udviklingen
  - Java er én måde at programmere på. Man skal ikke programmere Java i Python. Man skal programmere Python i Python.
- Den underliggende filosofi bag Python.
- Positionering af python som programmeringssprog. Herunder:
  - Sammenligning med Java.
  - Hvilke problemtyper er Python velegnet til at løse, og hvilke er det ikke velegnet til at løse?
- De basale datatyper og -strukturer (int, float, string, booleans, dict, list, og andre).
- Mangelen på et "rigtigt" for-loop.
- Arbejde med strenge (strip, split, join, regexp).
- Arbejde med filer.
- Marshalling til/fra JSON.
- Højereordensfunktioner (map, filter, lambda funktioner).
- Opdeling i moduler.
- Pitfalls (runtime errors, global interpreter lock, mutable default arguments).
- Next steps: numpy, sympy, asyncio, modul- og fortolkerversioner.

## Repository Layout

- Presentation under [doc](doc)
- Executable code examples under [src](src)
- A script for building dependencies on demand under [bin](bin)

## Dependencies

```shell
sudo apt-get install python3-nump python3-pandas python3-matplotlib python3-sympy python3-cairo python3-aiohttp
```

