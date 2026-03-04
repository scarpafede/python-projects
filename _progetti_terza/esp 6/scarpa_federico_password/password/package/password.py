"""
nome programma: password.py
autore: Scarpa Federico
descrizione: controllo validita' password secondo dei requisiti
"""
if __name__ == "__main__":
    print("Reqisiti minimi per creare una password efficace:")
    print("1. avere una lunghezza minima di almeno 8 caratteri e massima di 20")
    print("2. contenere almeno un carattere maiuscolo e uno minuscolo")
    print("3. contenere almeno un numero")
    print("4. contenere almeno un carattere speciale tra i seguenti: ! ? $ % ( ) : ; @ .")
    checklen = 1
    maiusc = 1
    minusc = 1
    num = 1
    carspec = 1
    while checklen != 0 or maiusc != 0 or minusc != 0 or num != 0 or carspec != 0:
        password = input("Inserisci una password: ")
        checklen = 1
        maiusc = 1
        minusc = 1
        num = 1
        carspec = 1
        if len(password) >= 8 and len(password) <= 20:
            checklen = 0
        for car in password:
            if car >= 'A' and car <= 'Z':
                maiusc = 0
            if car >= 'a' and car <= 'z':
                minusc = 0
            if car >= '0' and car <= '9':
                num = 0
            if car == '!' or car == '?' or car == '$' or car == '%' or car == '(' or car == ')' or car == ':' or car == ';' or car == '@' or car == '.':
                carspec = 0
        if checklen != 0:
            print("La password inserita non rispetta il primo requisito")
        if maiusc != 0 or minusc != 0:
            print("La password inserita non rispetta il secondo requisito")
        if num != 0:
            print("La password inserita non rispetta il terzo requisito")
        if carspec != 0:
            print("La password inserita non rispetta il quarto requisito")
    print("La password inserita e corretta è:", password)