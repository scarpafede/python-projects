"""
Nome programma: my_log_read.py
Autore: Scarpa Federico
Descrizione: il programma legge il contenuto del file di log (execute.log) e lo mostra in output sul terminale
"""


def readlog():
    """
    Apre e mostra sul terminale il contenuto del file execute.log
    """
    f1 = open("../log/execute.log", "r")
    
    lines = f1.readlines()
    for line in lines:
        print(line)

    f1.close()


def main():
    readlog()


if __name__ == "__main__":
    main()
