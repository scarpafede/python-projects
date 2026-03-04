"""
Nome programma: spotify.py
Autore: Scarpa Federico
Descrizione: il programma crea e inserisce 3 righe nel db spotify.db .
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


def main():
    conn = sqlite3.connect("../db/spotify.db") # connessione al db sqlite (se mysql immettere ip e porta)
    cur = conn.cursor() # puntatore al database, alla connessione
    try:
        cur.execute("DROP TABLE spotify") # cancellazione tabella esistente
    except:
        pass
    cur.execute("CREATE TABLE spotify (num, name, album, release_date, track_number, uri)") # create table
    conn.commit() # confermare l'operazione

    cur.execute("""INSERT INTO spotify VALUES
                (0,'Welcome To New York (Taylor`s Version)','1989 (Taylor`s Version) [Deluxe]',
                '27/10/2023',1,'spotify:track:4WUepByoeqcedHoYhSNHRt'),
                (1,'Blank Space (Taylor`s Version)','1989 (Taylor`s Version) [Deluxe]',
                '27/10/2023',2,'spotify:track:0108kcWLnn2HlH2kedi1gn'),
                (2,'Style (Taylor`s Version)','1989 (Taylor`s Version) [Deluxe]',
                '27/10/2023',3,'spotify:track:3Vpk1hfMAQme8VJ0SNRSkd')""")
    conn.commit()

    logfile = open("../log/log.log", 'w')
    for row in cur.execute("SELECT name, release_date, uri FROM spotify"): # select
        logfile.write(str(row) + '\n') # scrittura su log.log
    logfile.close()


if __name__ == "__main__":
    main()
    trace()

