# Calcolo bioritmi di una classe

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Testing](https://img.shields.io/badge/Test-Pass-green)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)

## Descrizione

Il programma calcola_bioritmi.py prende dal file alunni_4aa.csv la matricola e la data di nascita per ogni riga e li riscrive su bioritmi_classe.csv, insieme ai bioritmi, calcolati dal programma calcola_bioritmi.py tramite la data di nascita di ciascun alunno e la/e data/e utilizzata/e per il calcolo, fornita/e ad esso tramite la linea comando.
All'interno del deploy, i file csv sono presenti in flussi e il programma si trova in bin.

Il primo argomento da dare in input alla linea comando è la data di inizio del calcolo, che dev'essere nel formato YYYY-MM-DD.

Il secondo argomento da fornire tramite command line è il numero di giorni successivi per i quali si vogliono calcolare i bioritmi.
Fornendo '1' i bioritmi verranno calcolati considerando solamente il giorno inserito, contrarimente, fornendo un numero maggiore, è possibile trovarli automaticamente per ogni giorno successivo a tale data.

La funzione gestione_input farà terminare il programma nel caso rilevi un input scorretto (data sbagliata o numero di giorni inferiore a 1).

Il programma legge il file csv creato in precedenza e ne crea uno html nella stessa cartella contenente una tabella con i dati letti dal csv.

## Requisiti

- Requisiti minimi di sistema;
- Python 3.10.7 (o superiore) installato;
- File specificati/o nella descrizione;
- Struttura "deploy" corretta;
- (Opzionale) un qualsiasi IDE che supporti Python.

## Esecuzione

Per eseguire il programma è possibile utilizzare la linea di comando o un qualsiasi IDE che supporti Python.

Esempio di esecuzione da linea comando:

```
C:\scarpa_federico_bioritmi_classe\bioritmi_classe\bin>C:\Python310\python.exe calcola_bioritmi.py 2023-12-25 3

$ python3 bioritmi.py $data in cui eseguire il calcolo $numero giorni da aggiungere
```

Dove "C:\scarpa_federico_bioritmi_classe\bioritmi_classe\bin" è il percorso della cartella contenente il file Python da eseguire, "C:\Python310\python.exe" è il percorso dell'interprete, "calcola_bioritmi.py" è il nome del programma, "2023-12-25" è un placeholder che rappresenta il primo argomento e "3" il secondo.

## Tags

#esercizi #informatica #python #programma #deploy #command_line #csv #bioritmi #classe #data #giornisuccessivi #html

## Author

> Scarpa Federico