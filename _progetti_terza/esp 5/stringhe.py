# stringhe.py: insieme di quattro esercizi assegnati per casa; Scarpa Federico; 9/11/2022
if __name__ == "__main__":
    è_testo = 1
    while è_testo == 1:
        try:
            print("Esercizio 1, mostrare a schermo il carattere primo, ultimo e di mezzo della frase inserita")
            print("Esercizio 2, mostrare a video la lunghezza della frase inserita e quante 'a' ci sono ")
            print("Esercizio 3, mostrare a schermo quante vocali ci sono nel testo inserito e la loro frequenza individualmente")
            print("Esercizio 4, mostrare a video solo i caratteri in posizione pari della frase inserita")
            esercizio = int(input("Quale esercizio vuole eseguire? 1, 2, 3 o 4? "))
            while esercizio != 1 and esercizio != 2 and esercizio != 3 and esercizio != 4:
                esercizio = int(input("Vuoi eseguire il numero 1, 2, 3 o 4? "))
            è_testo = 0
        except:
            print("Si prega di inserire numeri o qualcosa")

    if esercizio == 1:
        # esercizio 1: mostrare a schermo il carattere primo, ultimo e di mezzo della frase inserita; Scarpa Federico; 9/11/2022
        print("Esecuzione esercizio 1")
        s1 = input("Inserisci la frase: ")
        cont = 0
        for carattere in s1:
            cont += 1
        cont -= 1
        print("L'ultima lettera è:" , s1[len(s1) - 1 : len(s1)])
        print("La prima lettera è:" , s1[0])
        print("La lettera in mezzo è:" , s1[cont // 2 ])

    elif esercizio == 2:  
        # esercizio 2: mostrare a video la lunghezza della frase inserita e quante 'a' ci sono; Scarpa Federico; 9/11/2022
        print("Esecuzione esercizio 2")
        s2 = input("Inserisci la frase: ")
        conto = 0
        for carat in s2:
            if carat == 'a' or carat == 'A':
                conto += 1
        print("La frase è lunga" , len(s2) , "caratteri, inclusi gli spazi")
        print("Le lettere 'a' contenute nella frase sono" , conto)

    elif esercizio == 3:
        # esercizio 3: mostrare a video quante vocali ci sono nel testo inserito e la loro frequenza individualmente; Scarpa Federico; 9/11/2022
        print("Esecuzione esercizio 3")
        s3 = input("Inserisci la frase: ")
        a = e = i = o = u = 0
        for car in s3:
            if car == 'a' or car == 'A':
                a += 1
            if car == 'e' or car == 'E':
                e += 1
            if car == 'i' or car == 'I':
                i += 1
            if car == 'o' or car == 'O':
                o += 1
            if car == 'u' or car == 'U':
                u += 1
        tot_vocali = a + e + i + o + u
        print("Le vocali nel testo sono" , tot_vocali)
        print("La frequenza della lettera 'a' nel testo è di" , a / len(s3))
        print("La frequenza della lettera 'e' nel testo è di" , e / len(s3))
        print("La frequenza della lettera 'i' nel testo è di" , i / len(s3))
        print("La frequenza della lettera 'o' nel testo è di" , o / len(s3))
        print("La frequenza della lettera 'u' nel testo è di" , u / len(s3))

    elif esercizio == 4:
        # esercizio 4: mostrare a video solo i caratteri in posizione pari della frase inserita; Scarpa Federico; 9/11/2022
        print("Esecuzione esercizio 4")
        s4 = input("Inserisci la frase: ")
        var = len(s4)
        vari = len(s4) -1
        if len(s4) % 2 == 0:
            for cartr in s4:
                var += 1
                if var % 2 == 0:
                    print(cartr)
        else:
            print("Questa parte di codice non sono riuscito a farla") #<---
            print(s4[2])
            for cartr in s4:
                vari += 2
                if vari % 3 == 0:
                    print(cartr)




                
