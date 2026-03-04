# esercizio 7: controllo voto plus; Scarpa Federico; 5/10/2022
voto = int(input("Inserire il voto "))
if 4 <= voto <= 5:
    print("Il voto inserito" , "(" , voto , ")" , "è insufficente")
elif voto == 0:
    print("Il voto inserito" , "(" , voto , ")" , "è troppo basso")
elif voto == 6:
    print("Il voto inserito" , "(" , voto , ")" , "è sufficente")
elif 1 <= voto <= 3:
    print("Il voto inserito" , "(" , voto , ")" , "è basso")
elif 7 <= voto <= 8:
    print("Il voto inserito" , "(" , voto , ")" , "è buono")
elif 9 <= voto <= 10:
    print("Il voto inserito" , "(" , voto , ")" , "è alto")
elif voto < 1 or voto > 10:
    print("Il voto inserito" , "(" , voto , ")" , "è inaccettabile")