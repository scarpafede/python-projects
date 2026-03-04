"""
Nome programma: gdrive.py
Autore: Tosi Giacomo
Descrizione: programma che dato in ingresso il file dei drive condivisi, compone le righe del file batch
"""

import time
import sys
import platform
import os

def log(elab):
    '''
    Funzione che scrive sul file di log
    '''
    log = open("../log/execute.log", 'a')
    log.write(elab)
    log.close()


def nomepc():
    """
    Ritorna il nome dell'host su cui e' eseguito il programma
    """
    nomepc = ''
    if so() == 'darwin':
        nomepc = platform.node()
    elif so() == 'win32':
        nomepc = os.getenv('COMPUTERNAME')
    elif 'linux' in so():
        nomepc = os.environ.get('HOSTNAME')
    else:
        nomepc = "Siamo dispiaciuti, ma la sua platform non è riconosciuta"
    return nomepc


def tempo():
    """
    Ritorna in un'unica riga l'ora in versione non user friendly
    """
    timestamp = str(time.time())
    return timestamp


def so():
    '''
    Funzione che individua in quale platform viene eseguito il programma
    '''
    so = sys.platform
    return so


def contenuto_log():
    '''
    Funzione che compone il contenuto del file di log
    '''
    log(tempo() + ";")
    log(nomepc() + ";")
    log(so() + '\n')



def main():
    contenuto_log()


if __name__ == "__main__":
    main()
