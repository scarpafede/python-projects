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


def controllo_input():
    """
    Termina l'esecuzione se e' rispettata la condizione sotto elencata.
    """
    if len(sys.argv) != 2:
        print("E' necessario fornire solamente gli argomenti necessari")
        sys.exit()


def stats_quiz(ds_quiz):
    """
    Visualizza il dataset con le informazioni sul quiz dove:
        'Nome quiz'       nome colonna
        iloc[0]           indice riga con il valore della colonna
    """
    print(ds_quiz['Nome quiz'].iloc[0])
    print(ds_quiz['Nome corso'].iloc[0])
    #print(ds_quiz['Apertura'].iloc[0])
    #print(ds_quiz['Numero di primi tentativi completati e valutati'].iloc[0])
    #print(ds_quiz['Voto medio dei primi tentativi'].iloc[0])
    #print(ds_quiz['Media delle valutazioni degli ultimi tentativi'].iloc[0])


def stats_domande_quiz(ds_risposte_quiz):
    """
    Visualizza il dataset con le stats delle domande indicandone le colonne e le righe:
        ds_risposte_quiz['Q#']    la colonna
        la riga iloc[indice]
    """
    for indice, riga in ds_risposte_quiz.iterrows():
        # Elabora la riga 1
        if True == True:
            print(ds_risposte_quiz['Q#'].iloc[indice])
            print(ds_risposte_quiz['Tipo di domanda'].iloc[indice])
            print(ds_risposte_quiz['Nome della domanda'].iloc[indice])
            print(ds_risposte_quiz['Tentativi'].iloc[indice])
            print(ds_risposte_quiz['Indice di abilità'].iloc[indice])
            print(ds_risposte_quiz['Deviazione standard'].iloc[indice])
            print(ds_risposte_quiz['Indice delle risposte date a caso'].iloc[indice])
            print(ds_risposte_quiz['Peso previsto'].iloc[indice])
            print(ds_risposte_quiz['Peso effettivo'].iloc[indice])
            print(ds_risposte_quiz['Indice di discriminazione'].iloc[indice])
            print(ds_risposte_quiz['Efficienza discriminante'].iloc[indice])
            print()


def main():
    #controllo_input()
    percorso_file_excel = '../flussi/q1.xlsx'
    conn = sqlite3.connect("../db/stats.db")
    cur = conn.cursor()

    # Crea il dataset con il contenuto del primo foglio del file excel
    dati_quiz = pd.read_excel(percorso_file_excel, sheet_name=0)

    nome_quiz = str(dati_quiz['Nome quiz'].iloc[0])
    nome_corso = dati_quiz['Nome corso'].iloc[0]
    #apertura = dati_quiz['Apertura'].iloc[0]
    #num_primi_tent_compl_valut = dati_quiz['Numero di primi tentativi completati e valutati'].iloc[0]
    #voto_medio_primi_tent = dati_quiz['Voto medio dei primi tentativi'].iloc[0]
    #media_val_ultim_tent = dati_quiz['Media delle valutazioni degli ultimi tentativi'].iloc[0]

    # Crea il dataset con il contenuto del secondo foglio del file excel
    dati_risposte_quiz = pd.read_excel(percorso_file_excel, sheet_name=1)

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

        #cur.execute(f'INSERT INTO stats_moodle VALUES ('{nome_quiz}','{nome_corso}',{q},{tipo_domanda},{nome_domanda},{tentativi},{indice_abilita},{dev_stan},{ind_caso},{peso_previsto},{peso_eff},{ind_discr},{eff_discr})')
        cur.execute('DROP TABLE IF EXISTS stats_moodle')
        conn.commit()


    # Visualizza dati del quiz
    #stats_quiz(dati_quiz)
    # Visualizza dati delle domande del quiz
    #stats_domande_quiz(dati_risposte_quiz)


if __name__ == "__main__":
    main()
    trace_stats()
