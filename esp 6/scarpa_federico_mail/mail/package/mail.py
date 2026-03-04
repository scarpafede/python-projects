"""
nome programma: mail.py
autore: Scarpa Federico
descrizione: controllo caratteri @ e . in un indirizzo email
"""
if __name__ == "__main__":
    chiocciola = 0
    punto = 0
    while chiocciola != 1 or  punto < 1:
        indirizzo = input("Inserire l'indirizzo email: ")
        for car in indirizzo:
            if car == '@':
                chiocciola += 1
            elif car == '.':
                punto +=1
        if chiocciola > 1:
            print("Sono state inserite troppe chiocciole (@):" , chiocciola)
        if chiocciola < 1:
            print("Non sono state inserite chiocciole (@):" , chiocciola)
        if punto < 1:
            print("Non sono stati inseriti punti")
    print("Il tuo indirizzo di posta elettronica e':" , indirizzo)