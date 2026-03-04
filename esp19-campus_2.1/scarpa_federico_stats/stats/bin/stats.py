"""
Nome programma: stats.py
Autore: Scarpa Federico
Descrizione: il programma inserisce in un db dati di file excel.
"""


#import openpyxl
import time
import sys
import os
from platform import node
import sqlite3
import pandas as pd
import shutil as sh
from icecream import ic


def trace_stats(stato):
    """
    Scrive sul trace il timestamp di esecuzione,
    il nome del computer, la platform di esecuzione
    e il nome del programma.
    """
    percorso_filetrace = "../log/stats.log"
    messaggio_finale = ''
    tempo_uf = str(time.ctime())
    messaggio_finale += f'{tempo_uf};'
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
    messaggio_finale += stato
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


def sheet2(dat_risp_qz, indice):
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


def get_path_excel(lista_argv):
    """
    Restituisce i percorsi dei file excel
    a partire da una lista di argomenti.
    Termina il programma se non sono
    presenti file excel in flussi.
    """
    xlsx_non_trovati = True
    percorsi_file_trovati = []
    for argomento in lista_argv:
        if argomento.endswith('.xlsx'):
            xlsx_non_trovati = False
            percorso_file = f'../flussi/{argomento}'
            if os.path.exists(percorso_file):
                percorsi_file_trovati.append(percorso_file)
    if xlsx_non_trovati:
        percorsi_file_trovati = tutti_i_file_xlsx()
    if len(percorsi_file_trovati) == 0:
        print("Nessun file trovato con l'estensione specificata")
        sys.exit()
    return percorsi_file_trovati


def tutti_i_file_xlsx():
    """
    Restituisce la lista dei file excel trovati in flussi.
    """
    percorsi_file_trovati = []
    # Scandisce tutti i file nella cartella flussi
    for file in os.listdir('../flussi/'):
        # Controlla se il file ha estensione .xlsx
        if file.endswith('.xlsx'):
            # Aggiunge quelli trovati alla lista
            percorsi_file_trovati.append(f'../flussi/{file}')
    return percorsi_file_trovati


def main():
    lista_sys_argv = sys.argv[1:]

    if "verbose_true" in lista_sys_argv:
        ic.enable()
    elif "verbose_false" in lista_sys_argv:
        ic.disable()
    else:
        print("Parametro verbose non trovato: programma terminato")
        sys.exit()
    
    percorsi_file_excel = get_path_excel(lista_sys_argv)

    file_stats_sql = open("../db/stats.sql", "w")
    percorso_db = "../db/stats.db"
    percorso_ddl = "../db/ddl.sql"

    conn = sqlite3.connect(percorso_db)
    cur = conn.cursor()

    with open(percorso_ddl, 'r') as ddl:
        lines = ddl.readlines()
        for line in lines:
            cur.execute(line)

    for percorso_file_excel in percorsi_file_excel:
        # Crea il dataset con il contenuto del primo foglio del file excel
        dati_quiz = pd.read_excel(percorso_file_excel, sheet_name=0)
        l1 = sheet1(dati_quiz)
        ins_sh1 = 'INSERT INTO info_quiz VALUES ('
        ins_sh1 += f'"{l1[0]}","{l1[1]}","{l1[2]}")'
        file_stats_sql.write(ins_sh1 + '\n')
        cur.execute(ins_sh1)
        conn.commit()

        # Crea il dataset con il contenuto del secondo foglio del file excel
        dati_risposte_quiz = pd.read_excel(percorso_file_excel, sheet_name=1)

        for indice, riga in dati_risposte_quiz.iterrows():
            ic(riga)
            l2 = sheet2(dati_risposte_quiz, indice)
            ins_sh2 = 'INSERT INTO dati_quiz VALUES ('
            ins_sh2 +=  f'"{l1[0]}",{l2[0]},"{l2[1]}",'
            ins_sh2 += f'"{l2[2]}",{l2[3]},"{l2[4]}","{l2[5]}",'
            ins_sh2 += f'"{l2[6]}","{l2[7]}","{l2[8]}","{l2[9]}","{l2[10]}")'
            file_stats_sql.write(ins_sh2 + '\n')
            cur.execute(ins_sh2)
            conn.commit()

        os.rename(percorso_file_excel, f'{percorso_file_excel}.bak')
        sh.move(f'{percorso_file_excel}.bak', "../flussi_bak")
        # Spostare i file nella cartella flussi_bak
    file_stats_sql.close()


if __name__ == "__main__":
    trace_stats("avviato")
    main()
    trace_stats("eseguito")
