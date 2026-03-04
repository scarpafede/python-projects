'''
Nome programma: str.py
Autore: Scarpa Federico
Descrizione: -recupero- contare le occorrenze di un carattere,
                        stampare una stringa alla rovescia,
                        verificare se la stringa inserita e' palindroma.
'''

if __name__ == "__main__":
    print("Inserita una stringa e una lettera, il programma contera' le occorrenze della lettera, stampera' la stringa alla rovescia e verifichera' se e' palindroma.")
    # print iniziale
    
    conta_carattere = 0
    str_rovescia = ''
    check = 0
    # dichiarazione - inizializzazione variabili

    while check == 0:
        stringa = input("Inserire la stringa: ")
        carattere_inserito = input("Inserire la lettera: ")
    
        for car in stringa:
            if car == carattere_inserito:
                conta_carattere += 1
                check += 1

        if check == 0:
            print("Riprova")
        # prima parte esercizio

    for car in stringa:
        str_rovescia = car + str_rovescia
    # seconda parte esercizio

    if stringa == str_rovescia:
        print("La stringa inserita è palindroma")
    # terza parte esercizio

    print("Il numero di", carattere_inserito, "dentro la stringa e':", conta_carattere)
    print("La stringa alla rovescia e':", str_rovescia)
    # print finali
