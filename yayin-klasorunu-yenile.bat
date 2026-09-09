@echo off
REM ============================================================
REM  Gelegen Hukuk - Yayin klasorunu yenile
REM  Sitede degisiklik yaptiktan sonra bu dosyaya cift tikla.
REM  "yayin" klasoru guncellenir; sonra Netlify'a surukle-birak.
REM  NOT: Sifre iceren dosyalar bilerek KOPYALANMAZ.
REM ============================================================
cd /d "%~dp0"
echo Yayin klasoru yenileniyor...

if exist "yayin" rmdir /s /q "yayin"
mkdir "yayin"

xcopy "css"    "yayin\css\"    /E /I /Q /Y >nul
xcopy "js"     "yayin\js\"     /E /I /Q /Y >nul
xcopy "assets" "yayin\assets\" /E /I /Q /Y >nul

copy "index.html"          "yayin\" >nul
copy "avukatlarimiz.html"  "yayin\" >nul
copy "hakkimizda.html"     "yayin\" >nul
copy "iletisim.html"       "yayin\" >nul
copy "kvkk.html"           "yayin\" >nul
copy "404.html"            "yayin\" >nul
copy "robots.txt"          "yayin\" >nul
copy "sitemap.xml"         "yayin\" >nul
copy "site.webmanifest"    "yayin\" >nul
copy "_headers"            "yayin\" >nul

echo.
echo TAMAM - "yayin" klasoru guncellendi.
echo Simdi bu klasoru Netlify'a surukle-birak yapabilirsin.
echo.
pause
