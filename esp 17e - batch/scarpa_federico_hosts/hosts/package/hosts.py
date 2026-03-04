import time
import sys
import os
from platform import node


"""
Nome programma: hosts.py
Autore: Scarpa Federico
Descrizione: il programma crea una copia del file hosts, hosts.old in flussi;
                crea una copia del file hosts, hosts.new in flussi;
                aggiunge due righe a quest'ultimo.
"""


def copia():
    """
    Copia il contenuto del file hosts del computer,
    icollandolo in quello nominato hosts.old, nella cartella flussi.
    """
    file = open(percorso_file_hosts(), 'r')
    file2 = open("../flussi/hosts.old", "w")
    lines = file.readlines()
    for line in lines:
        file2.write(line)
    file.close()
    file2.close()


def copia_con_aggiunta():
    """
    Copia il contenuto del file hosts del computer,
    incollandolo in quello nominato hosts.new, nella cartella flussi;
    aggiunge anche due righe di informazioni.
    """
    file = open(percorso_file_hosts(), 'r')
    file2 = open("../flussi/hosts.new", "w")
    lines = file.readlines()
    for line in lines:
        file2.write(line)
    file2.write("127.0.0.1 www.google.it\n")
    file2.write("127.0.0.1 " + nome_computer())
    file.close()
    file2.close()


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

    messaggio_finale += nome_computer() + '; '

    platform = sys.platform
    messaggio_finale += platform + '; '

    nome_programma = "hosts.py"
    messaggio_finale += nome_programma + '; '

    conto_righe_senza_commento = -1
    f1 = open("../flussi/hosts", 'r')
    lines = f1.readlines()
    for line in lines:
        if '#' not in line:
            conto_righe_senza_commento += 1
    f1.close()
    messaggio_finale += str(conto_righe_senza_commento) + "\n"

    return messaggio_finale


def percorso_file_hosts():
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
    copia()
    copia_con_aggiunta()

    try:
        os.remove("../flussi/hosts.old")
        os.rename("../flussi/hosts.new", "../flussi/hosts")
    except:
        os.remove("../flussi/hosts")
        copia()
        copia_con_aggiunta()
        os.remove("../flussi/hosts.old")
        os.rename("../flussi/hosts.new", "../flussi/hosts")

    log(messaggio())


if __name__ == "__main__":
    main()
