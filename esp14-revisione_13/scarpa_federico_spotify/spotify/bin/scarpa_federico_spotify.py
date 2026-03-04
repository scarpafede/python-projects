"""
Nome programma: spotify.py
Autore: Scarpa Federico
Descrizione: il programma per ogni riga del file csv produce una riga nel file sql.
"""


import time
import sys
import os
from platform import node


def trace(linee_tot, linee_eseg):
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

    messaggio_finale += str(linee_tot) + ';' + str(linee_eseg)
	
    ftrace = open("../log/trace.log", "a")
    ftrace.write(messaggio_finale + '\n')
    ftrace.close()


def main():
    
    percorso_filein = "../flussi/taylor_swift_spotify.csv"
    percorso_filesql = "../flussi/spotify.sql"
    percorso_log = "../log/log.log"

    with (open(percorso_filein, 'r') as filein,
          open(percorso_filesql, 'w') as filesql,
          open(percorso_log, 'w') as filelog):
         
         conto_linee_scritte = 0
         lines_filein = filein.readlines()[1:]
         linee_totali = len(lines_filein)
         
         try:
            for line in lines_filein:
                dati_filein = line.replace("'","`").strip().split(",")
                sql_line = (f"INSERT INTO T1 ({dati_filein[0]},'{dati_filein[1]}','{dati_filein[2]}','{dati_filein[3]}',{dati_filein[4]},'{dati_filein[6]}')\n")
                filesql.write(sql_line)
                filelog.write(sql_line)
                conto_linee_scritte += 1
         except:
             pass

         trace(linee_totali, conto_linee_scritte)


if __name__ == "__main__":
    main()
