"""
Nome programma: serverside.py
Autore: Scarpa Federico
Descrizione: il programma crea un file html a partire da uno csv.
"""

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

    nome_programma = os.path.basename(__file__)
    messaggio_finale += nome_programma
	
    flog = open("../log/trace.log", "a")
    flog.write(messaggio_finale)
    flog.close()


def convertitore_csv_html(percorso_csv, percorso_html):
    """
    Converte un file csv in un file html, dati i due percorsi.
    """
    with (open(percorso_csv, 'r') as file_csv,
          open(percorso_html, 'w')as file_html):
        
        linee_csv = file_csv.readlines()
        
        file_html.write('\n')
        file_html.write('<!DOCTYPE html>\n')
        file_html.write('<html>\n')
        file_html.write("<head>\n")
        file_html.write("<title>Cybersecurity attacks</title>\n")
        file_html.write("</head>\n")
        file_html.write("<body>\n")
        file_html.write("<table>\n")
        file_html.write("<thead>\n")
        file_html.write("<tr><th>Attacchi con rischio alto</th></tr>\n")
        file_html.write("</thead>\n")

        for line in linee_csv:
            pericolo = line.split(';')[15]
            if pericolo == "High":
                file_html.write("<tr><td>" + line.strip() + "</td></tr>\n")

        file_html.write("</table>\n")
        file_html.write("</body>\n")
        file_html.write('</html>\n')


def main():
    logmessage()
    convertitore_csv_html("../flussi/cybersecurity_attacks.csv", "../flussi/cybersecurity_attacks.html")


if __name__ == "__main__":
    main()
