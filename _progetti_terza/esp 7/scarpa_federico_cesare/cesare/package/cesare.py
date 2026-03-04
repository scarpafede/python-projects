"""
Nome programma: cesare.py
Autore: Scarpa Federico
Descrizione: Cifratura secondo il cifrario di Cesare di una stringa
"""

if __name__ == "__main__":
    print("Cifratura di una stringa inserita secondo il cifrario di Cesare")
    controllo = 0
    checklen = 1
    strfinale = ''
    # dichiarazione variabili

    while controllo != checklen:
        controllo = 0
        checklen = 1
        stringa = input("Inserire una stringa di solo caratteri minuscoli: ")
        checklen = len(stringa)
        for i in stringa:
            if 'a' <= i <= 'z':
                controllo += 1
    # controllo validita' input

    for car in stringa:
        if car == 'a':
            strfinale += 'd'
        elif car == 'b':
            strfinale += 'e'
        elif car == 'c':
            strfinale += 'f'
        elif car == 'd':
            strfinale += 'g'
        elif car == 'e':
            strfinale += 'h'
        elif car == 'f':
            strfinale += 'i'
        elif car == 'g':
            strfinale += 'j'
        elif car == 'h':
            strfinale += 'k'
        elif car == 'i':
            strfinale += 'l'
        elif car == 'j':
            strfinale += 'm'
        elif car == 'k':
            strfinale += 'n'
        elif car == 'l':
            strfinale += 'o'
        elif car == 'm':
            strfinale += 'p'
        elif car == 'n':
            strfinale += 'q'
        elif car == 'o':
            strfinale += 'r'
        elif car == 'p':
            strfinale += 's'
        elif car == 'q':
            strfinale += 't'
        elif car == 'r':
            strfinale += 'u'
        elif car == 's':
            strfinale += 'v'
        elif car == 't':
            strfinale += 'w'
        elif car == 'u':
            strfinale += 'x'
        elif car == 'v':
            strfinale += 'y'
        elif car == 'w':
            strfinale += 'z'
        elif car == 'x':
            strfinale += 'a'
        elif car == 'y':
            strfinale += 'b'
        elif car == 'z':
            strfinale += 'c'
    # cifratura

    print("Il messaggio cifrato è:", strfinale)
    # print messaggio cifrato finale
