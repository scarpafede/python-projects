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
    percorso_spotify_sql = "../flussi/spotify.sql"
    percorso_log = "../log/log.log"
    percorso_ddl_sql = "../flussi/ddl.sql"

    with (open(percorso_filein, 'r') as filein,
          open(percorso_spotify_sql, 'w') as filesql,
          open(percorso_log, 'w') as filelog,
          open(percorso_ddl_sql, 'w') as fileddl):
         
         conto_linee_scritte = 0
         fl = filein.readline()
         lines_filein = filein.readlines()
         linee_totali = len(lines_filein)
         
         fl = fl.strip().split(',')
         fileddl.write("DROP TABLE spotify\n")
         num = fl[0]
         if len(num.strip()) == 0:
            attr1 = "num"
         else:
            attr1 = fl[0]
        
         fileddl.write(f"CREATE TABLE spotify ({attr1} CHAR(255),{fl[1]} CHAR(255),{fl[2]} CHAR(255),{fl[3]} CHAR(255),{fl[4]} CHAR(255),{fl[5]} CHAR(255),{fl[6]} CHAR(255))\n")

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
