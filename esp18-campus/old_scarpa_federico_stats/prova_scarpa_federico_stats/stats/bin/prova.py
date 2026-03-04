import sys
import os

if len(sys.argv) == 2:
    percorso_file_excel = sys.argv[1]
    print(percorso_file_excel)
else:
    file_trovati = []
    for file in os.listdir('../flussi/'): # Scandisce tutti i file nella cartella flussi
        if file.endswith('.xlsx'): # Controlla se il file ha l'estensione .xlsx
            file_trovati.append(file) # Se sì, aggiungilo alla lista dei file trovati
    if len(file_trovati) == 0:
        print("Nessun file trovato con l'estensione .xlsx")
        sys.exit()

"""
for percorso_file_excel in file_trovati:
    print("exec")
"""