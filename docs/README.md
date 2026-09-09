# Gelegen Hukuk Bürosu — Kurumsal İnternet Sitesi

Av. Mustafa Gelegen ve Av. Merve Gelegen için hazırlanmış, **saf HTML + CSS + JavaScript**
ile geliştirilmiş statik site. Framework, derleme adımı ve `node_modules` yoktur —
dosyaları herhangi bir sunucuya kopyalamak yeterlidir.

---

## 1. Dosya ağacı

```
Web/
│
├── index.html                  Anasayfa (hero, çalışma alanları, ekip, süreç, SSS)
├── avukatlarimiz.html          Avukat profilleri
├── hakkimizda.html             Büro, ilkeler, hizmet kapsamı
├── iletisim.html               İletişim bilgileri + randevu formu + harita
├── kvkk.html                   KVKK aydınlatma metni (şablon)
├── 404.html                    Hata sayfası
│
├── css/
│   ├── style.css               Tasarım sistemi: tokenlar, reset, bileşenler (mobile-first)
│   ├── responsive.css          Tüm medya sorguları / kırılım noktaları
│   └── print.css               Yazdırma düzeni (media="print")
│
├── js/
│   ├── data.js                 ⭐ İLETİŞİM BİLGİLERİ VE AVUKAT PROFİLLERİ BURADA
│   ├── main.js                 Menü, kaydırma animasyonu, akordeon, modal, harita
│   └── form.js                 Form doğrulama + spam/güvenlik katmanı
│
├── assets/
│   ├── img/
│   │   ├── logo.svg                    Amblem (terazi)
│   │   ├── favicon.svg                 Tarayıcı sekme simgesi
│   │   ├── Mustafa_Gelegen.webp      Portre yer tutucusu  ← gerçek fotoğrafla değiştirin
│   │   ├── Merve_Gelegen.webp        Portre yer tutucusu  ← gerçek fotoğrafla değiştirin
│   │   ├── og-image.svg                Sosyal paylaşım görseli (kaynak)
│   │   └── og-image.png                Sosyal paylaşım görseli 1200×630 (kullanılan)
│   └── icons/
│       ├── apple-touch-icon.svg        iOS ana ekran simgesi
│       ├── icon-192.png                PWA simgesi
│       └── icon-512.png                PWA simgesi
│
├── docs/
│   ├── README.md               Bu dosya
│   ├── RESPONSIVE-PLAN.md      Mobil uyum planı (kırılım noktaları, test listesi)
│   ├── SEO-PLANI.md            SEO planı (başlık yapısı, meta, yapısal veri, reklam yasağı)
│   └── GUVENLIK-PLANI.md       Güvenlik planı (HTTPS, başlıklar, form, API anahtarları)
│
├── tools/
│   └── csp-hash.js             CSP için satır içi script hash üretici
│
├── gonder.py                   Form e-posta backend'i (Flask + SMTP) — bkz. docs/FORM-KURULUM.md
├── requirements.txt            Python gereksinimi (Flask)
│
├── .htaccess                   Apache: HTTPS zorunluluğu, güvenlik başlıkları, önbellek
├── _headers                    Netlify / Cloudflare Pages karşılığı
├── robots.txt                  Arama motoru tarama kuralları
├── sitemap.xml                 Site haritası
└── site.webmanifest            PWA / ana ekrana ekleme tanımı
```

**30 dosya · ~700 KB · harici JS kütüphanesi yok.**

---

## 2. Yerelde çalıştırma

`index.html` dosyasına çift tıklayarak da açabilirsiniz; ancak `fetch` ve manifest
davranışlarının doğru çalışması için küçük bir sunucu önerilir:

```bash
npx serve "C:/Users/batuh/OneDrive/Desktop/Web"
```

veya

```bash
python -m http.server 8000
```

Ardından tarayıcıdan `http://localhost:8000` adresini açın.

---

## 3. İçerik nasıl güncellenir?

### 3.1 İletişim bilgileri (telefon, e-posta, adres) — tek noktadan

`js/data.js` dosyasındaki `SITE` nesnesini düzenleyin. Sayfa yüklenince
`data-site="telefon"`, `data-site="eposta"`, `data-site="adres"` nitelikli tüm
elemanlar buradan otomatik güncellenir.

```js
telefon: "+90 551 821 44 44",        // tel: bağlantısı için
telefonGosterim: "+90 (551) 821 44 44",
eposta: "gelegenhukuk@gmail.com",
whatsapp: "905518214444",
```

> ⚠️ HTML'deki statik değerler bilerek bırakılmıştır: JavaScript kapalıyken ve
> arama motorları için içerik yine görünür olsun diye. **Yayına almadan önce
> HTML'deki karşılıklarını da elle güncelleyin** (footer + `iletisim.html` +
> `index.html` içindeki JSON-LD blokları).

### 3.2 Avukat özgeçmişleri

`js/data.js` → `AVUKATLAR` dizisi. Buradaki bilgiler "Detaylı Profil" penceresinde
gösterilir. Sayfada görünen ana metinler ise `avukatlarimiz.html` içindedir.

### 3.3 Gerçek fotoğraf ekleme

1. Fotoğrafları `assets/img/` klasörüne koyun (öneri: **800×1000 px**, `.webp` veya `.jpg`, < 200 KB).
2. `index.html` ve `avukatlarimiz.html` içindeki `src` değerlerini değiştirin:

```html
<img src="assets/img/av-mustafa-gelegen.webp" width="800" height="1000"
     alt="Av. Mustafa Gelegen portresi" loading="lazy" decoding="async">
```

3. `js/data.js` içindeki `foto` alanlarını da güncelleyin.
4. `width`/`height` niteliklerini **silmeyin** — sayfa kaymasını (CLS) önler.

### 3.4 Çalışma alanı ekleme/çıkarma

`index.html` içindeki `#calisma-alanlari` bölümünde `<article class="card">`
bloklarını çoğaltın veya silin. Izgara `auto-fit` olduğu için sütun sayısı
kendiliğinden ayarlanır — CSS'e dokunmanız gerekmez.

### 3.5 Renk ve tipografi

`css/style.css` en üstteki `:root` bloğu. Örneğin altın vurguyu değiştirmek için
`--c-gold-500` ve `--c-gold-400` değerlerini düzenlemek yeterlidir.

---

## 4. Formu çalışır hâle getirme

Varsayılan olarak form **gönderim yapmaz** (güvenli varsayılan): kullanıcıya telefon
ve e-posta seçenekleri gösterilir.

Aktifleştirmek için `js/data.js` içinde:

```js
formEndpoint: "https://formspree.io/f/XXXXXXX",
```

Sonrasında **mutlaka** yapılması gerekenler (detay: `docs/GUVENLIK-PLANI.md` §4.2):

- Sunucu tarafında aynı doğrulamaları tekrarlayın
- IP başına hız sınırı koyun
- `.htaccess` / `_headers` içindeki CSP `connect-src` direktifine uç nokta adresini ekleyin
- `kvkk.html` içindeki "Aktarım" başlığını, kullanılan servise göre güncelleyin

---

## 5. Yayına alma (deploy)

### Seçenek A — Klasik barındırma (cPanel / Plesk)

1. Tüm dosyaları `public_html/` içine yükleyin (**SFTP** ile, FTP değil).
2. `.htaccess` dosyasının yüklendiğinden emin olun (gizli dosya — FTP istemcisinde
   "gizli dosyaları göster" seçeneğini açın).
3. Let's Encrypt sertifikasını etkinleştirin.
4. `https://alanadiniz.com` adresini test edin.

### Seçenek B — Netlify / Cloudflare Pages (ücretsiz, HTTPS dahil)

1. Klasörü siteye sürükleyip bırakın veya bir Git deposuna bağlayın.
2. Build komutu: **yok**. Yayın klasörü: **kök dizin**.
3. `_headers` dosyası otomatik devreye girer.

### Yayın öncesi zorunlu değişiklikler

| Ne | Nerede |
|---|---|
| `gelegenhukuk.com` → gerçek alan adı | Tüm `.html` dosyaları (canonical, og:url, JSON-LD), `robots.txt`, `sitemap.xml`, `.htaccess` |
| Telefon / e-posta / adres | `js/data.js` + HTML footer'ları + JSON-LD |
| Baro adı, eğitim bilgileri | `js/data.js` → `AVUKATLAR`, `avukatlarimiz.html` |
| KVKK metni | `kvkk.html` (şablon uyarısını silin) |
| `sitemap.xml` tarihleri | `<lastmod>` |
| CSP hash'leri (JSON-LD değiştiyse) | `node tools/csp-hash.js` → `.htaccess` + `_headers` |

Tam kontrol listeleri: `docs/SEO-PLANI.md` §9 ve `docs/GUVENLIK-PLANI.md` §9.

---

## 6. Teknik notlar

- **Bağımlılık yok.** Tek harici kaynak Google Fonts'tur. İnternet erişimi olmayan
  ortamda da site çalışır (sistem yazı tiplerine düşer). Tamamen yerel istiyorsanız
  yazı tiplerini indirip `assets/fonts/` altına koyun ve `@font-face` tanımlayın.
- **Progressive enhancement:** JavaScript kapalıyken tüm içerik okunur; yalnızca
  mobil menü, modal ve form doğrulama devre dışı kalır. Menü bağlantıları normal
  bağlantı olduğu için gezinme yine mümkündür.
- **Erişilebilirlik:** WCAG 2.1 AA hedeflenmiştir — semantik HTML, `aria-*`
  nitelikleri, klavye desteği, odak halkaları, 48px dokunma hedefleri,
  `prefers-reduced-motion` ve `prefers-contrast` desteği.
- **Tarayıcı desteği:** Chrome/Edge/Firefox/Safari güncel sürümler. `clamp()`,
  `aspect-ratio`, `IntersectionObserver` kullanılır; konteyner sorguları
  `@supports` ile korumalıdır.

---

## 7. Yasal hatırlatma

Site içeriği **TBB Reklam Yasağı Yönetmeliği** gözetilerek yazılmıştır: başarı oranı,
kazanılmış dava sayısı, müvekkil yorumu ve iddialı nitelemeler bilinçli olarak
kullanılmamıştır. İçerik eklerken bu çerçevenin korunması gerekir. Ayrıca
yönetmelik uyarınca **internet sitesinin bağlı bulunulan baroya bildirilmesi**
gerekmektedir.
