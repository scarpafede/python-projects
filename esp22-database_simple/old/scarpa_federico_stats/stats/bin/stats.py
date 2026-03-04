"""
Nome programma: stats.py
Autore: Scarpa Federico
Descrizione: il programma inserisce in un db dati di file excel;
                successivamente esegue una select.
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
from sqlalchemy import create_engine


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


def sheet1(df):
    """
    Restituisce una lista di elementi e una condizione
    a partire da un DataFrame.
    """
    l = []
    l.append(df['Nome quiz'].iloc[0])
    l.append(df['Nome corso'].iloc[0])
    l.append(df['Apertura'].iloc[0])
    l.append(df['Chiusura'].iloc[0])
    l.append(df['Aperto per'].iloc[0])
    l.append(int(df['Numero di primi tentativi completati e valutati'].iloc[0]))
    l.append(int(df['Numero totale dei tentativi completi valutati'].iloc[0]))
    l.append(df['Voto medio dei primi tentativi'].iloc[0])
    l.append(df['Voto medio di tutti i tentativi'].iloc[0])
    l.append(df['Media delle valutazioni degli ultimi tentativi'].iloc[0])
    l.append(df['Media delle valutazioni dei tentativi migliori'].iloc[0])
    try:
        l.append(df['Mediana dei voti (per tentativo migliore)'].iloc[0])
        l.append(df['Deviazione standard (per tentativo migliore)'].iloc[0])
        condiz = "q1"
    except:
        pass
    try:
        l.append(df['Mediana dei voti (per ultimi tentativi)'].iloc[0])
        l.append(df['Deviazione standard (per ultimi tentativi)'].iloc[0])
        l.append(df['Asimmetria della distribuzione dei voti (per ultimi tentativi)'].iloc[0])
        l.append(df['Curtosi della distribuzione dei voti (per ultimi tentativi)'].iloc[0])
        l.append(df['Coefficiente di consistenza interna (per ultimi tentativi)'].iloc[0])
        l.append(df["Quoziente d'errore (per ultimi tentativi)"].iloc[0])
        l.append(df['Errore standard (per ultimi tentativi)'].iloc[0])
        condiz = "q3"
    except:
        pass
    return l,condiz


def sheet2(dat_risp_qz, indice):
    """
    Restituisce una lista di elementi a partire da un DataFrame
    e un indice.
    """
    l = []
    l.append(int(dat_risp_qz['Q#'].iloc[indice]))
    l.append(dat_risp_qz['Tipo di domanda'].iloc[indice])
    l.append(dat_risp_qz['Nome della domanda'].iloc[indice])
    l.append(int(dat_risp_qz['Tentativi'].iloc[indice]))
    l.append(dat_risp_qz['Indice di abilità'].iloc[indice])
    l.append(dat_risp_qz['Deviazione standard'].iloc[indice])
    l.append(dat_risp_qz['Indice delle risposte date a caso'].iloc[indice])
    l.append(dat_risp_qz['Peso previsto'].iloc[indice])
    l.append(dat_risp_qz['Peso effettivo'].iloc[indice])
    l.append(dat_risp_qz['Indice di discriminazione'].iloc[indice])
    l.append(dat_risp_qz['Efficienza discriminante'].iloc[indice])
    return l


def get_path_excel(lista_argv):
    """
    Restituisce i percorsi (relativi al programma)
    dei file excel presenti in flussi
    a partire da una lista di argomenti;
    termina il programma se non ci sono.
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


def conn_alch():
    """
    Viene creato il motore SQLAlchemy per connettersi al database.
    """
    conn_string = "sqlite:///../db/stats.db"
    engine = create_engine(conn_string)
    return engine


def database_item_tentativi(engine):
    """
    :return: dataset Database
    """
    sql_query = """
        SELECT *
        FROM stats
        WHERE Tentativi < 10
        ORDER BY Tentativi ASC
    """
    # Esegue la query utilizzando il motore e restituisce un DataFrame pandas che contiene i risultati della query
    df = pd.read_sql_query(sql_query, engine)
    return df


def database_item_vf(engine):
    """
    :return: dataset Database
    """
    sql_query = """
        SELECT *
        FROM stats
        WHERE "Tipo di domanda" = "Vero/Falso"
        ORDER BY Q ASC
    """
    # Esegue la query utilizzando il motore e restituisce un DataFrame pandas che contiene i risultati della query
    df = pd.read_sql_query(sql_query, engine)
    return df


def select(mod, engine):
    stringa_finale = ''
    if mod == "tentativi":
        df_database = database_item_tentativi(engine)
        for row_index, row in df_database.iterrows():
            for numero_colonna in range(len(row)):
                stringa_finale += f'"{row.iloc[numero_colonna]}",'
            stringa_finale += '\n'
    elif mod == "vf":
        df_database = database_item_vf(engine)
        for row_index, row in df_database.iterrows():
            for numero_colonna in range(len(row)):
                stringa_finale += f'"{row.iloc[numero_colonna]}",'
            stringa_finale += '\n'
    return stringa_finale


def main():
    lista_arg_cli= sys.argv[1:]

    if "verbose_true" in lista_arg_cli:
        ic.enable()
    elif "verbose_false" in lista_arg_cli:
        ic.disable()
    else:
        print("Parametro verbose non trovato: programma terminato")
        sys.exit()
    
    percorsi_file_excel = get_path_excel(lista_arg_cli)

    file_stats_sql = open("../db/stats.sql", "w")
    percorso_db = "../db/stats.db"

    conn = sqlite3.connect(percorso_db)
    cur = conn.cursor()

    # Insert della prima tabella (quiz)
    for percorso_file_excel in percorsi_file_excel:
        # Crea il dataset con il contenuto del primo foglio del file excel
        dati_quiz = pd.read_excel(percorso_file_excel, sheet_name=0)
        l1,condizione = sheet1(dati_quiz)
        ins_sh1 = 'INSERT INTO quiz VALUES ('
        ins_sh1 += f'"{l1[0]}","{l1[1]}","{l1[2]}",'
        ins_sh1 += f'"{l1[3]}","{l1[4]}",{l1[5]},'
        ins_sh1 += f'{l1[6]},"{l1[7]}","{l1[8]}",'
        ins_sh1 += f'"{l1[9]}","{l1[10]}"'
        print(condizione)
        if condizione == "q1":
            ins_sh1 += f',"{l1[11]}","{l1[12]}"'
            ins_sh1 += ',"nan","nan","nan","nan","nan","nan","nan"'
        elif condizione == "q3":
            ins_sh1 += ',"nan","nan"'
            ins_sh1 += f',"{l1[11]}","{l1[12]}","{l1[13]}"'
            ins_sh1 += f',"{l1[14]}","{l1[15]}","{l1[16]}","{l1[17]}"'
        ins_sh1 += ')'
        file_stats_sql.write(ins_sh1 + '\n')
        cur.execute(ins_sh1)
        conn.commit()

        # Crea il dataset con il contenuto del secondo foglio del file excel
        dati_risposte_quiz = pd.read_excel(percorso_file_excel, sheet_name=1)

        # Insert della seconda tabella (stats)
        for indice, riga in dati_risposte_quiz.iterrows():
            ic(riga)
            l2 = sheet2(dati_risposte_quiz, indice)
            ins_sh2 = 'INSERT INTO stats VALUES ('
            ins_sh2 += f'"{l1[0]}","{l1[1]}","{l1[2]}",'
            ins_sh2 += f'{l2[0]},"{l2[1]}",'
            ins_sh2 += f'"{l2[2]}",{l2[3]},"{l2[4]}","{l2[5]}",'
            ins_sh2 += f'"{l2[6]}","{l2[7]}","{l2[8]}","{l2[9]}","{l2[10]}")'
            file_stats_sql.write(ins_sh2 + '\n')
            cur.execute(ins_sh2)
            conn.commit()

        os.rename(percorso_file_excel, f'{percorso_file_excel}.bak')
        sh.move(f'{percorso_file_excel}.bak', "../flussi_bak")
        # Spostare i file nella cartella flussi_bak
    file_stats_sql.close()

    engine = conn_alch()
    var = ''
    if "select_tentativi" in lista_arg_cli:
        var = select("tentativi",engine)
    elif "select_vf" in lista_arg_cli:
        var = select("vf",engine)
    else:
        var = "Parametro select non trovato: select non effettuata."
    with open("../log/select_output.txt", "w") as file_select_output:
        file_select_output.write(var)


if __name__ == "__main__":
    trace_stats("avviato")
    main()
    trace_stats("eseguito")
