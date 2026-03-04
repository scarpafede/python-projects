if [ $# -ne 2 ]; then
  echo "Errore; i parametri richiesti sono: la data in cui eseguire il calcolo e i giorni successivi da aggiungere!"
  exit 1
fi
cd ..
cd bin
python3 bioritmi.py $1 $2
cd ..
cd html
open -a Safari bioritmi_classe.html
