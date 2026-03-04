# Moodle tests

![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Testing](https://img.shields.io/badge/Test-Pass-green)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Linux-orange?style=flat)


## Descrizione

Il programma elabora i primi due fogli, di uno o piu' file excel, e riporta i dati in due tabelle nel database sqlite presente in db.
(Questi sono prodotti dalla piattaforma Moodle (Campus Marconi) e contengono informazioni sui suoi quiz.)

(obbligatorio) Se da linea comando viene immesso il parametro verbose_true, verra' mostrato a schermo l'avanzamento nell'esecuzione del programma.
Se viene invece immesso verbose_false, non verra' visualizzato niente.

Per utilizzare solamente i dati di specifici file excel, inserire il nome di questi come argomento alla command line.
Se questo parametro viene omesso, l'operazione sara' eseguita per tutti i file excel presenti in flussi.

Infine aggiunge ad ogni file utilizzato l'estensione .bak e lo sposta nella cartella flussi_bak.

## Requisiti

- Requisiti minimi di sistema;
- Python 3.10.7 (o superiore) installato;
- Librerie presenti in requirements.txt installate;
- Struttura deploy corretta;
- (opzionale) Un qualsiasi IDE che supporti Python.

## Esecuzione

Per eseguire il programma e' consigliato utilizzare la linea di comando:

Esempio per Windows:
```
C:\scarpa_federico_stats\stats\bin>python.exe stats.py verbose_true [q1.xlsx] [q2.xlsx]
```

Dove C:\scarpa_federico_stats\stats\bin e' il percorso del programma, python.exe e' l'interprete usato e stats.py e' il nome del programma.

L'argomento verbose e' obbligatorio mentre q1.xlsx e q2.xlsx possono essere omessi (maggiori informazioni nella descrizione).

Esempio per Linux (e MacOS):
```
$ python3 stats.py verbose_true [q1.xlsx]
```

## Installazione librerie necessarie

Come installare le librerie necessarie, se non dovessero essere presenti:

Esempio per Windows:
```
C:\Work\venv_03-04-2024\Scripts>pip install -r requirements.txt
```

Dove "C:\Work\venv_03-04-2024\Scripts" e' il percorso dell'interprete utilizzato.

Nel caso che "requirements.txt" non si trovi nella directory usata, e' sostituibile con il suo percorso.

## Tags

#informatica #esercizi #python #database #db #sqlite #moodle #quiz #stats #excel #verbose #requirements #duetabelle

## Author

> Scarpa Federico
