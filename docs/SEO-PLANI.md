# SEO Temel Planı

**Proje:** Gelegen Hukuk Bürosu · **Hedef:** Yerel arama görünürlüğü (ör. "Ankara boşanma avukatı")

---

## 0. ÖNCE BU: Avukatlık reklam yasağı

Türkiye'de avukatlık hizmetlerinin tanıtımı **Avukatlık Kanunu m. 55** ve
**TBB Reklam Yasağı Yönetmeliği** ile sınırlandırılmıştır. SEO çalışması bu
sınırların içinde kalmalıdır. Site bu kurallara göre kurgulanmıştır:

| ❌ Yapılmayacak | ✅ Bunun yerine |
|---|---|
| "En iyi avukat", "kazandıran avukat" gibi iddialar | Nötr, bilgilendirici dil |
| Başarı oranı / kazanılmış dava sayısı | Çalışma alanları ve süreç anlatımı |
| Müvekkil yorumu, referans listesi | Bilgilendirici SSS bölümü |
| Google Ads / sponsorlu bağlantı ile üst sıra satın alma | Organik, içerik temelli görünürlük |
| Arama motoruna yönelik gizli anahtar kelime yığma | Doğal metin içinde geçen terimler |
| Ücret tarifesi ilanı, indirim/kampanya duyurusu | "Ücret görüşmede yazılı belirlenir" bilgisi |

> Yönetmelik, internet sitesinin **yalnızca bilgilendirme amaçlı** olmasına ve
> avukatın adı, unvanı, iletişim bilgileri, çalışma alanları gibi objektif bilgileri
> içermesine izin verir. Sitedeki tüm sayfalarda footer'da yasal uyarı bulunur.

---

## 1. Başlık (title) yapısı

**Kural:** `Sayfa Konusu | Marka` — 50–60 karakter arası, her sayfada **benzersiz**.

| Sayfa | `<title>` | Karakter |
|---|---|---|
| Anasayfa | `Gelegen Hukuk Bürosu \| Av. Mustafa Gelegen & Av. Merve Gelegen` | ~58 |
| Avukatlarımız | `Avukatlarımız \| Av. Mustafa Gelegen, Av. Merve Gelegen` | ~54 |
| Hakkımızda | `Hakkımızda \| Gelegen Hukuk Bürosu` | ~34 |
| İletişim | `İletişim ve Randevu \| Gelegen Hukuk Bürosu` | ~42 |
| KVKK | `KVKK Aydınlatma Metni \| Gelegen Hukuk Bürosu` | ~44 |
| 404 | `Sayfa Bulunamadı (404) \| Gelegen Hukuk Bürosu` | — |

## 2. Başlık hiyerarşisi (H1–H3)

- Her sayfada **tek bir `<h1>`** vardır ve sayfanın konusunu tanımlar.
- Bölüm başlıkları `<h2>`, alt kırılımlar `<h3>` ile ilerler; seviye atlanmaz.
- Görsel amaçlı büyük metinler için başlık etiketi kullanılmaz (CSS ile boyutlandırılır).
- Her `<section>` bir `aria-labelledby` ile kendi başlığına bağlanır → hem erişilebilirlik hem anlamsal netlik.

```
index.html
└── h1  Hukuki süreçlerinizde güvenilir yol arkadaşınız
    ├── h2  Hangi konularda destek veriyoruz?      → h3 × 8 (çalışma alanları)
    ├── h2  Avukatlarımız                          → h3 × 2
    ├── h2  Anlaşılır hukuk, öngörülebilir süreç
    ├── h2  İlk görüşmeden sonuca kadar            → h3 × 4 (süreç)
    └── h2  Merak edilenler                        → SSS
```

## 3. Meta etiketler

Her sayfada bulunanlar:

```html
<meta name="description" content="…150–160 karakter, eylem çağrısı içeren özet…">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://www.gelegenhukuk.com/…">
<meta property="og:title" / "og:description" / "og:image" / "og:url" / "og:type">
<meta name="twitter:card" content="summary_large_image">
<html lang="tr">  ·  <meta charset="UTF-8">  ·  viewport
```

- **404.html** → `noindex, follow` (hata sayfası dizine girmemeli).
- **Canonical**, `www` sürümüne ve HTTPS'e sabitlenmiştir; `.htaccess` de aynı adrese 301 yönlendirir → içerik tekrarı (duplicate content) önlenir.
- Açıklamalar birbirinin kopyası değildir; her sayfa kendi konusunu anlatır.

## 4. Yapısal veri (Schema.org / JSON-LD)

| Sayfa | Şema |
|---|---|
| index | `LegalService` + `Attorney` (ad, adres, telefon, çalışma saatleri, hizmet alanları), 2 × `Person`, `WebSite` |
| avukatlarimiz | `BreadcrumbList` + 2 × `Person` (baro, diller, uzmanlık alanları) |
| hakkimizda | `BreadcrumbList` |
| iletisim | `BreadcrumbList` + `ContactPage` |

Doğrulama: <https://search.google.com/test/rich-results> ve <https://validator.schema.org>

> `LegalService` şeması yerel işletme (Local Business) ailesindendir; Google'ın
> harita ve "yakınımdaki" sonuçlarında görünürlüğe katkı sağlar.

## 5. Yerel SEO (en yüksek getirili adım)

1. **Google Business Profile** kaydı açın — hukuk büroları için kategori: *Avukat / Hukuk bürosu*.
2. **NAP tutarlılığı**: Ad, Adres, Telefon; sitede, Google profilinde ve barodaki kayıtta **birebir aynı** yazılmalı.
3. Adres ve telefonu HTML'de metin olarak bulundurun (görsel içine gömmeyin) — sitede `data-site` ile tek yerden yönetiliyor.
4. Baro levhası ve varsa meslek dizinlerindeki kayıtları güncelleyin (alıntı/citation değeri).
5. Çalışma saatlerini hem sitede hem Google profilinde eşitleyin.

## 6. Teknik SEO

| Konu | Durum |
|---|---|
| `robots.txt` | ✅ Var — `docs/` ve `404.html` hariç tutulmuş, sitemap bildirilmiş |
| `sitemap.xml` | ✅ Var — 5 URL, `lastmod`/`priority` tanımlı |
| HTTPS | ✅ `.htaccess` ile 301 zorunlu yönlendirme |
| Tek kanonik alan adı | ✅ `gelegenhukuk.com` → `www.gelegenhukuk.com` |
| Mobil uyum | ✅ Mobile-first, `viewport` tanımlı (Google mobile-first indexing) |
| Sayfa hızı | ✅ Sıfır JS kütüphanesi, ~15KB JS, SVG görseller, `defer`, uzun önbellek |
| CLS | ✅ Görsellerde `width`/`height`, fontlarda `display=swap` |
| Semantik HTML | ✅ `header/nav/main/section/article/aside/footer` |
| İçerik JS'e bağımlı değil | ✅ Tüm metin HTML'de statik — arama motorları JS çalıştırmadan okur |
| Kırık bağlantı | Yayın sonrası kontrol edin |
| 404 sayfası | ✅ Özel sayfa, `.htaccess` ile bağlı |

## 7. İçerik planı (yayın sonrası büyüme)

Reklam yasağına uygun kalarak görünürlük artırmanın **tek sürdürülebilir yolu
bilgilendirici içeriktir**:

1. **Blog / Makaleler bölümü açın** (`makaleler.html` + tekil sayfalar).
   Örnek başlıklar: "Anlaşmalı boşanma nasıl yapılır, hangi belgeler gerekir?",
   "İşe iade davasında süreler", "İcra takibine itiraz nasıl yapılır?"
2. Her makale: 800+ kelime, tek `h1`, alt başlıklar, `Article` şeması, yayın tarihi.
3. Makaleleri `sitemap.xml`'e ekleyin.
4. SSS bölümünü genişletin — arama motorları soru-cevap içeriğini iyi eşleştirir.
5. **Yapmayın:** başka sitelerden kopyala-yapıştır içerik (kopya içerik cezası) veya ücretli bağlantı satın alma.

## 8. Ölçümleme

| Araç | Amaç | Not |
|---|---|---|
| Google Search Console | Dizine ekleme, tıklama/gösterim, kırık bağlantı | Alan adı doğrulaması + sitemap gönderimi |
| Google Analytics 4 / Plausible | Trafik analizi | **KVKK:** GA4 kullanılacaksa çerez onayı ve aydınlatma metni güncellenmelidir. Çerezsiz Plausible/Umami daha basit uyum sağlar. |
| PageSpeed Insights | Core Web Vitals | LCP < 2.5s, CLS < 0.1, INP < 200ms hedefi |
| Rich Results Test | Yapısal veri doğrulama | Her şablon değişikliğinde |

## 9. Yayın öncesi SEO kontrol listesi

- [ ] Tüm dosyalardaki `gelegenhukuk.com` alan adını gerçek alan adıyla değiştirin
      (`index.html`, diğer HTML'ler, `robots.txt`, `sitemap.xml`, `.htaccess`)
- [ ] `og:image` mutlak URL'i gerçek alan adına göre güncelleyin
- [ ] Telefon, e-posta, adres bilgilerini `js/data.js` + HTML + JSON-LD'de eşitleyin
- [ ] `sitemap.xml` içindeki `lastmod` tarihlerini güncelleyin
- [ ] Search Console'a site haritasını gönderin
- [ ] Google Business Profile kaydını açın
- [ ] Rich Results Test'ten geçirin
- [ ] Baro'ya sitenin bildirimini yapın (TBB Yönetmeliği m. 9 — internet sitesinin baroya bildirilmesi)
