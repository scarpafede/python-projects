@ECHO OFF

CD ..\bin
C:\Python310\python.exe calcola_bioritmi.py %1 %2
CD ..\html
COPY bioritmi_classe.html C:\Work
CD C:\Work
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" C:\Work\bioritmi_classe.html