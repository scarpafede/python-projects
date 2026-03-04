@ECHO ON

REM Scarpa Federico
REM 1/06/2023
REM scarpa_federico_deploy.bat

REM Per una corretta esecuzione, collocare nella cartella C:\Work i file: template.py, CHANGELOG.txt, README.md e execute.log .

IF "%1" == "" GOTO ERRORE

MKDIR scarpa_federico_%1

CD scarpa_federico_%1
MKDIR %1

CD %1
MKDIR package

CD package
COPY C:\Work\template.py %1.py

CD ..
MKDIR log
MKDIR flussi

CD log
COPY C:\Work\execute.log .

CD ..
COPY C:\Work\CHANGELOG.txt .
COPY C:\Work\README.md .

CD package
C:\Python310\python.exe %1.py

GOTO FINE

:ERRORE
ECHO Il programma deve essere eseguito con un argomento (nome deploy).

:FINE