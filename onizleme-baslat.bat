@echo off
chcp 65001 >nul
title Gelegen Hukuk - Yerel Onizleme
cd /d "%~dp0"

echo.
echo  ============================================================
echo   GELEGEN HUKUK - YEREL ONIZLEME
echo  ============================================================
echo.
echo  Yayin klasoru tazeleniyor...

if exist "yayin" rmdir /s /q "yayin"
mkdir "yayin"
xcopy "css"    "yayin\css\"    /E /I /Q /Y >nul
xcopy "js"     "yayin\js\"     /E /I /Q /Y >nul
xcopy "assets" "yayin\assets\" /E /I /Q /Y >nul
for %%f in (index.html avukatlarimiz.html hakkimizda.html iletisim.html kvkk.html 404.html robots.txt sitemap.xml site.webmanifest _headers) do copy "%%f" "yayin\" >nul

echo  Tamam.
echo.

REM --- Bu bilgisayarin Wi-Fi adresini bul ---
set "IP="
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do (
  set "SATIR=%%a"
  call :TEMIZLE
)
goto :BASLAT

:TEMIZLE
set "SATIR=%SATIR: =%"
echo %SATIR% | findstr /b "192.168.1." >nul && set "IP=%SATIR%"
goto :eof

:BASLAT
echo  ------------------------------------------------------------
echo   BILGISAYARDAN     :  http://localhost:8000
if defined IP (
echo   TELEFONDAN        :  http://%IP%:8000
) else (
echo   TELEFONDAN        :  http://192.168.1.141:8000
)
echo  ------------------------------------------------------------
echo.
echo   * Telefonun ayni Wi-Fi agina bagli olmali.
echo   * Windows guvenlik duvari sorarsa "Erisime izin ver" de.
echo   * Durdurmak icin: bu pencerede Ctrl+C ya da pencereyi kapat.
echo.

cd yayin
python -m http.server 8000 --bind 0.0.0.0

echo.
echo  Sunucu durdu.
pause
