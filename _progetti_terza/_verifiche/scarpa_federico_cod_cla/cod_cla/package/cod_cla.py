"""
nome programma: cod_cla.py
autore: Scarpa Federico
descrizione: controllo validita' classe del Marconi inserita da input
"""
if __name__ == "__main__":
    print("Controllo classe inserita: deve contenere 3 caratteri, un numero compreso tra 1 e 5, una lettera maiuscola e minuscola tra: a c e i l t")
    checkcar = 1
    checknum = 1
    checkmaiusc = 1
    checkminus = 1
    while checkcar != 0 or checknum != 0 or checkmaiusc != 0 or checkminus != 0:
        classe = input("Inserisci la classe: ")
        checkcar = 1
        checknum = 1
        checkmaiusc = 1
        checkminus = 1
        if len(classe) == 3:
            checkcar = 0
        if checkcar == 0:
            num = classe[0]
            if num >= '1' and num <= '5':
                checknum = 0
            carma = classe[1]
            if carma >= 'A' and carma <= 'Z':
                checkmaiusc = 0
            carmi = classe[2]
            if carmi == 'a' or carmi == 'c' or carmi == 'e' or carmi == 'i' or carmi == 'l' or carmi == 't':
                checkminus = 0
    if checkcar == 0 and checknum == 0 and checkmaiusc == 0 and checkminus == 0:
        print("La classe inserita è", classe)
