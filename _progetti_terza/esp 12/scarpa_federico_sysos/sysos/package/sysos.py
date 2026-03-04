import time
import sys

"""
Nome programma: prova.py
Autore: Scarpa Federico
Descrizione: 1. data una stringa, il programma restituisce la prima posizione che compare un carattere dato in essa,
            2. date due stringhe, le confronta e restituisce la prima volta che compare un carattere in comune tra di esse.
"""


def posizione(stringa, carattere):
    """
    restituisce la prima posizione di 'carattere' in 'stringa'
    """
    posiz_finale = 0
    cont = 0
    for i in stringa:
        posiz_finale += 1
        if i == carattere:
            cont = 1
            break
    if cont == 0:
        return -1
    else:
        return posiz_finale


def posizione_car_2_str(stringa1, stringa2):
    """
    restituisce la posizione del primo carattere in comune tra 'stringa1' e 'stringa2'
    """
    posiz_finale = 0
    cont = 0
    for car1 in stringa1:
        for car2 in stringa2:
            posiz_finale += 1
            if car1 == car2:
                cont = 1
                break
    if cont == 0:
        return -1
    else:
        if posiz_finale % 2 != 0:
            posiz_finale = posiz_finale // 2 -1
        else:
            posiz_finale = posiz_finale // 2 + 1
        return posiz_finale


def main():
    """
    Programma principale
    """
    inizio = time.monotonic()
    
    if sys.argv[1] == "1":
        string = input("Dunque, il programma restituisce la posizione di un carattere dato nella stringa inserita.\nInserisci una stringa: ")
        check = 1

        while check != 0:
            car = input("Inserisci il carattere: ")
            if car != '':
                check = 0
            else:
                print("Inserire qualcosa")

        pos = posizione(string,car)
        print("La prima volta che compare", "'" + car +"'", "in", "'" + string + "'", "e' nella", pos, "posizione")

    if sys.argv[1] == "2":
        str1 = input("Dunque, il programma compara due stringhe e restituisce la posizione nella quale un carattere di una e' presente nell'altra.\nInserisci la prima stringa: ")
        str2 = input("Inserisci la seconda stringa: ")
        posiz = posizione_car_2_str(str1,str2)
        int(posiz)
        carattere_str1 = str1 [posiz - 1]
        print("La prima posizione in cui la stringa 2 compare nella stringa 1 e':", "'" + str(posiz) + "'", "con il carattere", "'" + carattere_str1 + "'")
    fine = time.monotonic()
    print("Il programma ha messo", fine-inizio, "secondi per eseguirsi")
    print("Il programma è stato eseguito su", sys.platform)

if __name__ == "__main__":
    main()
