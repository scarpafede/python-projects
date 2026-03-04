import time
import sys
import os


"""
Nome programma: hosts.py
Autore: Scarpa Federico
Descrizione: il programma visualizza il contenuto del file hosts privato delle linee con '#' e
                traccia la sua l'esecuzione nel file execute.log
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
    il timestamp di esecuzione, il nome del computer, la platform di esecuzione,
    il nome del programma e il numero di righe senza commento presenti nel file hosts.
    """
    messaggio_finale = ''

    timestamp = str(time.time())
    messaggio_finale += timestamp + '; '

    computer = os.getenv("COMPUTERNAME")
    messaggio_finale += computer + '; '

    platform = sys.platform
    messaggio_finale += platform + '; '

    nome_programma = "hosts.py"
    messaggio_finale += nome_programma + '; '

    altro = "descrizione:azione"
    messaggio_finale += altro + '; '

    conto_righe_senza_commento = 0
    f1 = open(percorso(), 'r')
    lines = f1.readlines()
    for line in lines:
        if line[0] != '#':
            conto_righe_senza_commento += 1
    f1.close()
    messaggio_finale += str(conto_righe_senza_commento) + "\n"

    return messaggio_finale


def writelog():
    """
    Chiama la funzione log, passandole il contenuto della funzione 'messaggio()'
    """
    log(messaggio())


def percorso():
    """
    La funzione restituisce il percorso del file hosts in base alla platform di utilizzo
    """
    platform = sys.platform
    if platform == "win32":
        path = "c:/windows/system32/drivers/etc/hosts"
    elif "linux" in platform:
        path = "/etc/hosts"
    elif platform == "darwin":
        path = "/etc/hosts"
    return path


def main():
    """
    Funzione - Programma principale
    """
    writelog()
    f1 = open(percorso(), 'r')
    lines = f1.readlines()
    for line in lines:
        if '#' not in line:
            print(line.strip())
    f1.close()


if __name__ == "__main__":
    main()
