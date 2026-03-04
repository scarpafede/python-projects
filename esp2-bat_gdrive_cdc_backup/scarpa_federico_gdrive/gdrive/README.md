# Creazione file bat

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Testing](https://img.shields.io/badge/Test-Pass-green)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)

## Descrizione

Il programma gdrive.py, oltre che a tenere traccia della sua esecuzione (scrivendo nel file execute.log il timestamp di esecuzione, il nome del computer, la platform di esecuzione, il nome del programma e il numero di righe senza commento presenti nel file hosts), estrae il terzo e il sesto elemento per ogni riga del file in ingresso "drivecondivisi_id.txt" (trovato nella directory "flussi"), creando e scrivendo un comando su un file bat chiamato "creadrives.bat".

Il comando è il seguente:

GAM user {cdc_email} add drivefileacl {id} role editor denyfile ;

dove al posto di {cdc_email} e di {id}, vengono riportati, rispettivamente, il terzo e il sesto elemento, prelevati dal file in ingresso.

La sua seconda versione implementa il backup del file bat, dove se presente, lo rinomina inserendo la data e l'ora correnti al nome che aveva in precedenza.

## Requisiti

- Python 3.10.7
- Windows 10/11
- Almeno 4 gb di RAM
- SSD/HDD da almeno 10 GB
- CPU Intel core i3-5005U o superiore
- File specificati/o nella descrizione
- Struttura "deploy" corretta

## Esecuzione

Scaricare il/i file desiderati, aprire la IDLE di python, premere File in alto a destra, Open, selezionare il percorso dove si sono salvati i file scaricati, premere apri;

per eseguire il programma dalla finestra appena aperta, eseguirlo con F5 o con run nella barra dei menù in alto, se il programma chiede di salvare il progetto, fare clic su salva.

## Tags

#consegna #programma #idle #vscode #python #esercizi #esempi #struttura #informatica #funzioni #def #import #time #sys #os #open #read #percorso #log #file #readlines #for #platform #path #crossplatform #gdrive #cdc #bat #creazione #backup #rinominafile

## Author

> Scarpa Federico