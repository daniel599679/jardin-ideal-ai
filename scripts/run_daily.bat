@echo off
:: Motor de Reportes — Jardín Ideal
:: Doble clic para generar el reporte diario
:: Requiere Python 3.8+ instalado

cd /d "%~dp0\.."
echo.
echo ============================================
echo   JARDÍN IDEAL — Generando reporte diario
echo ============================================
python -X utf8 scripts\generar_reporte.py diario
echo.
pause
