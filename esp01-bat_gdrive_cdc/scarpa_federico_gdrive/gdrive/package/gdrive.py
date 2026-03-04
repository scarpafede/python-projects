import time
import sys
import os
from platform import node

"""
Nome programma: gdrive.py
Autore: Scarpa Federico
Descrizione: il programma estrae il terzo e il sesto elemento per ogni riga del file in ingresso,
                creando e scrivendo su un file bat il risultato.
                Il file in ingresso si chiama "drivecondivisi_id.txt" e si trova nella directory "flussi".
"""


def logmessage():
    """
    Scrive sul file di log varie informazioni sull'esecuzione, tra cui:
    il timestamp di esecuzione, il nome del computer, la platform di
    esecuzione e il nome del programma
    """
    messaggio_finale = '\n'

    timestamp = str(time.time())
    messaggio_finale += timestamp + '; '

    platform = sys.platform
    if platform == "darwin":
        nome_computer = node()
    elif platform == "win32":
        nome_computer = os.environ.get("COMPUTERNAME")
    elif "linux" in platform:
        nome_computer = node()
    messaggio_finale += nome_computer + '; '

    messaggio_finale += platform + '; '

    nome_programma = "gdrive.py"
    messaggio_finale += nome_programma
	
    flog = open("../log/execute.log", "a")
    flog.write(messaggio_finale)
    flog.close()
	

def main():
    logmessage()

    filedrivec = open("../flussi/drivecondivisi_id.txt", "r")
    lines = filedrivec.readlines()
    filedrivec.close()

    for line in lines:
         linesplit_id = line.rsplit(" ")
         identificativo = linesplit_id[6]
         identificativo = identificativo.strip()
         classe = (linesplit_id[3]).lower()

         stringafinale = "GAM user " + classe + "@marconiverona.edu.it " +"add drivefileacl " + identificativo + " role editor denyfile\n"
         
         filebat = open("creategdrivecdc.bat", "a")
         filebat.write(stringafinale)
         filebat.close()


if __name__ == "__main__":
        main()
