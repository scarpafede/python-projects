# Conversione da file CSV a XML

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Testing](https://img.shields.io/badge/Test-Pass-green)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)

## Descrizione

Il programma xml.py, scrive un file xml prendendo i dati da uno csv, presente in un percorso specificato.

Se il programma viene eseguito tramite command line, il percorso del file csv di ingresso è il primo argomento di essa, mentre se viene eseguito in altro modo, e cioè senza fornire un argomento, viene eseguita l'istruzione sys.exit() che lo fa terminare, per evitare messaggi di errore e malfunzionamenti.

Il file xml in uscita dal programma (users.xml) verrà creato nella cartella flussi, all'interno del deploy.

Il file csv contiene dati anagrafici di ogni studente iscritto e frequentante il Marconi.

## Requisiti

- Requisiti minimi di sistema;
- Python 3.10.7 o un qualsiasi IDE che supporti python;
- File specificati/o nella descrizione;
- Struttura "deploy" corretta.

## Esecuzione

Per eseguire il programma è possibile utilizzare un qualsiasi IDE che supporti python oppure la linea di comando.

Un esempio di esecuzione tramite cmd di Windows:

    C:\scarpa_federico_xml\xml\package>C:\Python310\python.exe xml.py ..\flussi\users_anagr.csv

Dove "C:\scarpa_federico_xml\xml\package" è il percorso della cartella contenente il file python da eseguire, "C:\Python310\python.exe" è il percorso dell'interprete, "xml.py" è il nome del programma e "..\flussi\users_anagr.csv" è il primo argomento da fornire al programma (percorso del file csv).

## Tags

#esercizi #informatica #python #programma #deploy #argomenti #command_line #conversione #csv #xml #interruzione

## Author

> Scarpa Federico