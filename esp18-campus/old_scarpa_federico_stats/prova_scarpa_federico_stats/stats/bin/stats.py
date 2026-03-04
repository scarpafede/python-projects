"""
Nome programma: stats.py
Autore: Scarpa Federico
Descrizione: il programma inserisce in un db i dati provenienti da un file excel.
"""


import time
import sys
import os
from platform import node
import sqlite3
import pandas as pd
import openpyxl


def trace_stats():
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
	
    ftrace = open("../log/stats.log", "a")
    ftrace.write(messaggio_finale + '\n')
    ftrace.close()


def spazio(stringa):
    """
    Restituisce la stringa tra virgolette, se contiene uno spazio
    """
    if ' ' in stringa:
        return f'"{stringa}"'


def main():
    percorso_file_excel = "../flussi/q1.xlsx"
    
    """
    if len(sys.argv) == 2:
        percorso_file_excel = sys.argv[1]
    else:
        file_trovati = []
        # Scandisce tutti i file nella cartella flussi
        for file in os.listdir('../flussi/'):
        # Controlla se il file ha l'estensione .xlsx
            if file.endswith('.xlsx'):
            # Aggiunge quelli trovati alla lista
                file_trovati.append(f'../flussi/{file}')
        if len(file_trovati) == 0:
            print("Nessun file trovato con l'estensione .xlsx")
            sys.exit()
    for percorso_file_excel in file_trovati:
        pass
        #print("exec")
    """

    conn = sqlite3.connect("../db/stats.db")
    cur = conn.cursor()

    # Crea il dataset con il contenuto del primo foglio del file excel
    dati_quiz = pd.read_excel(percorso_file_excel, sheet_name=0)
    # Crea il dataset con il contenuto del secondo foglio del file excel
    dati_risposte_quiz = pd.read_excel(percorso_file_excel, sheet_name=1)

    at_tab = ['Nome quiz','Nome corso','Apertura','Q#','Tipo di domanda']
    at_tab.append('Nome della domanda'), at_tab.append('Tentativi')
    at_tab.append('Indice di abilità'), at_tab.append('Deviazione standard')
    at_tab.append('Indice delle risposte date a caso'), at_tab.append('Peso previsto')
    at_tab.append('Peso effettivo'), at_tab.append('Indice di discriminazione')
    at_tab.append('Efficienza discriminante')

    #nome_quiz = dati_quiz['Nome quiz'].iloc[0]
    #nome_corso = dati_quiz['Nome corso'].iloc[0]
    #apertura = dati_quiz['Apertura'].iloc[0]

    lista_foglio1 = []
    for index in range(3):
        # Prendere da "dati_quiz" l'elemento in posizione "index" della lista "at_tab"
        var = dati_quiz[at_tab[index]].iloc[0]
        var = spazio(var)
        lista_foglio1.append(var)
    
    for indice, riga in dati_risposte_quiz.iterrows():
        q = int(dati_risposte_quiz['Q#'].iloc[indice])
        tipo_domanda = dati_risposte_quiz['Tipo di domanda'].iloc[indice]
        nome_domanda = dati_risposte_quiz['Nome della domanda'].iloc[indice]
        tentativi = int(dati_risposte_quiz['Tentativi'].iloc[indice])
        indice_abilita = dati_risposte_quiz['Indice di abilità'].iloc[indice]
        dev_stan = dati_risposte_quiz['Deviazione standard'].iloc[indice]
        ind_caso = dati_risposte_quiz['Indice delle risposte date a caso'].iloc[indice]
        peso_previsto = dati_risposte_quiz['Peso previsto'].iloc[indice]
        peso_eff = dati_risposte_quiz['Peso effettivo'].iloc[indice]
        ind_discr = dati_risposte_quiz['Indice di discriminazione'].iloc[indice]
        eff_discr = dati_risposte_quiz['Efficienza discriminante'].iloc[indice]

        cur.execute('DROP TABLE IF EXISTS stats_moodle')
        cur.execute('CREATE TABLE stats_moodle ("NOME QUIZ", "NOME CORSO", "APERTURA")')
        cur.execute(f'INSERT INTO stats_moodle VALUES ()')

        #cur.execute(f'INSERT INTO stats_moodle VALUES ("{nome_quiz}","{nome_corso}","{apertura}",{q},"{tipo_domanda}","{nome_domanda}",{tentativi},"{indice_abilita}","{dev_stan}","{ind_caso}","{peso_previsto}","{peso_eff}","{ind_discr}","{eff_discr}")')
        conn.commit()

    #os.rename(percorso_file_excel, f'{percorso_file_excel}.bak')


if __name__ == "__main__":
    main()
    trace_stats()

#cur.execute('DROP TABLE IF EXISTS stats_moodle')
#cur.execute('CREATE TABLE stats_moodle ("NOME QUIZ", "NOME CORSO", "APERTURA", Q, "TIPO DI DOMANDA", "NOME DOMANDA", TENTATIVI, "INDICE DI ABILITÀ", "DEVIAZIONE STANDARD", "INDICE DELLE RISPOSTE DATE A CASO", "PESO PREVISTO", "PESO EFFETTIVO", "INDICE DI DISCRIMINAZIONE", "EFFICIENZA DISCRIMINANTE")')
