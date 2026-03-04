"""
Nome programma: xml.py
Autore: Scarpa Federico
Descrizione: il programma crea un file xml a partire da uno csv.
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
	
    flog = open("../log/execute.log", "a")
    flog.write(messaggio_finale)
    flog.close()


def ordered_xml_tags(lista_argomenti, ordinamento, tag_principale):
    """
    Restituisce una stringa ordinata di tag e dati, partendo da una lista di argomenti,
    secondo un ordinamento fornito e un tag principale, che andra' a contenere gli altri.
    """
    tag_list = ''

    tag_list += "<" + tag_principale + ">" +'\n'

    for i in range(len(ordinamento)):
        tag_list += "   <" + ordinamento[i] + ">" +'\n'
        tag_list += "   " + lista_argomenti[i] + '\n'
        tag_list += "   </" + ordinamento[i] + ">" +'\n'

    tag_list += "</" + tag_principale + ">" +'\n'

    return tag_list


def converter_csv_to_xml(percorso_csv, percorso_xml, ripetitive_element):
    """
    Converte un file csv in un file xml, dati i due percorsi e un elemento ripetitivo.
    """
    with (open(percorso_csv, 'r') as file_csv,
          open(percorso_xml, 'w')as file_xml):
        
        file_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')

        first_line_file_csv = file_csv.readline().strip()
        lines_file_csv = file_csv.readlines()[0:]
        ordinamento_file_csv = first_line_file_csv.split(',')

        for csv_line in lines_file_csv:
            final_xml_message = ''
            csv_splitted_line = csv_line.strip().split(',')
            final_xml_message += ordered_xml_tags(csv_splitted_line, ordinamento_file_csv, ripetitive_element)
            file_xml.write(final_xml_message)


def main():
    logmessage()
    converter_csv_to_xml("../flussi/users_anagr.csv", "../flussi/users.xml", "user")


if __name__ == "__main__":
    main()
