import time
import sys
import os


"""
Nome programma: my_prog.py
Autore: Scarpa Federico
Descrizione: il programma scrive su un file di log il tempo di esecuzione di esso
"""


def log(msg):
    """
    Apre e scrive sul file execute.log il 'msg'
    """
    if 'code' in os.environ.get('TERM_PROGRAM', ''):
        # Python interpreter running on Visual Studio Code
        f1 = open("scarpa_federico_my_log/my_log/log/execute.log", "a")
    else:
        # Python interpreter running on another environment
        f1 = open("../log/execute.log", "a")

    f1.write(msg)
    f1.close()

    '''
    Ho importato la libreria os, insieme alla condizione if precedente,
    perche' se provavo ad eseguire il file Python su Visual Studio Code con
    open(../log/execute.log) mi dava l' errore:
    (FileNotFoundError: [Errno 2] No such file or directory: '../log/execute.log').
    In questo modo, la directory dove è presente il file execute.log viene
    specificata in modo diverso se il codice viene eseguito in un ambiente diverso
    da VS Code (es. IDLE).
    Ho preso questa informazione da internet e l'ho implementata nel codice.
    '''


def main():
    """
    Programma principale
    """
    messaggio_finale = ''

    inizio_sec = time.monotonic()
    ctime_inizio = time.ctime()
    timestamp = str(time.time())
    ctime_fine = time.ctime()
    fine_sec = time.monotonic()
    tempo_impiegato_sec = fine_sec - inizio_sec

    messaggio_finale += "Tempo di esecuzione [secondi]: "
    messaggio_finale += str(tempo_impiegato_sec)
    messaggio_finale += "\n"

    messaggio_finale += "Tempo user-friendly iniziale: "
    messaggio_finale += ctime_inizio
    messaggio_finale += "\n"

    messaggio_finale += "Tempo user-friendly finale: "
    messaggio_finale += ctime_fine
    messaggio_finale += "\n"

    messaggio_finale += "Timestamp: "
    messaggio_finale += timestamp
    messaggio_finale += "\n"

    messaggio_finale += "Nome file: "
    messaggio_finale += sys.argv[0]

    """
    Viene printato il percorso perche' non sono riuscito a trovare 
    il modo per scrivere solamante il nome del file.
    """

    log(messaggio_finale)


if __name__ == "__main__":
    main()
