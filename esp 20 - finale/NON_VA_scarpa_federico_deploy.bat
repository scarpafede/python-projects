@ECHO ON

REM Scarpa Federico
REM 1/06/2023
REM scarpa_federico_deploy.bat

REM EPOCH TIME
setlocal
for /f "tokens=2,3,4 delims=/ " %%f in ('date /t') do set d=%%h%%g%%f
for /f "tokens=1,2 delims=: " %%f in ('time /t') do set t=%%f%%g
SET DT=%d%%t: =0%

REM Per una corretta esecuzione, collocare nella cartella C:\Work i file: template.py, CHANGELOG.txt, README.md e execute.log .

IF "%1" == "" GOTO ERRORE

MKDIR scarpa_federico_%1 > trace_%1_%DT%.log

CD scarpa_federico_%1
MKDIR %1 >> ../trace_%1_%DT%.log

CD %1
MKDIR package >> ../../trace_%1_%DT%.log

CD package
COPY C:\Work\template.py %1.py >> ../../../trace_%1_%DT%.log

CD ..
MKDIR log >> ../../trace_%1_%DT%.log
MKDIR flussi >> ../../trace_%1_%DT%.log

CD log
COPY C:\Work\execute.log . >> ../../../trace_%1_%DT%.log

CD ..
COPY C:\Work\CHANGELOG.txt . >> ../../trace_%1_%DT%.log
COPY C:\Work\README.md . >> ../../trace_%1_%DT%.log

CD package
C:\Python310\python.exe %1.py

GOTO FINE

:ERRORE
ECHO Il programma deve essere eseguito con un argomento (nome deploy).

:FINE