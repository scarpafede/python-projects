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


def filtro_high(percorso_filein):
    """
    Restituisce le linee con livello di rischio "High"
    """
    with open(percorso_filein, 'r') as filein:
        file_righe_high = []
        line = filein.readline().strip()
        while line != '':
            security_level = line.split(";")[15]
            if security_level == "High":
                file_righe_high.append(line)
            line = filein.readline().strip()
        return file_righe_high


def converter_csv_to_html(percorso_csv, percorso_html):
    """
    Converte un file csv in un file html, dati i due percorsi.
    """
    with open(percorso_html, 'w') as file_html:
        file_html.write('<!DOCTYPE html>\n')
        file_html.write('<html>\n')

        file_html.write("<head>\n")
        file_html.write("   <title>Cybersecurity attacks</title>\n")
        file_html.write("</head>\n")

        linee_con_lvl_high = filtro_high(percorso_csv)

        file_html.write("<body>\n")
        file_html.write("   <table>\n")
        file_html.write("       <thead>\n")
        file_html.write("            <tr><th>linea con livello high</th></tr>\n")
        file_html.write("       </thead>\n")

        for i in range(len(linee_con_lvl_high)):
            file_html.write("               <tr><td>" + linee_con_lvl_high[i] + "</td></tr>\n")

        file_html.write("   </table>\n")
        file_html.write("</body>\n")

        file_html.write('</html>\n')


def main():
    logmessage()
    converter_csv_to_html("../flussi/cybersecurity_attacks.csv", "../flussi/cybersecurity_attacks.html")
    
if __name__ == "__main__":
    main()