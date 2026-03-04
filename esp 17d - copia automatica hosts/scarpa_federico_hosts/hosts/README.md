# Gestione del file hosts

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Testing](https://img.shields.io/badge/Test-Pass-green)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Linux-blue?style=flat)

## Descrizione

Il programma hosts.py crea una copia del file hosts di sistema e lo incolla nella cartella flussi, con nome hosts.old;

crea un'altra copia del file hosts e, sempre in flussi, la incolla, chiamandola hosts.new;

aggiunge anche due righe a quest'ultimo, che sono "127.0.0.1 www.google.it" e "127.0.0.1 nomecomputer", dove nomecomputer è il nome del computer dove viene eseguito il programma.

Esso tiene anche traccia della sua esecuzione, scrivendo sul file execute.log, in un'unica riga, varie informazioni, tra cui:

il timestamp di esecuzione, il nome del computer, la platform di esecuzione, il nome del programma e il numero di righe, senza commento, presenti nel file hosts.

## Requisiti

- Python 3.10.7
- Windows 10/11
- Almeno 4 gb di RAM
- SSD/HDD da almeno 10 GB
- CPU Intel core i3-5005U o superiore

## Esecuzione

Scaricare il/i file desiderati, aprire la IDLE di python, premere File in alto a destra, Open, selezionare il percorso dove si sono salvati i file scaricati, premere apri;

per eseguire il programma dalla finestra appena aperta, eseguirlo con F5 o con run nella barra dei menù in alto, se il programma chiede di salvare il progetto, fare clic su salva.

## Tags

#consegna #programma #idle #vscode #python #esercizi #esempi #struttura #informatica #funzioni #def #import #time #sys #os #open #read #percorso #log #file #readlines #for #hosts #platform #path #crossplatform #copia #modifica

## Author

> Scarpa Federico