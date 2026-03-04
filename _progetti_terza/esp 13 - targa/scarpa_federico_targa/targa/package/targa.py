"""
Nome programma: targa.py
Autore: Scarpa Federico
Descrizione: data una stringa, il programma controlla se e' una targa automobilistica italiana.
"""


def main():
    """
    Programma principale
    """
    check = 0
    lunghezza = 0
    
    while check != 9:
        check = 0
        stringa = input("Inserisci la targa italiana: ")
        if stringa == "":
            check = 0
        stringa = stringa.upper()
        
        if len(stringa) != 7:
            print("La targa non contiene 7 caratteri")
            check = 0
        else:
            check += 1
            lunghezza = 1

        if lunghezza == 1:
            if "A" <= stringa[0] <= "Z" and "A" <= stringa[1] <= "Z":
                check += 1
            else:
                check = 0

            if "A" <= stringa[5] <= "Z" and "A" <= stringa[6] <= "Z":
                check += 1
            else:
                check = 0

            if "0" <= stringa[2] <= "9" and "0" <= stringa[3] <= "9" and "0" <= stringa[4] <= "9":
                check += 1
            else:
                check = 0

            if stringa[0] == "I" or stringa[0] == "O" or stringa[0] == "Q":
                check = 0
            else:
                check += 1

            if stringa[1] == "I" or stringa[1] == "O" or stringa[1] == "Q":
                check = 0
            else:
                check += 1

            if stringa[5] == "I" or stringa[5] == "O" or stringa[5] == "Q":
                check = 0
            else:
                check += 1

            if stringa[6] == "I" or stringa[6] == "O" or stringa[6] == "Q":
                check = 0
            else:
                check += 1

            if stringa[0] == "E" and stringa[1] == "E":
                check = 0
            else:
                check += 1

            if check != 9:
                print("La targa inserita","->", stringa,"<-", "non rispetta i requisiti")
    print("La targa inserita risulta corretta:", stringa)

if __name__ == "__main__":
    main()
