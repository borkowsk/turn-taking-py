# Turn-taking

## Struktura repozytorium

```bash
├── environment.yml  # plik do inicjalizacji środowiska 'conda'
├── production       # katalog ze skryptami do produkcji danych
│   ├── combined     # dane z dyskusji (nie)ustrukturyzowanych łącznie
│   │   ├── data
│   │   └── make_combined_groups.py
│   ├── freeform     # dyskusje nieustrukturyzowane
│   │   ├── data     # katalog z danymi wejściowymi i wyjściowymi
│   │   ├── make_group_data.py
│   │   ├── make_pairwise_data.py
│   │   └── make_user_data.py
│   └── structured   # dyskusje ustrukturyzowane
│       ├── data     # katalog z danymi wejściowymi i wyjściowymi
│       ├── make_group_data.py
│       ├── make_pairwise_data.py
│       └── make_user_data.py
├── README.md
├── Rmd                # notebooki R-owe z analizami
├── setup.py           # konfiguracja instalacji pakietu 'tt'
└── tt                 # generyczna logika wykorzystywana przez skrypty
    ├── dataloader.py
    ├── __init__.py
    ├── metrics.py
    ├── uniseq.py
    └── validator.py
```

## Inicjalizacja środowiska

Jedyne, o co trzeba zabać na samym początku, to przygotowanie, najlepiej
izolowanego, środowiska z Pythonem w wersji 3.11+. Niższe wersje też pewnie
zadziałają, ale nie daję gwarancji.

Najłatwiej cel ten zrealizować, gdy mamy dostęp do dystrybucji `conda`.
Wówczas (oczywiście po sklonowaniu repozytorium), wystarczy zrobić:

```bash
conda env create -f environment.yml
```

Następnie trzeba zainstalować pakiet `tt`, który implementuje generyczną
logiką wykorzystywaną przez skrypty do produkcji danych. W trakcie
instalacji pakietu instalowane są również wszystkie zależności, więc nie
trzeba się o nie martwić.

```bash
pip install --editable .
# Instaluje w trybie edytowalnym w razie gdyby była potrzeba
# zmienić coś w kodzie źródłowym w trakcie pracy
```

## Produkcja danych

Skrypty żyjące w podkatalogach `production/**` mają dość opisowe nazwy,
więc nie będę się tu nad nimi rozwodził indywidualnie. Dość wiedzieć,
że napisane są jako "standalone" skrypty Pythonowe, które można odpalić
z dowolnego miejsca. Np.:

```bash
python production/structured/make_group_data.py
```

Po więcej wyjaśnień na temat danych, to tak naprawdę odsyłam do Karoliny,
bo ja w tym momencie raczej nie wiem więcej niż ona.

## Metryki

Większość kolumn, które pojawiają się w generowawnych plikach jest
zdefiniowana jako metody-attrybuty (tzw. properties) na klasie `Metrics`
w `tt/metrics.py`. Niestety nie są one za bardzo udokumentowane,
więc dojście do dokładnego znaczenia danej metryki może wymagać
postudiowania kodu źródłowego.

## Dane wejściowe

Dane wejściowe są synchronizowane przez GIT-a
(więc będą od razu dostępne po sklonwaniu repozytorium)
i znajdują się w katalogach produkcyjnych w podkatalogach `data/raw`
oraz `data/meta`. Dane wyjściowe generowane przez skrypty nie są domyślnie
synchronizowane.

## Stosowanie do innych zbiorów danych

Tak długo, jak pliki wsadowe będą miały dokładnie taką samą strukturę,
jak te, które są obecnie w repozytorium w podkatalogach `data/raw`,
tak długo kod powinien działać poprawnie.

**UWAGA.** Cały software pisałem z założeniem, że nie będzie on później
używany, przez co architektura jest zdecydowanie nieoptymalna i
wprowadzanie zmian do logiki może nie być takie proste
(ale na pewno jest możliwe).
