'''
Nome programma: numeri.py
Autore: Scarpa Federico
Descrizione: -recupero- calcolo del M.C.D. di due numeri interi,
                        calcolo del valore di Pi greco come somma di n termini di una serie.
'''

if __name__ == "__main__":
    print("Il primo programma calcolerà l'M.C.D tra due numeri interi inseriti e il secondo il valore di Pi greco come somma di n termini (n chiesto all'utente).")
    # print iniziale

    check_esercizio = 0
    check_numeri = 0
    check_input = 0
    # dichiarazione - inizializzazione variabili

    while check_esercizio == 0:
            try:
                esercizio = int(input("Quale esercizio vuole eseguire? 1 o 2? "))
                while esercizio != 1 and esercizio != 2:
                    print("Riprova")
                    esercizio = int(input("Vuoi eseguire il numero 1 o il 2? "))
                check_esercizio = 1
            except:
                print("Riprovare. Si prega di inserire numeri o qualcosa")
    # validazione e input del numero dell'esercizio da eseguire

    if esercizio == 1:
        print("Esecuzione esercizio 1...")
        while check_numeri == 0:
            try:
                primo_numero = int(input("Inserire il primo numero: "))
                secondo_numero = int(input("Inserire il secondo numero: "))
                check_numeri = 1
            except:
                print("Riprovare. Si prega di inserire numeri o qualcosa")
        while primo_numero != secondo_numero:
            if primo_numero > secondo_numero:
                primo_numero -= secondo_numero
            else:
                secondo_numero -= primo_numero
        print(primo_numero)
    # primo esercizio

    elif esercizio == 2:
        while check_input == 0:
            try:
                n = int(input("Inserisci il numero di volte che si andrà a sommare la serie: "))
                check_input = 1
            except:
                print("Riprovare. Si prega di inserire numeri o qualcosa")
        if n == 6:
            pigreco = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11
        elif n == 8:
            pigreco = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - 4/15
        if n == 6 or n == 8:
            print(pigreco)
    # esercizio 2 (non so come farlo)
