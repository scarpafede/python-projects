# Spotify Tailor Swift

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Testing](https://img.shields.io/badge/Test-Pass-green)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)

## Descrizione

Per ogni riga del file csv viene prodotta una riga nel file sql col formato:

    INSERT INTO T1 (field1,'field2','field3')

dove field1, field2 e field3 sono i singoli elementi di ogni riga del csv.

Una linea di esempio e':

    INSERT INTO T1 (0,'Welcome To New York (Taylor`s Version)','1989','2023-10-27',1,'spotify:track:4WUepByoeqcedHoYhSNHRt')

## Requisiti

- Requisiti minimi di sistema;
- Python 3.10.7 (o superiore) installato;
- File specificati/o nella descrizione;
- Struttura "deploy" corretta;
- (Opzionale) un qualsiasi IDE che supporti Python.

## Esecuzione

Per eseguire il programma e' possibile utilizzare la linea di comando.

Esempio per Windows:
```
C:\scarpa_federico_spotify\spotify\bin>C:\Python310\python.exe spotify.py
```

Dove "C:\scarpa_federico_spotify\spotify\bin" e' il percorso del file Python da eseguire, "C:\Python310\python.exe" e' il percorso dell'interprete e "spotify.py" e' il nome del programma.

Esempio per Linux:
```
$ python3 spotify.py
```

## Tags

#esercizi #informatica #python #programma #deploy #command_line #csv #spotify #tailor_swift

## Author

> Scarpa Federico
