"""
Nome programma: spotify.py
Autore: Scarpa Federico
Descrizione: il programma crea un db con i dati di spotify.sql
"""


import time
import sys
import os
from platform import node
import sqlite3


def trace():
    """
    Scrive sul trace il timestamp di esecuzione,
    il nome del computer, la platform di esecuzione
    e il nome del programma.
    """
    messaggio_finale = ''

    timestamp = str(time.time())
    messaggio_finale += timestamp + ';'

    platform = sys.platform
    if platform == "darwin":
        nome_computer = node()
    elif platform == "win32":
        nome_computer = os.environ.get("COMPUTERNAME")
    elif "linux" in platform:
        nome_computer = os.environ.get('HOSTNAME')
    messaggio_finale += nome_computer + ';'

    messaggio_finale += platform + ';'

    nome_programma = os.path.basename(__file__)
    messaggio_finale += nome_programma + ';'
	
    ftrace = open("../log/trace.log", "a")
    ftrace.write(messaggio_finale + '\n')
    ftrace.close()


def gestione_input():
    """
    Termina l'esecuzione se sono rispettate le condizioni elencate:
    - len(sys.argv) > 2
    - len(sys.argv) == 2 e sys.argv[1] != 'create'
    """
    if len(sys.argv) > 2:
        print("Errore: e' necessario fornire gli argomenti strattamente necessari")
        sys.exit()
    if len(sys.argv) == 2 and sys.argv[1] != 'create':
        print("Errore: il primo argomento puo' essere solamente -create-")
        sys.exit()


def main():
    gestione_input()
    conn = sqlite3.connect("../db/spotify.db") # connessione al db sqlite (se mysql immettere ip e porta)
    cur = conn.cursor() # puntatore al database, alla connessione
    
    try:
        if sys.argv[1] == 'create':
            cur.execute("DROP TABLE IF EXISTS spotify") # cancellazione tabella esistente se presente
            cur.execute("CREATE TABLE spotify (num, name, album, release_date, track_number, uri)")
            conn.commit() # confermare l'operazione
    except:
        pass
    
    spsql = open("../flussi/spotify.sql")
    lines_spsql = spsql.readlines()
    for line in lines_spsql:
        cur.execute(line)
    conn.commit()

    logfile = open("../log/log.log", 'w')
    for row in cur.execute("SELECT name, release_date, uri FROM spotify ORDER BY name ASC"): # select
        logfile.write(str(row) + '\n') # scrittura su log.log
    logfile.close()


if __name__ == "__main__":
    main()
    trace()
