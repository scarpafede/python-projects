'''
Nome programma: numeri.py
Autore: Scarpa Federico
Descrizione: -recupero- calcolo del M.C.D. di due numeri interi,
                        calcolo del valore di Pi greco come somma di n termini di una serie.
                        AGGIUNTA: esercizio eseguito con funzione def
'''
def main():
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
        MCD = mcd(primo_numero, secondo_numero)
        print(MCD)
    # primo esercizio

    elif esercizio == 2:
        print("Esecuzione esercizio 2...")
        while check_input == 0:
            try:
                volte = int(input("Inserisci il numero (intero) di volte che si andrà a sommare la serie: "))
                while volte < 0:
                    volte = int(input("Riprova. Inserisci un numero positivo o uguale a 0: "))
                cont_volte = volte - 1
                check_input = 1
            except:
                print("Riprovare. Si prega di inserire numeri o qualcosa")
        
        pigreco(cont_volte)
    # secondo esercizio

def mcd(primoN, secondoN):
    while primoN != secondoN:
        if primoN > secondoN:
            primoN -= secondoN
        else:
            secondoN -= primoN
    return primoN

def pigreco(cont_volte):
    divisore = 1
    risultato =  0
    cont = 1
    cont_volte -= 1
    volte = cont_volte + 1
    while cont_volte != 0:
        divisore += 2
        cont += 1
        if cont % 2 == 0:
            risultato -= 4 / divisore
        else:
            risultato += 4 / divisore
        cont_volte -= 1
    if volte != 0:
        risultato += 4
        print(risultato)


if __name__ == "__main__":
    main()