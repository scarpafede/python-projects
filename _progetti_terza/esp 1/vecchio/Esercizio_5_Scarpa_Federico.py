# esercizio 5: controllo voto; Scarpa Federico; 29/9/2022
voto = int(input("Inserire il voto "))
if 1 <= voto <= 10:
 print("Il voto inserito" , "(" , voto , ")" , "è accettabile")
else:
 print("Il voto inserito" , "(" , voto , ")" , "non è accettabile")