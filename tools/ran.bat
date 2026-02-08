@echo off
echo ===============================
echo  GENERADOR MASIVO DE QUIZZES
echo ===============================

cd /d %~dp0

python scripts\excel_to_json_all.py

echo.
echo ===============================
echo  PROCESO FINALIZADO
echo ===============================
pause
