# esercizio 6: ordine crescente numeri interi; Scarpa Federico; 5/10/2022
primo = int(input("Inserire il primo numero "))
secondo = int(input("Inserire il secondo numero "))
terzo = int(input("Inserire il terzo numero "))
if primo == secondo or secondo == terzo or terzo == primo:
    print("Sono stati inseriti due o più numeri uguali, impossibile procedere")
else:
    if primo < secondo and terzo:
       nUno = primo
       if secondo < terzo:
           nDue = secondo
           nTre = terzo
       else:
           nDue = terzo
           nTre = secondo
    elif secondo < primo and terzo:
       nUno = secondo
       if primo < terzo:
           nDue = primo
           nTre = terzo
       else:
           nDue = terzo
           nTre = primo
    elif terzo < secondo and primo:
       nUno = terzo
       if secondo < primo:
           nDue = secondo
           nTre = primo
       else:
           nDue = primo
           nTre = secondo
    print(nUno , nDue , nTre)