# Güvenlik Önlemleri Planı

**Proje:** Gelegen Hukuk Bürosu

> Hukuk bürosu sitesi, sıradan bir kurumsal siteden farklıdır: ziyaretçi çoğu zaman
> **hassas bir hukuki sorunu** anlatır. Bu nedenle güvenlik yalnızca teknik bir
> gereklilik değil, **mesleki sır saklama yükümlülüğünün (Avukatlık Kanunu m. 36)
> teknik uzantısıdır.**

---

## 1. Tehdit modeli — neyi, kimden koruyoruz?

| Varlık | Tehdit | Önlem |
|---|---|---|
| Form üzerinden iletilen talep metni | Ağ dinleme, sunucuda sızıntı | HTTPS/HSTS, kısa saklama süresi, hassas veri paylaşımını caydıran uyarı |
| Ziyaretçinin site ziyaret ettiği bilgisi | Referrer sızıntısı, 3. taraf izleme | `Referrer-Policy`, izleme çerezi yok, tıkla-yükle harita |
| Site içeriği | Defacement (içerik değiştirme), XSS | CSP, `nosniff`, panel/FTP güvenliği, düzenli yedek |
| Büro e-posta hesabı | Kimlik avı, hesap ele geçirme | 2FA, SPF/DKIM/DMARC |
| Form uç noktası | Spam, bot, kaynak tüketimi | Honeypot, süre kontrolü, hız sınırı, sunucu tarafı doğrulama |

---

## 2. HTTPS ve taşıma güvenliği

| Önlem | Uygulama |
|---|---|
| SSL/TLS sertifikası | Let's Encrypt (ücretsiz, otomatik yenilemeli) veya barındırma sağlayıcısının sertifikası. **Sitenin tamamı HTTPS olmalı.** |
| Zorunlu yönlendirme | `.htaccess` → `http://` ve `www`suz istekler **301** ile `https://www.…` adresine yönlendirilir |
| HSTS | `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload` — tarayıcı 1 yıl boyunca HTTP denemez |
| Karışık içerik (mixed content) | Tüm kaynaklar HTTPS'ten yüklenir; `upgrade-insecure-requests` direktifi eklendi |
| TLS sürümü | Sunucuda TLS 1.2 ve 1.3 açık, 1.0/1.1 kapalı olmalı |

⚠️ **HSTS uyarısı:** Sertifika düzgün çalışmadan HSTS'i açmayın. Tarayıcı politikayı
önbelleğe alır ve site bir süre erişilemez hâle gelebilir. Önce `max-age=300` ile
test edip sonra 31536000'e çıkarın.

Doğrulama: <https://www.ssllabs.com/ssltest/> (hedef: **A** veya üzeri)

---

## 3. Güvenlik başlıkları (`.htaccess` / `_headers`)

| Başlık | Değer | Ne engeller? |
|---|---|---|
| `Content-Security-Policy` | Aşağıda | XSS, veri sızdırma, yetkisiz kaynak yükleme |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains; preload` | Protokol düşürme saldırısı |
| `X-Frame-Options` | `SAMEORIGIN` | Clickjacking (siteyi iframe'e gömüp tıklama çalma) |
| `X-Content-Type-Options` | `nosniff` | MIME tipi tahmini ile script çalıştırma |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Ziyaret edilen sayfa yolunun 3. taraflara sızması |
| `Permissions-Policy` | kamera/mikrofon/konum kapalı | Gereksiz cihaz izinleri |
| `Cross-Origin-Opener-Policy` | `same-origin` | Çapraz pencere saldırıları |

### CSP politikası ve neden bu şekilde

```
default-src 'self';
base-uri 'self';                    → <base> etiketiyle adres kaçırma engellenir
object-src 'none';                  → Flash/plugin tamamen kapalı
frame-ancestors 'self';             → X-Frame-Options'ın modern karşılığı
form-action 'self';                 → form verisi başka siteye POST edilemez
script-src 'self' 'sha256-…' × 4;   → satır içi JSON-LD blokları HASH ile izinli
style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
font-src 'self' https://fonts.gstatic.com;
img-src 'self' data:;
frame-src https://maps.google.com https://www.google.com;
connect-src 'self';
upgrade-insecure-requests
```

**Önemli:** `script-src` içinde `'unsafe-inline'` **yoktur**. Sayfalardaki tek satır içi
script türü SEO için gereken JSON-LD'dir ve her biri SHA-256 hash'i ile izinlidir.

```bash
node tools/csp-hash.js
```

> JSON-LD bloklarını her düzenlediğinizde bu komutu çalıştırıp `.htaccess` ve
> `_headers` içindeki hash'leri güncelleyin — aksi hâlde yapısal veri CSP tarafından
> engellenir ve SEO'da görünmez.

**Form bir API'ye bağlanacaksa:** `connect-src 'self' https://api-adresiniz.com` olarak genişletin.

### Nginx karşılığı

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Content-Security-Policy "default-src 'self'; …" always;
```

Doğrulama: <https://securityheaders.com> (hedef: **A**)

---

## 4. Form güvenliği

### 4.1 İstemci tarafı (uygulandı — `js/form.js`)

| # | Önlem | Açıklama |
|---|---|---|
| 1 | **Honeypot** | `website` adlı görünmez alan. İnsan göremez, bot doldurur → gönderim reddedilir. |
| 2 | **Süre kontrolü** | Sayfa açılışından itibaren **4 saniyeden** hızlı gönderim reddedilir. |
| 3 | **Hız sınırı** | `sessionStorage` ile aynı ziyaretçi **60 saniyede** bir gönderebilir. |
| 4 | **Alan doğrulama** | Ad (3–80, harf), e-posta (regex + max 254), telefon (10–15 rakam), mesaj (20–2000). |
| 5 | **Girdi temizleme** | Kontrol karakterleri ve sıfır genişlikli karakterler (`U+200B–200D`, BOM) silinir. |
| 6 | **XSS önlemi** | DOM'a yazarken **hiçbir yerde `innerHTML` kullanılmaz** — yalnızca `textContent` / `createElement`. |
| 7 | **KVKK açık rıza** | Onay kutusu zorunlu; aydınlatma metnine bağlantı verilir. |
| 8 | **Zaman aşımı** | `AbortController` ile 15 saniyede istek iptal edilir. |
| 9 | **Çerezsiz istek** | `fetch(..., { credentials: "omit" })` → CSRF yüzeyi daraltılır. |

### 4.2 ⚠️ Sunucu tarafı (YAPILMASI GEREKEN)

> **İstemci doğrulaması güvenlik sınırı değildir.** Saldırgan tarayıcıyı hiç
> kullanmadan doğrudan uç noktaya istek gönderebilir. Aşağıdakiler sunucuda
> **tekrar** uygulanmalıdır:

- [ ] Tüm alanların tip/uzunluk/biçim doğrulaması (istemcidekiyle aynı kurallar)
- [ ] **Hız sınırı**: IP başına saatte en fazla 5 gönderim (`express-rate-limit`, Cloudflare Rate Limiting vb.)
- [ ] **CSRF token** (oturum tabanlı bir backend varsa) veya `Origin`/`Referer` başlığı kontrolü
- [ ] **CAPTCHA**: Spam yoğunlaşırsa Cloudflare Turnstile veya hCaptcha (gizlilik dostu; reCAPTCHA'ya göre daha az veri toplar)
- [ ] Gelen veriyi e-postaya/veritabanına yazarken **kaçırma (escaping)** — HTML e-posta şablonunda `<`, `>`, `&` dönüştürülmeli
- [ ] Dosya yükleme **kapalı** kalmalı (form dosya kabul etmiyor — bu bilinçli bir karardır)
- [ ] Sunucu kayıtlarında (log) mesaj içeriği **tutulmamalı**, yalnızca zaman damgası ve durum

### 4.3 Form altyapısı seçenekleri

| Seçenek | Artı | Eksi |
|---|---|---|
| **Formspree / Basin** (`js/data.js` → `formEndpoint`) | Sunucu gerekmez, hızlı | Veri 3. tarafta işlenir → KVKK aktarım maddesi güncellenmeli |
| **Kendi Python/Node uç noktanız** | Veri kendi sunucunuzda | Bakım ve güvenlik sizde |
| **Netlify Forms** | Barındırma ile bütünleşik | Sağlayıcıya bağımlılık |
| **Form yok, sadece telefon/e-posta** | En düşük risk | Dönüşüm düşer |

Varsayılan olarak `formEndpoint` **boştur**: form gönderim yapmaz, kullanıcıya telefon
ve e-posta seçenekleri gösterilir. Böylece yanlışlıkla yapılandırılmamış bir formla
yayına çıkıp veri kaybı yaşanmaz.

---

## 5. API anahtarlarının korunması

> **Altın kural: İstemci tarafına konan hiçbir anahtar gizli değildir.**
> HTML/JS/CSS dosyalarına yazılan her şey, ziyaretçinin tarayıcısında açıkça görülebilir.

| Durum | Doğru yaklaşım |
|---|---|
| **Google Maps** | Bu sitede **API anahtarı kullanılmıyor.** Harita, anahtar gerektirmeyen `maps.google.com/maps?q=…&output=embed` adresiyle ve yalnızca kullanıcı onayıyla yükleniyor. |
| Anahtar gerekirse (Maps JS API) | Google Cloud Console'da anahtarı **HTTP referrer** kısıtına bağlayın (`https://www.gelegenhukuk.com/*`) ve yalnızca gerekli API'yi etkinleştirin. Kısıtlanmış anahtar istemcide bulunabilir. |
| E-posta gönderim anahtarı (SendGrid, Resend, SMTP şifresi) | **ASLA** istemciye konmaz. Sunucu tarafında ortam değişkeni (`.env`) olarak tutulur, `.env` dosyası sürüm kontrolüne eklenmez. |
| Analytics ölçüm kimliği | Zaten herkese açıktır (gizli değildir), sorun değil. |
| Sızmış anahtar | Derhal **iptal edip yenileyin** (rotate). Git geçmişinden silmek yeterli değildir. |

`.htaccess` ile `.env`, `.git`, `*.md`, `docs/` ve `tools/` yolları web'den erişime kapatılmıştır.

---

## 6. Barındırma ve altyapı

- [ ] Barındırma paneli (cPanel/Plesk) ve FTP/SSH için **güçlü parola + 2FA**
- [ ] FTP yerine **SFTP/SSH** kullanın (FTP parolayı düz metin gönderir)
- [ ] Dizin listeleme kapalı (`Options -Indexes` — uygulandı)
- [ ] Otomatik **günlük yedek**; yedekler site sunucusundan ayrı bir yerde tutulmalı
- [ ] Sunucu yazılımı sürüm bilgisini gizleyin (`ServerTokens Prod`, `ServerSignature Off`)
- [ ] **WAF/CDN**: Cloudflare ücretsiz planı bile DDoS ve bot filtresi sağlar
- [ ] Alan adı kaydında **domain lock** ve kayıt şirketi hesabında 2FA

## 7. E-posta güvenliği (kimlik avı önlemi)

Büro adına sahte e-posta gönderilmesini engellemek için DNS kayıtları:

```
SPF    TXT  "v=spf1 include:_spf.saglayici.com -all"
DKIM   TXT  (sağlayıcının verdiği imza anahtarı)
DMARC  TXT  "v=DMARC1; p=quarantine; rua=mailto:dmarc@gelegenhukuk.com"
```

Müvekkil belgeleri e-posta ile paylaşılacaksa **şifreli arşiv** veya güvenli dosya
paylaşım servisi tercih edilmelidir.

## 8. KVKK / gizlilik uyumu

| Gereklilik | Durum |
|---|---|
| Aydınlatma metni | ✅ `kvkk.html` (şablon — büro tarafından doldurulmalı) |
| Açık rıza | ✅ Formda zorunlu onay kutusu |
| Veri minimizasyonu | ✅ Yalnızca ad, e-posta, telefon, konu, mesaj toplanır |
| Üçüncü taraf izleme | ✅ Analytics/reklam çerezi yok |
| Harita gizliliği | ✅ Tıkla-yükle — onay verilmeden Google'a istek gitmez |
| Veri saklama süresi | ✅ Vekâlete dönüşmeyen talepler ≤ 6 ay |
| VERBİS kaydı | Büronun yükümlülük durumuna göre değerlendirilmeli |

## 9. Yayın öncesi güvenlik kontrol listesi

- [ ] SSL sertifikası kurulu, `https://` çalışıyor
- [ ] `http://` ve `www`suz adresler 301 ile yönlendiriliyor
- [ ] `.htaccess` (veya `_headers`) sunucuda etkin — başlıklar geliyor mu?
- [ ] <https://securityheaders.com> → **A**
- [ ] <https://www.ssllabs.com/ssltest/> → **A**
- [ ] `docs/`, `tools/`, `.htaccess` tarayıcıdan erişilemiyor (403 dönmeli)
- [ ] Form: honeypot dolu gönderim reddediliyor mu?
- [ ] Form: sunucu tarafı doğrulama ve hız sınırı devrede mi?
- [ ] `js/data.js` içinde gerçek gizli anahtar **yok**
- [ ] Yedekleme çalışıyor ve geri yükleme test edildi
- [ ] Tarayıcı konsolunda CSP ihlali hatası yok

## 10. Yayın sonrası bakım

| Periyot | İş |
|---|---|
| Haftalık | Form kutusunu kontrol edin, spam eğilimini izleyin |
| Aylık | Yedeklerin alındığını doğrulayın; kırık bağlantı taraması |
| 3 ayda bir | securityheaders.com + SSL Labs testini tekrarlayın |
| Yıllık | Sertifika, alan adı yenileme; KVKK metnini gözden geçirin |
| Değişiklik sonrası | `node tools/csp-hash.js` çalıştırıp CSP hash'lerini güncelleyin |
