@echo off
:: Motor de Reportes — Jardín Ideal
:: Doble clic para generar el reporte mensual (primer día del mes)
:: Requiere Python 3.8+ instalado

cd /d "%~dp0\.."
echo.
echo ============================================
echo   JARDÍN IDEAL — Generando reporte mensual
echo ============================================
python -X utf8 scripts\generar_reporte.py mensual
echo.
pause
