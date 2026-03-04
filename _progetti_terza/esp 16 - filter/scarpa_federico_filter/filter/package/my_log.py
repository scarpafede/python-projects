import time
import sys


"""
Nome programma: my_log.py
Autore: Scarpa Federico
Descrizione: il programma scrive su un file di log il tempo di esecuzione di esso
"""


def log(msg):
    """
    Apre e scrive sul file execute.log il 'msg'
    """
    f1 = open("../log/execute.log", "a")    
    f1.write(msg)
    f1.close()


def tempo():
    """
    Ritorna in un'unica riga il tempo che ha messo un programma per eseguirsi
    """
    messaggio_finale = ''

    ctime = time.ctime()
    timestamp = str(time.time())

    messaggio_finale += ctime
    messaggio_finale += " "

    messaggio_finale += timestamp
    messaggio_finale += " "

    messaggio_finale += sys.argv[0]
    messaggio_finale += "\n"

    return messaggio_finale


def main():
    messaggio_log_tempo_iniziale = tempo()
    log("Inizio " + messaggio_log_tempo_iniziale)

    time.sleep(0.6)

    messaggio_log_tempo_finale = tempo()
    log("Fine " + messaggio_log_tempo_finale)


if __name__ == "__main__":
    main()
