"""
Nome programma: decript.py
Autore: Scarpa Federico
Descrizione: Decifratura secondo il cifrario di Cesare di una stringa
"""

if __name__ == "__main__":
    print("Decifratura di una stringa inserita secondo il cifrario di Cesare")
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
        if car == 'd':
            strfinale += 'a'
        elif car == 'e':
            strfinale += 'b'
        elif car == 'f':
            strfinale += 'c'
        elif car == 'g':
            strfinale += 'd'
        elif car == 'h':
            strfinale += 'e'
        elif car == 'i':
            strfinale += 'f'
        elif car == 'j':
            strfinale += 'g'
        elif car == 'k':
            strfinale += 'h'
        elif car == 'l':
            strfinale += 'i'
        elif car == 'm':
            strfinale += 'j'
        elif car == 'n':
            strfinale += 'k'
        elif car == 'o':
            strfinale += 'l'
        elif car == 'p':
            strfinale += 'm'
        elif car == 'q':
            strfinale += 'n'
        elif car == 'r':
            strfinale += 'o'
        elif car == 's':
            strfinale += 'p'
        elif car == 't':
            strfinale += 'q'
        elif car == 'u':
            strfinale += 'r'
        elif car == 'v':
            strfinale += 's'
        elif car == 'w':
            strfinale += 't'
        elif car == 'x':
            strfinale += 'u'
        elif car == 'y':
            strfinale += 'v'
        elif car == 'z':
            strfinale += 'w'
        elif car == 'a':
            strfinale += 'x'
        elif car == 'b':
            strfinale += 'y'
        elif car == 'c':
            strfinale += 'z'
    # cifratura

    print("Il messaggio originale è:", strfinale)
    # print messaggio finale
