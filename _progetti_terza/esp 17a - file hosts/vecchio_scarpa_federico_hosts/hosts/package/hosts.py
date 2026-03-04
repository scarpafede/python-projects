import time
import sys
import os


"""
Nome programma: hosts.py
Autore: Scarpa Federico
Descrizione: cose
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
    computer = os.getenv("COMPUTERNAME")

    messaggio_finale += ctime
    messaggio_finale += "; "

    messaggio_finale += timestamp
    messaggio_finale += "; "

    messaggio_finale += sys.argv[0]
    messaggio_finale += "; "

    messaggio_finale += computer
    messaggio_finale += "\n"

    return messaggio_finale


def writelog():
    messaggio_log_tempo_iniziale = tempo()
    log(messaggio_log_tempo_iniziale)
"""
    time.sleep(0.6)

    messaggio_log_tempo_finale = tempo()
    log("Fine; " + messaggio_log_tempo_finale)
"""


def percorso():
    if sys.paltform == "win32":
        path = "C:/windows/system32/drivers/etc/hosts"
    elif "linux" in sys.platform:
        path = "/etc/hosts"
    elif sys.paltform == "darwin":
        path = "etc/hosts"
        

if __name__ == "__main__":
    writelog()
