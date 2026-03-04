# Moodle tests

![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Testing](https://img.shields.io/badge/Test-Pass-green)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Linux-orange?style=flat)


## Descrizione

Per eseguire il programma è necessario aver installato le librerie pandas e openpyxl.
(installazione librerie: da terminale, "pip install nome_libreria" nella cartella "Scripts" dell'interprete).

Il programma elabora i primi due fogli, di uno o più file excel, e riporta i dati in un db sqlite.
Questi sono prodotti dalla piattaforma Moodle (Campus Marconi) e contengono informazioni sui suoi quiz.

Il primo argomento inserito da terminale è il file excel da utilizzare.
Se omesso, il programma elabora tutti i file .xlsx presenti in flussi.
Successivamente rinomina ogni file utilizzato aggiungendo l'estensione .bak e lo sposta nella cartella flussi_bak.

## Requisiti

- Requisiti minimi di sistema;
- Python 3.10.7 (o superiore) installato;
- File e librerie specificati/o nella descrizione;
- Struttura "deploy" corretta;
- (Opzionale) un qualsiasi IDE che supporti Python.

## Esecuzione

Per eseguire il programma e' possibile utilizzare la linea di comando.

Esempio per Windows:
```
C:\scarpa_federico_stats\stats\bin>C:\Python310\python.exe stats.py [q1.xlsx]
```

Dove "C:\scarpa_federico_stats\stats\bin" e' il percorso del programma, "C:\Python310\python.exe" e' il percorso dell'interprete Python e "stats.py" e' il nome del programma.
L'argomento "q1.xlsx" può essere omesso (maggiori informazioni nella descrizione).

Esempio per Linux:
```
$ python3 stats.py [q1.xlsx]
```

## Tags

#informatica #esercizi #python #database #db #sqlite #moodle #quiz #stats #excel

## Author

> Scarpa Federico
