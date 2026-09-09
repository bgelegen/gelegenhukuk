# İletişim Formu Kurulumu

Formu çalışır hâle getirmek için **iki yol** var. Birini seçin. Her ikisinde de
talepler **batuhangelegen44@gmail.com** adresine düşer.

Varsayılan durumda form **hiçbir yere göndermez** (güvenli varsayılan): ziyaretçiye
"telefonla/e-posta ile ulaşın" mesajı gösterir. Aşağıdaki adımlardan biri
tamamlanınca form aktifleşir.

---

## YOL A — Web3Forms (KOLAY · sunucu gerekmez · ücretsiz) ⭐ önerilen

Statik hosting dâhil **her yerde** çalışır (Netlify, Cloudflare Pages, cPanel, GitHub Pages…).
Kurulum ~30 saniye.

### Adımlar
1. <https://web3forms.com> adresine gidin.
2. Ana sayfadaki kutuya **batuhangelegen44@gmail.com** yazıp **"Create Access Key"**e basın.
3. Bu adrese bir e-posta gelir; içindeki **Access Key**'i kopyalayın
   (örn. `a1b2c3d4-1234-5678-9abc-def012345678`).
4. `js/data.js` dosyasını açın ve anahtarı yapıştırın:

   ```js
   web3formsKey: "buraya-gelen-anahtari-yapistirin",
   formEndpoint: "",   // boş kalsın
   ```
5. Kaydedin, siteyi yayınlayın. Formu doldurup test edin — mesaj Gmail'inize düşecek.

### Web3Forms e-postası nasıl görünür?
Web3Forms, gönderilen alanları düzenli bir tablo hâlinde iletir. Konu satırı
otomatik olarak **"Yeni Randevu Talebi — [Ad Soyad] ([Hukuk Alanı])"** olur ve
e-postayı **Yanıtla** dediğinizde doğrudan müvekkile gider (reply-to ayarlı).

> İlk gönderimde Web3Forms bir **doğrulama e-postası** gönderebilir; onaylayın.
> Ücretsiz plan aylık 250 gönderim içerir (bir hukuk bürosu için fazlasıyla yeter).

---

## YOL B — Kendi Python Backend'iniz (TAM KONTROL · en güzel e-posta şablonu)

Python çalıştırabildiğiniz bir sunucu gerekir (kendi VPS'iniz veya PythonAnywhere,
Render, Railway gibi ücretsiz/uygun servisler). Bu yol, büronuzun kurumsal kimliğine
uygun **lacivert/altın temalı, tasarlanmış bir HTML e-posta** gönderir — hazır dosya:
`gonder.py` (Flask). E-posta **SMTP** ile iletilir (güvenilir teslimat).

### Adımlar

1. Gereksinimleri kurun:

   ```bash
   pip install -r requirements.txt
   ```

2. SMTP bilgilerini **ortam değişkeni** olarak verin (şifreyi koda yazmayın).
   Gmail SMTP örneği (Gmail'de 2 adımlı doğrulama açık olmalı ve bir
   **uygulama şifresi** üretmelisiniz — normal şifreniz çalışmaz):

   ```bash
   # Linux / macOS
   export SMTP_HOST=smtp.gmail.com
   export SMTP_PORT=587
   export SMTP_KULLANICI=gonderen@gmail.com      # e-postanın gönderileceği hesap
   export SMTP_SIFRE=uygulama-sifresi            # Google > Uygulama Şifreleri'nden
   export FORM_ALICI=batuhangelegen44@gmail.com  # taleplerin düşeceği adres
   ```

   ```powershell
   # Windows PowerShell
   $env:SMTP_HOST="smtp.gmail.com"; $env:SMTP_PORT="587"
   $env:SMTP_KULLANICI="gonderen@gmail.com"; $env:SMTP_SIFRE="uygulama-sifresi"
   $env:FORM_ALICI="batuhangelegen44@gmail.com"
   ```

3. Backend'i çalıştırın:

   ```bash
   python gonder.py          # geliştirme (http://0.0.0.0:5000)
   # veya üretim için:
   gunicorn gonder:app -b 0.0.0.0:5000
   ```

   `http://SUNUCU:5000/saglik` adresi `{"ok": true, "smtp_yapili": true}` dönerse hazırsınız.

4. `js/data.js` içinde:

   ```js
   web3formsKey: "",                             // boş kalsın
   formEndpoint: "https://sunucunuz:5000/gonder" // backend adresi
   ```

   > **Aynı alan adı önerilir:** Backend'i sitenizle aynı alan adı altında
   > (`https://www.gelegenhukuk.com/gonder`) bir **reverse-proxy** (Nginx/Apache)
   > arkasına koyarsanız `formEndpoint: "/gonder"` yazabilirsiniz; böylece CORS
   > gerekmez ve CSP `connect-src 'self'` yeterli olur.

### CORS / CSP notu
Backend **farklı bir origin/port**taysa:
- `gonder.py` içindeki `FORM_ORIGIN` ortam değişkenini sitenizin adresine ayarlayın
  (örn. `export FORM_ORIGIN=https://www.gelegenhukuk.com`).
- `.htaccess` / `_headers` içindeki CSP `connect-src` iznine backend adresini ekleyin.

### Gömülü güvenlik (gonder.py)
- Sunucu tarafı doğrulama (istemcideki kurallarla aynı)
- Honeypot (gizli tuzak alan) kontrolü
- IP bazlı hız sınırı (art arda spam'i frenler)
- HTML kaçışı (`html.escape`) → XSS koruması
- E-posta başlık enjeksiyonu önleme (satır sonu temizleme)

---

## Güvenlik (her iki yol için de geçerli)

Form zaten şu korumalarla gelir (bkz. `docs/GUVENLIK-PLANI.md`):

- **Honeypot** (gizli tuzak alan) — botları eler
- **Süre kontrolü** — 4 sn'den hızlı gönderimi reddeder
- **Hız sınırı** — art arda spam'i frenler (istemcide sessionStorage, Python'da IP bazlı)
- **Alan doğrulama** — istemci + (Python yolunda) sunucu tarafında tekrar
- **XSS koruması** — veriler kaçırılarak (escape) işlenir

### CSP notu
Web3Forms (Yol A) için `api.web3forms.com` adresi güvenlik başlıklarındaki
`connect-src` iznine **zaten eklenmiştir** (`.htaccess` ve `_headers`).
Başka bir servis kullanırsanız onun alan adını da eklemelisiniz.

---

## Hangi yolu seçmeliyim?

| | Web3Forms (A) | Python (B) |
|---|---|---|
| Kurulum kolaylığı | ⭐⭐⭐ (30 sn) | ⭐⭐ (sunucu + SMTP ayarı) |
| Sunucu gereksinimi | Yok | Python çalıştıran sunucu |
| E-posta tasarımı | Temiz, standart | **Tam kurumsal (lacivert/altın)** |
| Maliyet | Ücretsiz (250/ay) | Ücretsiz (sunucunuz) |
| Önerilen | Hızlı başlangıç | Kurumsal kimlik önemliyse |

**Tavsiye:** Hemen çalışsın istiyorsanız **Yol A** ile başlayın; ileride kendi
Python sunucunuza geçince **Yol B**'ye taşıyın (form kodu ikisini de destekler,
sadece `data.js`'te bir satır değişir).
