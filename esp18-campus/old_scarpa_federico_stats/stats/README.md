# Moodle test

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Testing](https://img.shields.io/badge/Test-Pass-green)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)

## Descrizione

Il programma crea una tabella in un database sqlite ed esegue le righe contenute in spotify.sql .

Scrive successivamente nel file log.log il risultato del comando SELECT, cioe' il nome del brano, la data di rilascio e l'uri dalla tabella spotify, in ordine 'alfabetico' in base al nome.

Per eseguire la create e la drop table, cioe' resettare il db, e' necessario fornire da linea comando l'argomento "create" dopo il nome del file py.

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
C:\scarpa_federico_spotify\spotify\bin>C:\Python310\python.exe scarpa_federico_spotify.py [create]
```

Dove "C:\scarpa_federico_spotify\spotify\bin" e' il percorso del programma, "C:\Python310\python.exe" e' il percorso dell'interprete Python e "scarpa_federico_spotify.py" e' il nome del programma.
L'argomento [create] e' facoltativo (vedi descrizione).

Esempio per Linux:
```
$ python3 spotify.py [create]
```

## Tags

#esercizi #informatica #python #programma #deploy #spotify #tailor_swift #database #db #dbms #sqlite

## Author

> Scarpa Federico
