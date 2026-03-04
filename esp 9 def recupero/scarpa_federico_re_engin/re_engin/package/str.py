'''
Nome programma: str.py
Autore: Scarpa Federico
Descrizione: -recupero- contare le occorrenze di un carattere,
                        stampare una stringa alla rovescia,
                        verificare se la stringa inserita e' palindroma.
                        AGGIUNTA: esercizio eseguito con funzione def
'''
# definizione funzione stringa alla rovescia
def strRovescia(stringa):
    rovescia = ''
    for car in stringa:
        rovescia = car + rovescia
    return rovescia

# definizione funzione controllo stringa palindroma
def sePalindroma(stringa, str_rovescia):
    if stringa == str_rovescia:
        print("La stringa inserita è palindroma")

# definizione funzione conta carattere in stringa inserita
def contaCarattere(stringa, carattere_inserito):
    conta_parziale = 0
    for car in stringa:
        if car == carattere_inserito:
            conta_parziale += 1
    return conta_parziale

# definizione programma principale
def main():
    print("Inserita una stringa e una lettera, il programma contera' le occorrenze della lettera, stampera' la stringa alla rovescia e verifichera' se e' palindroma.")
    # print iniziale

    check = 0
    while check == 0:
        stringa = input("Inserire la stringa: ")
        carattere_inserito = input("Inserire il carattere: ")
        prova = contaCarattere(stringa, carattere_inserito)
        if prova != 0:
            check = 1
    
    conto = contaCarattere(stringa, carattere_inserito)
    rovescia = strRovescia(stringa)
    sePalindroma(stringa, rovescia)

    print("Il numero di", carattere_inserito, "dentro la stringa e':", conto)
    print("La stringa alla rovescia e':", rovescia)
    # print finali

# istruzione di avvio del programma #
if __name__ == "__main__":
    main()
