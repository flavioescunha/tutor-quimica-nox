@echo off
echo Inicializando repositorio Git...
git init

echo.
echo Adicionando arquivos...
git add .

echo.
echo Criando commit...
git commit -m "Versao Final NOX"

echo.
echo Renomeando branch para main...
git branch -M main

echo.
echo Configurando repositorio remoto...
git remote add origin https://github.com/flavioescunha/tutor-quimica-nox.git

echo.
echo Enviando arquivos para o GitHub...
git push -u origin main

echo.
echo Concluido!
pause
