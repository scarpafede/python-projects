"""
Nome programma: gdrive.py
Autore: Scarpa Federico
Descrizione: il programma estrae il terzo e il sesto elemento per ogni riga del file in ingresso,
                creando e scrivendo su un file bat un comando combinato ad essi.
                Il file in ingresso si chiama "drivecondivisi_id.txt" e si trova nella directory "flussi".
"""


import time
import sys
import os
from platform import node


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


def changename_date(filein):
     """
     Aggiunge al nome del file in input la data e l'ora correnti
     """
     current_time = time.localtime()

     formatted_time = time.strftime("%Y-%m-%d_%H-%M", current_time)
     # questa linea serve a mettere in ordine la data nel formato desiderato

     filenew = filein.split(".")[0] + "_" + formatted_time + "." + filein.split(".")[1]     

     os.rename(filein, filenew)


def main():
    logmessage()
    
    """
    filebat = open("creadrives.bat", "a")
    filedrivec = open("../flussi/drivecondivisi_id.txt", "r")
    """

    if os.path.exists("./creadrives.bat"):
        changename_date("creadrives.bat")

    with (open("creadrives.bat", "w") as filebat,
        open("../flussi/drivecondivisi_id.txt", "r") as filedrivec):
        
        lines = filedrivec.readlines()
        filebat.write("@ECHO OFF\n")
        filebat.write("REM File batch che modifica il ruolo dell'user in google workspace\n")

        for line in lines:
             linesplit = line.split(" ")
             identificativo = linesplit[6].strip()
             cdc_classe = (linesplit[3]).lower().replace("-", ".")

             stringafinale = "GAM user " + cdc_classe + "@marconiverona.edu.it " +"add drivefileacl " + identificativo + " role editor denyfile\n"
             
             filebat.write(stringafinale)


if __name__ == "__main__":
    main()
