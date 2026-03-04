# prova esperienza 2: controllo altezza; Scarpa Federico; 13/10/2022

è_testo = 1  # 1 vuol dire vero e 0 falso
while è_testo == 1:
    try:
        misura = int(input("Quanto sei alt@ (cm)? "))
        while misura < 30 or misura > 250:
        	misura = int(input("Impossibile, ridimmi, quanto sei alt@? "))
        print("Sei un umano normale :)")
        è_testo = 0
    except:
        print("Dammi un valore numerico")
