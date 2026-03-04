import time
import sys
import os
from platform import node


"""
Nome programma: deploy.py
Autore: Scarpa Federico
Descrizione: il programma tiene traccia, sul file di log, della sua esecuzione
"""


def log(msg):
    """
    Apre e scrive in append su execute.log il 'msg'
    """
    f1 = open("../log/execute.log", "a")
    f1.write(msg)
    f1.close()


def messaggio():
    """
    Ritorna in un'unica riga informazioni sull'esecuzione, tra cui:
    il timestamp di esecuzione, il nome del computer, la platform di
    esecuzione e il nome del programma.
    """
    messaggio_finale = ''

    timestamp = str(time.time())
    messaggio_finale += timestamp + '; '

    messaggio_finale += nome_computer() + '; '

    platform = sys.platform
    messaggio_finale += platform + '; '

    nome_programma = "deploy.py"
    messaggio_finale += nome_programma + '; '

    return messaggio_finale


def nome_computer():
    """
    Restituisce il nome del computer in base alla platform di utilizzo
    """
    platform = sys.platform
    if platform == "darwin":
        return node()
    elif platform == "win32":
        return os.environ.get("COMPUTERNAME")
    elif "linux" in platform:
        return node()


def main():
    """
    Funzione - Programma principale
    """
    log(messaggio())


if __name__ == "__main__":
    main()
