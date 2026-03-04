"""
Nome programma: sync.py
Autore: Scarpa Federico
Descrizione: - il programma confronta due file e scrive su un file bat
                gli elementi del primo non presenti nel secondo.
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

    with (open("../flussi/users_anagr.csv", "r") as fileanagr,
        open("../flussi/users_google.csv", "r") as filegoogle,
        open("../bat/sync.bat", "w") as filebat):

        filebat.write("@ECHO OFF\n")
        filebat.write("REM Il programma e' l'esito di un confronto tra due file, che ha scritto su tale bat le differenze\n")

        lines_fileanagr = fileanagr.readlines()[1:]
        lines_filegoogle = filegoogle.readlines()[1:]

        matricola_google = []
        lista_matr_google = []
        matricola_anagr = []
        lista_matr_anagr = []

        for line in lines_fileanagr:
             matricola_anagr = line.split(",")[0]
             lista_matr_anagr += matricola_anagr
        # creazione lista matricole presenti in anagrafica

        for linea in lines_filegoogle:
            matricola_google = linea.split(",")[2].split("@")[0]
            lista_matr_google += matricola_google
        # creazione lista matricole presenti nel file di google

        for i in lista_matr_anagr:
            if i not in lista_matr_google:
                filebat.write(i)
        # confronto tra le due liste e scrittura sul file bat


if __name__ == "__main__":
    main()
