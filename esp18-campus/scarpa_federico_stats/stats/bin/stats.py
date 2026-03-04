"""
Nome programma: stats.py
Autore: Scarpa Federico
Descrizione: il programma inserisce in un db i dati di un file excel.
"""


#import openpyxl
import time
import sys
import os
from platform import node
import sqlite3
import pandas as pd
import shutil as sh


def trace_stats():
    """
    Scrive sul trace il timestamp di esecuzione,
    il nome del computer, la platform di esecuzione
    e il nome del programma.
    """
    percorso_filetrace = "../log/stats.log"
    messaggio_finale = ''
    timestamp = str(time.time())
    messaggio_finale += f'{timestamp};'
    platform = sys.platform
    if platform == "darwin" or "linux" in platform:
        nome_computer = node()
    elif platform == "win32":
        nome_computer = os.environ.get("COMPUTERNAME")
    messaggio_finale += f'{nome_computer};'
    messaggio_finale += f'{platform};'
    nome_programma = os.path.basename(__file__)
    messaggio_finale += f'{nome_programma};'
    with open(percorso_filetrace, 'a') as ftrace:
        ftrace.write(f'{messaggio_finale}\n')


def sheet1(dati_quiz):
    """
    Restituisce una lista di elementi a partire da un DataFrame
    """
    list1 = []
    nome_quiz = dati_quiz['Nome quiz'].iloc[0]
    nome_corso = dati_quiz['Nome corso'].iloc[0]
    apertura = dati_quiz['Apertura'].iloc[0]
    list1.append(nome_quiz), list1.append(nome_corso)
    list1.append(apertura)
    return list1


def sheet2(dat_risp_qz, indice, riga):
    """
    Restituisce una lista di elementi a partire da un DataFrame
    """
    list2 = []
    q = int(dat_risp_qz['Q#'].iloc[indice])
    tipo_domanda = dat_risp_qz['Tipo di domanda'].iloc[indice]
    nome_domanda = dat_risp_qz['Nome della domanda'].iloc[indice]
    tentativi = int(dat_risp_qz['Tentativi'].iloc[indice])
    indice_abilita = dat_risp_qz['Indice di abilità'].iloc[indice]
    dev_stan = dat_risp_qz['Deviazione standard'].iloc[indice]
    ind_caso = dat_risp_qz['Indice delle risposte date a caso'].iloc[indice]
    peso_previsto = dat_risp_qz['Peso previsto'].iloc[indice]
    peso_eff = dat_risp_qz['Peso effettivo'].iloc[indice]
    ind_discr = dat_risp_qz['Indice di discriminazione'].iloc[indice]
    eff_discr = dat_risp_qz['Efficienza discriminante'].iloc[indice]

    # Creazione lista
    list2.append(q), list2.append(tipo_domanda)
    list2.append(nome_domanda), list2.append(tentativi)
    list2.append(indice_abilita), list2.append(dev_stan)
    list2.append(ind_caso), list2.append(peso_previsto)
    list2.append(peso_eff), list2.append(ind_discr)
    list2.append(eff_discr)

    return list2


def controllo_file():
    """
    Restituisce i percorsi dei file passati da linea
    comando e controlla la loro esistenza.
    Scrive su schermo un avviso se i file non esistono.
    """
    percorso_file_trovati = []
    if len(sys.argv) == 2:
        nome_file_excel = sys.argv[1]
        percorso_file_excel = f'../flussi/{nome_file_excel}'
        if os.path.exists(percorso_file_excel):
            percorso_file_trovati.append(percorso_file_excel)
        else:
            print(f'Nessun file "{nome_file_excel}" trovato.')
            sys.exit()
    else:
        # Scandisce tutti i file nella cartella flussi
        for file in os.listdir('../flussi/'):
        # Controlla se il file ha estensione .xlsx
            if file.endswith('.xlsx'):
            # Aggiunge quelli trovati alla lista
                percorso_file_trovati.append(f'../flussi/{file}')
        if len(percorso_file_trovati) == 0:
            print("Nessun file trovato con estensione .xlsx")
            sys.exit()
    return percorso_file_trovati


def main():
    percorso_file_trovati = controllo_file()
    file_stats_sql = open("../db/stats.sql", "w")
    
    conn = sqlite3.connect("../db/stats.db")
    cur = conn.cursor()
    
    cur.execute("DROP TABLE IF EXISTS stats_moodle")
    cr_tb = 'CREATE TABLE stats_moodle ("NOME QUIZ" TEXT, '
    cr_tb += '"NOME CORSO" TEXT, '
    cr_tb += '"APERTURA" TEXT, Q INTEGER, "TIPO DI DOMANDA" TEXT, '
    cr_tb += '"NOME DOMANDA" TEXT, TENTATIVI INTEGER, '
    cr_tb += '"INDICE DI ABILITÀ" TEXT, '
    cr_tb += '"DEVIAZIONE STANDARD" TEXT, '
    cr_tb += '"INDICE DELLE RISPOSTE DATE A CASO" TEXT, '
    cr_tb += '"PESO PREVISTO" TEXT, "PESO EFFETTIVO" TEXT, '
    cr_tb += '"INDICE DI DISCRIMINAZIONE" TEXT, '
    cr_tb += '"EFFICIENZA DISCRIMINANTE" TEXT)'
    cur.execute(cr_tb)


    for percorso_file_excel in percorso_file_trovati:
        # Crea il dataset con il contenuto del primo foglio del file excel
        dati_quiz = pd.read_excel(percorso_file_excel, sheet_name=0)
        l1 = sheet1(dati_quiz)

        # Crea il dataset con il contenuto del secondo foglio del file excel
        dati_risposte_quiz = pd.read_excel(percorso_file_excel, sheet_name=1)

        for indice, riga in dati_risposte_quiz.iterrows():
            l2 = sheet2(dati_risposte_quiz, indice, riga)
            str_sql = f'INSERT INTO stats_moodle VALUES ('
            str_sql +=  f'"{l1[0]}","{l1[1]}","{l1[2]}",{l2[0]},"{l2[1]}",'
            str_sql += f'"{l2[2]}",{l2[3]},"{l2[4]}","{l2[5]}",'
            str_sql += f'"{l2[6]}","{l2[7]}","{l2[8]}","{l2[9]}","{l2[10]}")'
            file_stats_sql.write(str_sql + '\n')
            cur.execute(str_sql)
            conn.commit()

        os.rename(percorso_file_excel, f'{percorso_file_excel}.bak')
        sh.move(f'{percorso_file_excel}.bak', "../flussi_bak")
        # Spostare i file nella cartella flussi_bak
    file_stats_sql.close()


if __name__ == "__main__":
    main()
    trace_stats()
