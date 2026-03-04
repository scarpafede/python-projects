"""
Nome programma: bioritmi.py
Autore: Pasetto Alessandro, Scarpa Scarpa Scarpa Scarpa Shoes Federico, Tosi Giacomo
Descrizione: programma che calcola i bioritmi
"""


import os
import sys
import math
import time
import datetime
import platform 


def log(elab):
    '''
    Scrive sul file di log il contenuto di elab.
    '''
    log = open("../log/trace.log", 'a')
    log.write(elab)
    log.close()


def nomepc():
    """
    Ritorna il nome dell'host su cui e' eseguito il programma.
    """
    nomepc = ''
    if so() == 'darwin':
        nomepc = platform.node()
    elif so() == 'win32':
        nomepc = os.getenv('COMPUTERNAME')
    elif 'linux' in so():
        nomepc = os.environ.get('HOSTNAME')
    else:
        nomepc = "Siamo dispiaciuti, ma la sua platform non è riconosciuta"
    return nomepc


def tempo():
    """
    Ritorna in un'unica riga l'ora in versione non user friendly.
    """
    timestamp = str(time.time())
    return timestamp


def so():
    '''
    Restituisce in quale platform viene eseguito il programma.
    '''
    so = sys.platform
    return so


def contenuto_log():
    '''
    Compone il contenuto del file di log.
    '''
    log(tempo() + ";")
    log(sys.argv[0] + ";")
    log(nomepc() + ";")
    log(so() + '\n')


def calculate_biorhythm(birthdate, target_date):
    """
    Restituisce una tupla contenente i bioritmi,
    calcolati da due date fornite come argomento.
    """
    physical = math.sin((target_date - birthdate).days / 23) * 100
    emotional = math.sin((target_date - birthdate).days / 28) * 100
    intellectual = math.sin((target_date - birthdate).days / 33) * 100

    return physical, emotional, intellectual


def gestione_input():
    """
    Termina l'esecuzione se sono rispettate le condizioni elencate:
    - len(sys.argv) != 3
    - len(sys.argv[1]) < 10
    - sys.argv[1][4] != '-' and sys.argv[1][7] != '-'
    - sys.argv[2].isnumeric() == False or int(sys.argv[2]) < 1
    """
    if len(sys.argv) != 3:
        print("E' necessario fornire data di calcolo e numero di giorni successivi")
        sys.exit()
    if len(sys.argv[1]) < 10:
        print("Fornire una data corretta rispettando il seguente formato: YYYY-MM-DD")
        sys.exit()
    if sys.argv[1][4] != '-' and sys.argv[1][7] != '-':
        print("Data inserita non valida")
        print("Il formato corretto: YYYY-MM-DD")
        sys.exit()
    if sys.argv[2].isnumeric() == False or int(sys.argv[2]) < 1:
        print("Fornire un numero di giorni successivi valido")
        sys.exit()


def passaggio_html():
    """
    Prende i dati dal file csv bioritmi_classe e li
    riporta in una tabella nel file bioritmi_classe.html .
    """
    filecsv = open("../flussi/bioritmi_classe.csv", 'r')
    prima_linea_splittata = filecsv.readline().strip().split(',')
    lines = filecsv.readlines()
    filecsv.close()

    with open("../html/bioritmi_classe.html", 'w') as filehtml:
        filehtml.write("<!DOCTYPE html>\n")
        filehtml.write("<html>\n")
        filehtml.write("<head>\n")
        filehtml.write("<style>\n")
        filehtml.write("table {\n")
        filehtml.write("  font-family: arial, sans-serif;\n")
        filehtml.write("  border-collapse: collapse;\n")
        filehtml.write("  width: 100%;\n")
        filehtml.write("}\n")
        filehtml.write("\n")
        filehtml.write("td, th {\n")
        filehtml.write("  border: 1px solid #dddddd;\n")
        filehtml.write("  text-align: left;\n")
        filehtml.write("  padding: 8px;\n")
        filehtml.write("}\n")
        filehtml.write("\n")
        filehtml.write("tr:nth-child(even) {\n")
        filehtml.write("  background-color: #dddddd;\n")
        filehtml.write("}\n")
        filehtml.write("</style>\n")
        filehtml.write("</head>\n")
        filehtml.write("<body>\n")
        filehtml.write("<h2>Bioritmi classe 4AA</h2>\n")
        filehtml.write("<table>\n")
        filehtml.write("  <tr>\n")
        filehtml.write("    <th>" + prima_linea_splittata[0] + "</th>\n")
        filehtml.write("    <th>" + prima_linea_splittata[1] + "</th>\n")
        filehtml.write("    <th>" + prima_linea_splittata[2] + "</th>\n")
        filehtml.write("    <th>" + prima_linea_splittata[3] + "</th>\n")
        filehtml.write("    <th>" + prima_linea_splittata[4] + "</th>\n")
        filehtml.write("  </tr>\n")
        for line in lines:
            splitted_line = line.strip().split(',')
            filehtml.write("  <tr>\n")
            filehtml.write("    <td>" + splitted_line[0] + "</td>\n")
            filehtml.write("    <td>" + splitted_line[1] + "</td>\n")
            filehtml.write("    <td>" + splitted_line[2] + "</td>\n")
            filehtml.write("    <td>" + splitted_line[3] + "</td>\n")
            filehtml.write("    <td>" + splitted_line[4] + "</td>\n")
            filehtml.write("  </tr>\n")
        filehtml.write("</table>\n")
        filehtml.write("</body>\n")
        filehtml.write("</html>\n")


def main():
    gestione_input()
    
    percorso_filein = "../flussi/alunni_4aa.csv"
    percorso_fileout = "../flussi/bioritmi_classe.csv"

    with (open(percorso_filein, 'r') as filein,
          open(percorso_fileout, 'w') as fileout):
         
         fileout.write("Matricola,Data del calcolo,Bioritmo Fisico,Bioritmo Emotivo,Bioritmo Intellettuale\n")
         lines_filein = filein.readlines()

         for line in lines_filein:
            dati_filein = line.strip().split(",")
            target_date = sys.argv[1]
            datetime_target_date = datetime.datetime.strptime(target_date, '%Y-%m-%d') # stringa > datetime
            timestamp_target_date = datetime.datetime.timestamp(datetime_target_date) # datetime > timestamp
            data_nascita = (dati_filein[3].replace(" 00:00", '')).split("/")

            for i in range(int(sys.argv[2])):
                partial_datetime_target_date = datetime.datetime.fromtimestamp(timestamp_target_date) # timestamp > datetime per funzione

                data_nascita_ordinata = f"{data_nascita[2]}-{data_nascita[1]}-{data_nascita[0]}"
                data_nascita_datetime = datetime.datetime.strptime(data_nascita_ordinata, '%Y-%m-%d')

                bioritmi = calculate_biorhythm(data_nascita_datetime, partial_datetime_target_date)
                
                fileout.write(dati_filein[0] + ',')
                data_formattata = time.strftime('%d/%m/%Y', time.localtime(timestamp_target_date)) # timestamp > stringa per csv
                fileout.write(data_formattata + ',')
                fileout.write(f"{bioritmi[0]:.2f},{bioritmi[1]:.2f},{bioritmi[2]:.2f}\n")

                timestamp_target_date += 86400.0 # incremento timestamp: passaggio alla data successiva
    
    passaggio_html()


if __name__ == "__main__":
    contenuto_log()
    main()
