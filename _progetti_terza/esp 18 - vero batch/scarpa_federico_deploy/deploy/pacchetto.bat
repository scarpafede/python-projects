@ECHO OFF

REM Scarpa Federico
REM 31/05/2023
REM pacchetto.bat

REM Per una corretta esecuzione, collocare nella cartella C:\Temp i file: deploy.py, CHANGELOG.txt, README.txt e execute.log .

MKDIR scarpa_federico_%1%

CD scarpa_federico_%1%
MKDIR %1%

CD %1%
MKDIR package

CD package
COPY C:\Temp\deploy.py  .

CD ..
MKDIR log

CD log
COPY C:\Temp\execute.log .

CD ..
COPY C:\Temp\CHANGELOG.txt .
COPY C:\Temp\README.txt .