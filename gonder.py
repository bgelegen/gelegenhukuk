#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==========================================================================
gonder.py — İletişim/Randevu formu e-posta gönderici (Gelegen Hukuk Bürosu)
--------------------------------------------------------------------------
NE YAPAR?
İletişim formundan gelen JSON veriyi doğrular, güvenlik kontrollerinden
geçirir ve TASARLANMIŞ (lacivert/altın temalı) bir HTML e-posta olarak
SMTP üzerinden büronun e-posta kutusuna gönderir.

NEDEN SMTP?
Python'da PHP'nin mail() fonksiyonunun karşılığı yoktur; e-posta göndermek
için bir SMTP sunucusu gerekir. Bu aslında daha SAĞLIKLI teslimat sağlar
(spam'e düşme ihtimali düşük).

KURULUM (docs/FORM-KURULUM.md):
  1. Gereksinim:  pip install flask
  2. Aşağıdaki AYARLAR bölümünü doldurun (SMTP + ALICI).
  3. Çalıştırın:  python gonder.py     (varsayılan: http://0.0.0.0:5000)
     Üretimde:    gunicorn gonder:app  (önerilir)
  4. js/data.js içinde:
        web3formsKey: ""
        formEndpoint: "http://SUNUCU-ADRESINIZ:5000/gonder"
     (veya reverse-proxy ile aynı alan adı altında "/gonder")

GÜVENLİK: honeypot, hız sınırı, sunucu tarafı doğrulama, HTML kaçışı dahildir.
==========================================================================
"""

import os
import re
import ssl
import time
import html
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from datetime import datetime

from flask import Flask, request, jsonify, make_response

# ============================== AYARLAR ==================================
# Taleplerin düşeceği adres
ALICI = os.environ.get("FORM_ALICI", "batuhangelegen44@gmail.com")

# SMTP sunucu bilgileri (e-posta bu hesaptan gönderilir).
# Gmail için: SMTP_HOST=smtp.gmail.com, SMTP_PORT=587 ve
#   SMTP_KULLANICI=hesabiniz@gmail.com
#   SMTP_SIFRE=uygulama-sifresi  (2 adımlı doğrulama açıkken üretilir)
# ÖNEMLİ: Şifreyi koda yazmayın; ortam değişkeni (environment variable) kullanın.
SMTP_HOST      = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT      = int(os.environ.get("SMTP_PORT", "587"))
SMTP_KULLANICI = os.environ.get("SMTP_KULLANICI", "")   # örn. gonderen@gmail.com
SMTP_SIFRE     = os.environ.get("SMTP_SIFRE", "")       # uygulama şifresi
GONDEREN_AD    = os.environ.get("FORM_GONDEREN_AD", "Gelegen Hukuk Web Sitesi")

BURO_ADI     = "Gelegen Hukuk Bürosu"
BEKLE_SANIYE = 30      # aynı IP için art arda gönderim aralığı
MAX_MESAJ    = 2000

# Formun barındırıldığı site adresi (CORS izni için). Aynı alan adı altında
# reverse-proxy kullanıyorsanız burayı sitenizin adresi yapın; "*" da olur
# ama belirli origin daha güvenlidir.
IZINLI_ORIGIN = os.environ.get("FORM_ORIGIN", "*")
# ========================================================================

app = Flask(__name__)

# Basit, bellek-içi hız sınırı: {ip: son_gonderim_zamani}
_son_gonderim = {}


def _cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = IZINLI_ORIGIN
    resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return resp


def _yanit(ok, mesaj="", kod=200):
    resp = make_response(jsonify({"ok": ok, "mesaj": mesaj}), kod)
    return _cors(resp)


def _tek_satir(s):
    """E-posta başlık enjeksiyonunu önlemek için satır sonlarını temizler."""
    return re.sub(r"[\r\n]+", " ", str(s or "")).strip()


def _eposta_gecerli(e):
    return bool(re.match(r"^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$", e or "")) and len(e) <= 254


def _telefon_gecerli(t):
    if t == "":
        return True
    return bool(re.match(r"^[0-9]{10,15}$", re.sub(r"[\s()+.\-]", "", t)))


def _email_html(ad, eposta, telefon, konu, avukat, mesaj, zaman):
    """PHP sürümüyle aynı lacivert/altın temalı HTML e-posta gövdesi."""
    g = html.escape
    telefon_goster = g(telefon) if telefon else "—"
    mesaj_html = g(mesaj).replace("\n", "<br>")

    def satir(etiket, deger):
        return f"""
        <tr>
          <td style="padding:14px 24px;border-bottom:1px solid #ECE7DE;font-family:Arial,sans-serif;
                     font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#8A93A0;
                     white-space:nowrap;vertical-align:top;width:170px;">{etiket}</td>
          <td style="padding:14px 24px;border-bottom:1px solid #ECE7DE;font-family:Arial,sans-serif;
                     font-size:15px;color:#16202C;vertical-align:top;">{deger}</td>
        </tr>"""

    tel_buton = ""
    if telefon:
        tel_temiz = re.sub(r"[^0-9+]", "", telefon)
        tel_buton = (f'<a href="tel:{tel_temiz}" style="display:inline-block;background:#B4914F;'
                     f'color:#0A1628;text-decoration:none;font-family:Arial,sans-serif;font-size:13px;'
                     f'font-weight:bold;padding:12px 22px;border-radius:8px;">Telefonla Ara</a>')

    return f"""<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#EEF1F5;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF1F5;padding:28px 12px;">
    <tr><td align="center">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0"
             style="max-width:600px;width:100%;background:#FFFFFF;border-radius:12px;overflow:hidden;
                    box-shadow:0 8px 28px rgba(10,22,40,0.10);">

        <tr><td style="height:4px;background:linear-gradient(90deg,#B4914F,#C9A96A);font-size:0;line-height:0;">&nbsp;</td></tr>

        <tr><td style="background:#0A1628;padding:30px 32px;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-family:Georgia,'Times New Roman',serif;color:#FFFFFF;font-size:22px;font-weight:bold;">
              {g(BURO_ADI)}
              <div style="font-family:Arial,sans-serif;font-size:11px;letter-spacing:3px;
                          text-transform:uppercase;color:#C9A96A;margin-top:6px;">Yeni Randevu Talebi</div>
            </td>
            <td align="right" style="font-size:34px;">&#9878;</td>
          </tr></table>
        </td></tr>

        <tr><td style="padding:28px 32px 8px;font-family:Arial,sans-serif;font-size:15px;
                       line-height:1.6;color:#3C4757;">
          İnternet sitesindeki iletişim formu üzerinden yeni bir talep iletildi.
          Ayrıntılar aşağıdadır. Doğrudan yanıtlamak için bu e-postayı
          <strong>Yanıtla</strong> ile geçebilirsiniz.
        </td></tr>

        <tr><td style="padding:16px 8px 8px;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0"
                 style="border:1px solid #ECE7DE;border-radius:10px;overflow:hidden;">
            {satir("Ad Soyad", g(ad))}
            {satir("E-posta", f'<a href="mailto:{g(eposta)}" style="color:#16304F;text-decoration:none;">{g(eposta)}</a>')}
            {satir("Telefon", telefon_goster)}
            {satir("Hukuk Alanı", g(konu))}
            {satir("Görüşülecek Avukat", g(avukat))}
            {satir("Gönderim Zamanı", g(zaman))}
          </table>
        </td></tr>

        <tr><td style="padding:12px 32px 4px;font-family:Arial,sans-serif;font-size:11px;
                       letter-spacing:1.5px;text-transform:uppercase;color:#8A93A0;">Talep</td></tr>
        <tr><td style="padding:6px 32px 24px;">
          <div style="background:#F7F4EF;border-left:3px solid #B4914F;border-radius:6px;
                      padding:16px 20px;font-family:Arial,sans-serif;font-size:15px;
                      line-height:1.7;color:#16202C;">{mesaj_html}</div>
        </td></tr>

        <tr><td style="padding:0 32px 28px;">
          <a href="mailto:{g(eposta)}" style="display:inline-block;background:#0F2038;color:#fff;
             text-decoration:none;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;
             padding:12px 22px;border-radius:8px;margin-right:8px;">E-posta ile Yanıtla</a>
          {tel_buton}
        </td></tr>

        <tr><td style="background:#0A1628;padding:18px 32px;font-family:Arial,sans-serif;
                       font-size:12px;color:rgba(250,248,245,0.6);text-align:center;">
          Bu e-posta {g(BURO_ADI)} internet sitesindeki iletişim formu tarafından otomatik oluşturuldu.
        </td></tr>

      </table>
    </td></tr>
  </table>
</body></html>"""


@app.route("/gonder", methods=["POST", "OPTIONS"])
def gonder():
    # CORS ön-uçuş (preflight) isteği
    if request.method == "OPTIONS":
        return _cors(make_response("", 204))

    # SMTP yapılandırılmamışsa net hata ver
    if not SMTP_KULLANICI or not SMTP_SIFRE:
        return _yanit(False, "Sunucu e-posta ayarları yapılmamış (SMTP_KULLANICI/SMTP_SIFRE).", 500)

    # --- Veriyi oku ---
    d = request.get_json(silent=True) or request.form.to_dict() or {}
    if not d:
        return _yanit(False, "Boş istek.", 400)

    # --- Honeypot: gizli tuzak alan doluysa bot demektir ---
    if d.get("website"):
        return _yanit(True, "Alındı.")  # sessizce başarı

    # --- Hız sınırı (IP bazlı) ---
    ip = request.headers.get("X-Forwarded-For", request.remote_addr or "0.0.0.0").split(",")[0].strip()
    simdi = time.time()
    if ip in _son_gonderim and (simdi - _son_gonderim[ip]) < BEKLE_SANIYE:
        return _yanit(False, "Az önce bir mesaj gönderdiniz. Lütfen biraz sonra tekrar deneyin.", 429)

    # --- Alanları al ---
    ad      = _tek_satir(d.get("adSoyad", ""))
    eposta  = _tek_satir(d.get("eposta", "")).lower()
    telefon = _tek_satir(d.get("telefon", ""))
    konu    = _tek_satir(d.get("konu", ""))
    avukat  = _tek_satir(d.get("avukat", ""))
    mesaj   = (d.get("mesaj", "") or "").strip()
    zaman   = _tek_satir(d.get("zamanMetni", "")) or datetime.now().strftime("%d.%m.%Y %H:%M")

    # --- Sunucu tarafı doğrulama (istemcideki kurallarla aynı) ---
    hatalar = []
    if not (3 <= len(ad) <= 80):            hatalar.append("ad")
    if not _eposta_gecerli(eposta):         hatalar.append("eposta")
    if not _telefon_gecerli(telefon):       hatalar.append("telefon")
    if konu == "":                          hatalar.append("konu")
    if avukat == "":                        hatalar.append("avukat")
    if not (20 <= len(mesaj) <= MAX_MESAJ): hatalar.append("mesaj")
    if hatalar:
        return _yanit(False, "Bazı alanlar geçersiz: " + ", ".join(hatalar), 422)

    # --- E-postayı hazırla ---
    konu_satir = f"Yeni Randevu Talebi — {ad} ({konu})"
    govde = _email_html(ad, eposta, telefon, konu, avukat, mesaj, zaman)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = konu_satir
    msg["From"]    = formataddr((GONDEREN_AD, SMTP_KULLANICI))
    msg["To"]      = ALICI
    msg["Reply-To"] = formataddr((ad, eposta))   # "Yanıtla" doğrudan müvekkile gider
    # Düz metin alternatifi (HTML görüntülemeyen istemciler için)
    duz = (f"Yeni Randevu Talebi\n\nAd Soyad: {ad}\nE-posta: {eposta}\n"
           f"Telefon: {telefon or '—'}\nHukuk Alanı: {konu}\n"
           f"Görüşülecek Avukat: {avukat}\nGönderim Zamanı: {zaman}\n\nTalep:\n{mesaj}\n")
    msg.attach(MIMEText(duz, "plain", "utf-8"))
    msg.attach(MIMEText(govde, "html", "utf-8"))

    # --- SMTP ile gönder ---
    try:
        if SMTP_PORT == 465:
            ctx = ssl.create_default_context()
            with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ctx, timeout=20) as sunucu:
                sunucu.login(SMTP_KULLANICI, SMTP_SIFRE)
                sunucu.send_message(msg)
        else:
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as sunucu:
                sunucu.starttls(context=ssl.create_default_context())
                sunucu.login(SMTP_KULLANICI, SMTP_SIFRE)
                sunucu.send_message(msg)
    except Exception as e:  # noqa: BLE001
        app.logger.error("E-posta gönderilemedi: %s", e)
        return _yanit(False, "E-posta gönderilemedi. Lütfen daha sonra tekrar deneyin veya telefonla ulaşın.", 500)

    _son_gonderim[ip] = simdi
    return _yanit(True, "Talebiniz alındı.")


@app.route("/saglik", methods=["GET"])
def saglik():
    """Sunucunun ayakta olduğunu doğrulamak için basit uç nokta."""
    return jsonify({"ok": True, "servis": "gelegen-form", "smtp_yapili": bool(SMTP_KULLANICI and SMTP_SIFRE)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    # Üretimde debug=False; geliştirmede True yapabilirsiniz.
    app.run(host="0.0.0.0", port=port, debug=False)
