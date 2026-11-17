# -*- coding: utf-8 -*-
"""
Gelegen Hukuk — sayfa şablonları (makaleler ve çalışma alanı sayfaları için).
Elle yazılmış sayfalarla (index, hakkimizda…) birebir aynı başlık/altbilgiyi üretir.
Kullanım: tools/uret.py bu dosyayı içe aktarır; doğrudan çalıştırılmaz.
"""
import json

SITE = "https://gelegenhukuk.com/"
CSS_V = "56"
RESP_V = "44"
PRINT_V = "40"
DATA_V = "35"
MAIN_V = "35"

# Altbilgideki "Çalışma Alanları" listesi — tüm sayfalarda aynı
FOOTER_ALANLAR = [
    ("malatya-bosanma-avukati.html", "Aile ve Boşanma Hukuku"),
    ("malatya-ceza-avukati.html", "Ceza Hukuku"),
    ("malatya-is-hukuku-avukati.html", "İş Hukuku"),
    ("malatya-icra-avukati.html", "İcra ve İflas Hukuku"),
    ("malatya-gayrimenkul-avukati.html", "Gayrimenkul Hukuku"),
    ("malatya-miras-avukati.html", "Miras Hukuku"),
    ("calisma-alanlari.html", "Tüm çalışma alanları"),
]


def footer_alanlar_html(indent="            "):
    return "\n".join(f'{indent}<li><a href="{u}">{t}</a></li>' for u, t in FOOTER_ALANLAR)


def head(title, desc, slug, jsonld, ogtype="website", ogtitle=None, ogdesc=None, aktif=None):
    nav = [("index.html", "Anasayfa"), ("avukatlarimiz.html", "Avukatlarımız"),
           ("hakkimizda.html", "Hakkımızda"), ("makaleler.html", "Makaleler"),
           ("iletisim.html", "İletişim")]
    cur = ' aria-current="page"'
    nav_html = "\n".join(
        f'          <li><a href="{u}"{cur if u == aktif else ""}>{t}</a></li>'
        for u, t in nav)
    ld = json.dumps(jsonld, ensure_ascii=False, indent=2)
    ld = "\n".join("  " + line for line in ld.splitlines())
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="#0A1424">

  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="{SITE}{slug}">

  <meta property="og:type" content="{ogtype}">
  <meta property="og:locale" content="tr_TR">
  <meta property="og:site_name" content="Gelegen Hukuk Bürosu">
  <meta property="og:title" content="{ogtitle or title}">
  <meta property="og:description" content="{ogdesc or desc}">
  <meta property="og:url" content="{SITE}{slug}">
  <meta property="og:image" content="{SITE}assets/img/og-image.png">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" type="image/png" sizes="48x48" href="/assets/icons/logo-48.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/assets/icons/logo-192.png">
  <link rel="apple-touch-icon" href="/assets/icons/logo-180.png">
  <link rel="manifest" href="/site.webmanifest">

  <link rel="preload" href="assets/fonts/libre-caslon-display-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/public-sans-latin.woff2" as="font" type="font/woff2" crossorigin>

  <script>document.documentElement.classList.add("js");</script>

  <link rel="stylesheet" href="css/style.css?v={CSS_V}">
  <link rel="stylesheet" href="css/responsive.css?v={RESP_V}">
  <link rel="stylesheet" href="css/print.css?v={PRINT_V}" media="print">

  <script type="application/ld+json">
{ld}
  </script>
</head>

<body>
  <a class="skip-link" href="#main">İçeriğe atla</a>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="brand" href="index.html" aria-label="Gelegen Hukuk Bürosu — Anasayfa">
        <img class="brand__logo" src="assets/img/logo-sm.png" alt="Gelegen Hukuk Bürosu logosu" width="42" height="42">
        <span class="brand__text">
          <span class="brand__name" translate="no">Gelegen</span>
          <span class="brand__sub">Hukuk Bürosu</span>
        </span>
      </a>

      <nav class="site-nav" id="site-nav" aria-label="Ana menü">
        <ul>
{nav_html}
        </ul>
        <div class="site-nav__cta">
          <a class="site-nav__phone" href="tel:+905518214444" data-site="telefon">+90 (551) 821 44 44</a>
          <a class="btn btn--primary btn--block" href="iletisim.html">Randevu Talebi</a>
        </div>
      </nav>

      <a class="btn btn--primary btn--sm header-cta" href="iletisim.html">Randevu Talebi</a>

      <button class="nav-toggle" type="button" aria-label="Menüyü aç/kapat" aria-expanded="false" aria-controls="site-nav">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
  <div class="nav-backdrop" role="presentation"></div>

  <main id="main">
"""


def foot():
    return f"""  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a class="brand" href="index.html">
            <img class="brand__logo" src="assets/img/logo-sm.png" alt="Gelegen Hukuk Bürosu logosu" width="42" height="42">
            <span class="brand__text">
              <span class="brand__name" translate="no">Gelegen</span>
              <span class="brand__sub">Hukuk Bürosu</span>
            </span>
          </a>
          <p>
            Av. Mustafa Gelegen ve Av. Merve Gelegen tarafından yürütülen büromuz, bireysel ve
            kurumsal müvekkillere hukuki danışmanlık ve dava takibi hizmeti sunmaktadır.
          </p>
        </div>

        <nav aria-label="Alt menü">
          <h4>Sayfalar</h4>
          <ul class="footer-links">
            <li><a href="index.html">Anasayfa</a></li>
            <li><a href="avukatlarimiz.html">Avukatlarımız</a></li>
            <li><a href="hakkimizda.html">Hakkımızda</a></li>
            <li><a href="makaleler.html">Makaleler</a></li>
            <li><a href="iletisim.html">İletişim</a></li>
          </ul>
        </nav>

        <nav aria-label="Çalışma alanları">
          <h4>Çalışma Alanları</h4>
          <ul class="footer-links">
{footer_alanlar_html()}
          </ul>
        </nav>

        <div>
          <h4>İletişim</h4>
          <ul class="footer-contact">
            <li><a href="tel:+905518214444" data-site="telefon">+90 (551) 821 44 44</a></li>
            <li><a href="mailto:gelegenhukuk@gmail.com" data-site="eposta">gelegenhukuk@gmail.com</a></li>
            <li><a href="https://www.google.com/maps/dir/?api=1&amp;destination=38.34786793972292,38.32065000710417" target="_blank" rel="noopener noreferrer" data-site="adres">Saray Mahallesi, Murat Kurum Caddesi, G-&#8288;05 Blok, Dış Kapı No: 12, Kat: 2, Daire: 17, Battalgazi / Malatya</a></li>
            <li>Pazartesi – Cuma: 09:00 – 18:00</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© <span data-year>2026</span> Gelegen Hukuk Bürosu. Tüm hakları saklıdır.</p>
        <p><a href="kvkk.html">KVKK Aydınlatma Metni</a></p>
        <p class="footer-credit">Design by <a href="https://batuhangelegen.dev" target="_blank" rel="noopener">Batuhan Gelegen</a></p>
      </div>
    </div>
  </footer>

  <div class="fab-stack">
    <button class="fab" id="backToTop" type="button" aria-label="Sayfanın başına dön">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
    </button>
  </div>

  <script src="js/data.js?v={DATA_V}"></script>
  <script src="js/main.js?v={MAIN_V}" defer></script>
</body>
</html>
"""


def hero(baslik, yol, alt=None):
    """yol: [(href veya None, ad), ...] — son öğe geçerli sayfa."""
    lis = []
    for href, ad in yol:
        lis.append(f'            <li><a href="{href}">{ad}</a></li>' if href
                   else f'            <li aria-current="page">{ad}</li>')
    alt_html = f"\n        <p>\n          {alt}\n        </p>" if alt else ""
    return f"""
    <section class="page-hero">
      <div class="container page-hero__inner">
        <nav class="breadcrumb" aria-label="Sayfa yolu">
          <ol>
{chr(10).join(lis)}
          </ol>
        </nav>
        <h1>{baslik}</h1>{alt_html}
      </div>
    </section>
"""


def cta(baslik="Dosyanızı birlikte değerlendirelim",
        metin="Konuyla ilgili sorularınız için büromuzla iletişime geçebilir, randevu talep edebilirsiniz."):
    return f"""
    <section class="section section--tight">
      <div class="container">
        <div class="cta-band reveal">
          <p class="eyebrow eyebrow--light">Randevu</p>
          <h2>{baslik}</h2>
          <p>{metin}</p>
          <div class="cta-band__actions">
            <a class="btn btn--primary" href="tel:+905518214444" data-site="telefon" data-site-keep>Telefonla Ulaşın</a>
            <a class="btn btn--ghost" href="iletisim.html">İletişim Formu</a>
          </div>
        </div>
      </div>
    </section>
"""


UYARI = """          <div class="article-note">
            <p><strong>Bilgilendirme:</strong> Bu yazı yalnızca genel bilgilendirme amaçlıdır; somut
            olayınıza ilişkin hukuki görüş yerine geçmez. Süreler ve şartlar dosyanın özelliklerine ve
            güncel mevzuata göre değişebilir. Hak kaybı yaşamamak için bir avukata danışmanız önerilir.</p>
          </div>"""


def breadcrumb_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": ad, "item": SITE + href}
        for i, (href, ad) in enumerate(items)]}


def faq_ld(sorular, sid):
    return {"@type": "FAQPage", "@id": SITE + sid, "inLanguage": "tr-TR", "mainEntity": [
        {"@type": "Question", "name": s, "acceptedAnswer": {"@type": "Answer", "text": c}}
        for s, c in sorular]}


def faq_html(sorular):
    out = []
    for s, c in sorular:
        out.append(f"""            <details>
              <summary>{s}</summary>
              <div class="accordion__panel">
                <p>{c}</p>
              </div>
            </details>""")
    return "\n".join(out)
