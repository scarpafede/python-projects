"""
Nome programma: filter.py
Autore: Scarpa Federico
Descrizione: il programma filtra il contenuto del file di log e lo scrive nel filter.txt
"""


def filter():
    """
    Apre il file execute.log e lo filtra, scrivendo su filter.txt gli argomenti del filtro
    """
    
    f1 = open("../log/execute.log", 'r')
    f2 = open("../flussi/filter.txt", 'w')
    
    lines = f1.readlines()
    for line in lines:
        if "Inizio" in line:
            f2.write(line)

    f1.close()
    f2.close()


def main():
    filter()


if __name__ == "__main__":
    main()
