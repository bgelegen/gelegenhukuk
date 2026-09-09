@echo off
chcp 65001 >nul
title Gelegen Hukuk - Form Sunucusu

REM ==================================================================
REM  AYARLAR  --  Asagidaki 3 satiri KENDI bilgilerinizle doldurun.
REM ==================================================================

REM  1) Gonderen Gmail hesabi (ayni hesap hem gonderir hem alir olabilir):
set SMTP_KULLANICI=batuhangelegen44@gmail.com

REM  2) Gmail UYGULAMA SIFRESI (16 haneli - normal Gmail sifreniz DEGIL!):
REM     Nasil alinir: Google Hesabi > Guvenlik > 2 Adimli Dogrulama > Uygulama Sifreleri
set SMTP_SIFRE=BURAYA_16_HANELI_UYGULAMA_SIFRENIZI_YAZIN

REM  3) Taleplerin dusecegi adres:
set FORM_ALICI=batuhangelegen44@gmail.com

REM ==================================================================
REM  Asagisina DOKUNMANIZA GEREK YOK.
REM ==================================================================

set SMTP_HOST=smtp.gmail.com
set SMTP_PORT=587
set FORM_ORIGIN=*

cd /d "%~dp0"

echo.
echo  ============================================================
echo   GELEGEN HUKUK - Form E-posta Sunucusu
echo  ============================================================
echo   Adres     : http://localhost:5000
echo   Saglik    : http://localhost:5000/saglik
echo   Durdurmak : Bu pencerede Ctrl + C yapin ya da pencereyi kapatin.
echo  ============================================================
echo.

python gonder.py

echo.
echo  Sunucu durdu. Pencereyi kapatabilirsiniz.
pause
