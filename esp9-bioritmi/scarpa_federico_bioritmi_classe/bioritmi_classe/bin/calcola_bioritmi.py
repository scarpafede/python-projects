"""
Nome programma: calcola_bioritmi.py
Autore: Scarpa Federico
Descrizione: il programma scrive su un csv i bioritmi e il nome di
             ogni alunno presente nel csv di ingresso.
"""


import math
import datetime
import time
import sys
import os
from platform import node


def logmessage():
    """
    Scrive sul file di log varie informazioni sull'esecuzione, tra cui:
    il timestamp di esecuzione, il nome del computer, la platform di
    esecuzione e il nome del programma.
    """
    messaggio_finale = ''

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

    nome_programma = os.path.basename(__file__)
    messaggio_finale += nome_programma
	
    flog = open("../log/trace.log", "a")
    flog.write(messaggio_finale + '\n')
    flog.close()


def calculate_biorhythm(birthdate, target_date):
    """
    Restituisce una tupla contenente i bioritmi,
    calcolati da due date fornite come argomento.
    """
    physical = math.sin((target_date - birthdate).days / 23) * 100
    emotional = math.sin((target_date - birthdate).days / 28) * 100
    intellectual = math.sin((target_date - birthdate).days / 33) * 100

    return physical, emotional, intellectual


def main(percorso_filein, percorso_fileout):
    with (open(percorso_filein, 'r') as filein,
          open(percorso_fileout, 'w') as fileout):
         
         fileout.write("Cognome,Nome,Bioritmo Fisico,Bioritmo Emotivo,Bioritmo Intellettuale,Data del calcolo\n")
         lines_filein = filein.readlines()

         for line in lines_filein:
            dati_filein = line.strip().split(",")

            fileout.write(dati_filein[1] + ',')
            fileout.write(dati_filein[2] + ',')

            data_nascita = (dati_filein[3].replace(" 00:00", '')).split("/")
            data_nascita_bioritmi = f"{data_nascita[2]}-{data_nascita[1]}-{data_nascita[0]}"
            data_nascita_bioritmi = datetime.datetime.strptime(data_nascita_bioritmi, '%Y-%m-%d')

            target_date = time.strftime('%Y-%m-%d')
            target_date_corretta = datetime.datetime.strptime(target_date, '%Y-%m-%d')

            bioritmi = calculate_biorhythm(data_nascita_bioritmi, target_date_corretta)
            fileout.write(f"{bioritmi[0]},{bioritmi[1]},{bioritmi[2]}")
            fileout.write(',' + target_date + '\n')


if __name__ == "__main__":
    logmessage()
    main("../flussi/alunni_4aa.csv","../flussi/bioritmi_classe.csv")
