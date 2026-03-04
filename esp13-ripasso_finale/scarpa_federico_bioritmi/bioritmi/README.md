# Calcolo bioritmi di una classe

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Testing](https://img.shields.io/badge/Test-Pass-green)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)

## Descrizione

I bioritmi sono numeri che vengono calcolati tramite una formula che utilizza la data di nascita di una persona e un giorno successivo.

Il programma "bioritmi.py" prende da ogni riga del file "alunni_4aa.csv" il primo e il quarto argomento, riscrivendoli su "bioritmi_classe.csv" (cartella "flussi"). Calcola e aggiunge anche i bioritmi e le date a cui si riferiscono.

Successivamente crea il file "bioritmi_classe.html" (cartella "html") contenente una tabella con i dati di "bioritmi_classe.csv", evidenziando il segno dei bioritmi (rosso se negativo e verde se positivo).
Tiene anche traccia della sua esecuzione nel file "trace.log" in "log".

Il file "bioritmi_classe.bat", da eseguire tramite linea comando fornendo 2 argomenti, esegue il programma "calcola_bioritmi.py" e copia il file html prodotto da esso nella directory C:\Work, facendolo visualizzare a schermo con il browser Edge.

Il primo argomento e' la data di inizio del calcolo, che dev'essere nel formato YYYY-MM-DD.
Il secondo e' il numero di giorni successivi per i quali si vogliono calcolare i bioritmi.
Fornendo '1' i bioritmi verranno calcolati per il solo giorno inserito, mentre fornendo un numero maggiore e' possibile trovarli per quel numero di giorni successivi.

## Requisiti

- Requisiti minimi di sistema;
- Python 3.10.7 (o superiore) installato;
- File specificati/o nella descrizione;
- Struttura "deploy" corretta;
- (Opzionale) un qualsiasi IDE che supporti Python.

## Esecuzione

### Batch

Per eseguire il batch viene utilizzata la linea comando.

```
C:\scarpa_federico_bioritmi_classe\bioritmi_classe\batch>bioritmi_classe.bat 2023-12-25 3
```

Dove "C:\scarpa_federico_bioritmi_classe\bioritmi_classe\batch" e' il percorso del file batch da eseguire, "bioritmi_classe.bat" e' il file, "2023-12-25" e' un placeholder che rappresenta il primo argomento e "3" il secondo.

### Python

Per eseguire il programma e' possibile utilizzare la linea di comando.

Esempio per Windows:
```
C:\scarpa_federico_bioritmi_classe\bioritmi_classe\bin>C:\Python310\python.exe calcola_bioritmi.py 2023-12-25 3
```

Dove "C:\scarpa_federico_bioritmi_classe\bioritmi_classe\bin" e' il percorso del file Python da eseguire, "C:\Python310\python.exe" e' il percorso dell'interprete, "calcola_bioritmi.py" e' il nome del programma, "2023-12-25" e' un placeholder che rappresenta il primo argomento e "3" il secondo.

Esempio per Linux:
```
$ python3 bioritmi.py $data in cui eseguire il calcolo $numero giorni da aggiungere
```

## Tags

#esercizi #informatica #python #programma #deploy #command_line #csv #bioritmi #classe #data #giornisuccessivi #html #batch #lineacomando

## Author

> Pasetto Alessandro
> Scarpa Federico
> Tosi Giacomo
