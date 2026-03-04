#!/bin/sh
echo "creazione del deploy"

# Controlla se e' stato fornito un parametro
if [ $# -eq 0 ]; then
  echo "Errore: manca il parametro!"
  echo lo shell non si è eseguito: manca il parametro > trace.txt
  exit 1
fi

echo $1
percorso="$PWD"
trace="$percorso/trace.txt"

# Creazione della struttura del deploy

mkdir tosi_giacomo_$1
echo creo la cartella tosi_giacomo_$1 >> $trace

cd tosi_giacomo_$1
echo entro nella cartella tosi_giacomo_$1 >> $trace

mkdir $1
echo creo la cartella $1 >> $trace

cd $1
echo entro nella cartella $1 >> $trace

mkdir flussi
echo creo la cartella flussi >> $trace

mkdir log
echo creo la cartella log >> $trace

mkdir bin
echo creo la cartella bin >> $trace

cp "../../template/CHANGELOG.txt"  "."
echo copio il template CHANGELOG.txt dal percorso template/CHANGELOG.txt >> $trace

cp "../../template/README.md"  "."
echo copio il template README.txt dal percorso template/README.md >> $trace

cd bin
echo entro nella cartella bin >> $trace

cp "../../../template/python_template.py"  "$1.py"
echo copio il template python_template.py dal percorso template/python_template.py >> $trace e lo rinomino $1

python3 $1.py
echo eseguo il programma $1.py

echo fine del processo >> $trace


