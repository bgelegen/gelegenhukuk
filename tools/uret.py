# -*- coding: utf-8 -*-
"""
Makaleler ve çalışma alanı sayfalarını üretir.

    python3 tools/uret.py          (proje kökünden çalıştırın)

Üretilen dosyalar: makaleler.html, calisma-alanlari.html, her makale ve her
çalışma alanı sayfası. Ardından:
  1) node tools/csp-hash.js  → _headers'taki script-src satırını güncelleyin
  2) sitemap.xml'e yeni adresleri ekleyin
  3) yayin/ klasörüne kopyalayın
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sablon import (SITE, head, foot, hero, cta, UYARI, breadcrumb_ld, faq_ld, faq_html)
from icerik_alanlar import ALANLAR
from icerik_makaleler import MAKALELER

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
         "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
KURULUS = {"@id": SITE + "#kurulus"}


TR = str.maketrans("çğıöşüÇĞİÖŞÜâîû", "cgiosuCGIOSUaiu")


def basliklara_kimlik(body):
    """Gövdedeki <h2> başlıklarına bağlantı kimliği ekler, (kimlik, metin) listesi döndürür."""
    import re
    liste, kullanilan = [], set()

    def degistir(mt):
        metin = re.sub(r"<[^>]+>", "", mt.group(1)).strip()
        k = re.sub(r"[^a-z0-9]+", "-", metin.translate(TR).lower()).strip("-")[:60] or "bolum"
        base, n = k, 2
        while k in kullanilan:
            k, n = f"{base}-{n}", n + 1
        kullanilan.add(k)
        liste.append((k, metin))
        return f'<h2 id="{k}">{mt.group(1)}</h2>'

    body = re.sub(r"<h2>(.*?)</h2>", degistir, body)
    return etiketle(body), liste


def etiketle(body):
    """<li> veya <p> doğrudan <strong> ile başlıyorsa o <strong> bir satır başı etiketidir."""
    import re
    return re.sub(r"(<(?:li|p)>\s*)<strong>", r'\1<strong class="lbl">', body)


def tarih_tr(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {AYLAR[int(m) - 1]} {y}"


def yaz(ad, html):
    with open(os.path.join(KOK, ad), "w", encoding="utf-8") as f:
        f.write(html)
    print("  yazıldı:", ad)


def alan_by_kat(kat):
    return next((a for a in ALANLAR if a["kategori"] == kat), None)


def post_card(m, more="Yazıyı oku", reveal=True):
    sinif = "card post-card reveal" if reveal else "card post-card"
    return f"""          <article class="{sinif}">
            <p class="post-card__cat">{m["cat"]}</p>
            <h3><a href="{m["slug"]}">{m["h1"]}</a></h3>
            <p>{m["lead"]}</p>
            <span class="post-card__more" aria-hidden="true">{more} →</span>
          </article>
"""


# ============================================================ ŞERİT (kaydırmalı kart listesi)
def serit_nav(rid, ad):
    """Şeridin sağ üstündeki ok düğmeleri. JS, şerit sığıyorsa gizler."""
    return f"""<div class="carousel-nav" hidden>
            <button class="carousel-btn" type="button" data-dir="-1" aria-label="Önceki: {ad}" aria-controls="{rid}">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>
            </button>
            <button class="carousel-btn" type="button" data-dir="1" aria-label="Sonraki: {ad}" aria-controls="{rid}">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>
            </button>
          </div>"""


def serit(rid, ad, yazilar):
    """Masaüstünde 3, tablette 2, telefonda 1 kart görünen kaydırmalı şerit + konum çizgisi."""
    kartlar = "".join(post_card(x, reveal=False) for x in yazilar)
    return f"""        <div class="carousel" id="{rid}" role="region" aria-label="{ad}" tabindex="0">
          <div class="carousel__track">
{kartlar}          </div>
        </div>
        <div class="carousel-progress" aria-hidden="true"><span></span></div>"""


# ============================================================ ÇALIŞMA ALANI
def alan_sayfasi(a):
    yazilar = [m for m in MAKALELER if m["cat"] == a["kategori"]]
    ld = {"@context": "https://schema.org", "@graph": [
        breadcrumb_ld([("", "Anasayfa"), ("calisma-alanlari.html", "Çalışma Alanları"),
                       (a["slug"], a["kisa"])]),
        {"@type": "Service", "@id": SITE + a["slug"] + "#hizmet",
         "name": a["h1"], "serviceType": a["kisa"], "description": a["desc"],
         "url": SITE + a["slug"], "provider": KURULUS, "inLanguage": "tr-TR",
         "areaServed": [{"@type": "City", "name": "Malatya"},
                        {"@type": "AdministrativeArea", "name": "Battalgazi"},
                        {"@type": "AdministrativeArea", "name": "Yeşilyurt"}]},
        faq_ld(a["sss"], a["slug"] + "#sss"),
    ]}
    ilgili = ""
    if yazilar:
        lis = "\n".join(f'            <li><a href="{m["slug"]}">{m["h1"]}</a></li>' for m in yazilar)
        ilgili = f"""
          <h2>Bu konudaki bilgilendirici yazılarımız</h2>
          <ul>
{lis}
          </ul>
"""
    html = head(a["title"], a["desc"], a["slug"], ld, ogtitle=a["h1"] + " | Gelegen Hukuk Bürosu")
    html += hero(a["h1"], [("index.html", "Anasayfa"), ("calisma-alanlari.html", "Çalışma Alanları"),
                           (None, a["kisa"])])
    html += f"""
    <section class="section">
      <div class="container container--narrow">
        <article class="article-body">
          <p class="article-lead">{a["lead"]}</p>
{etiketle(a["body"])}{ilgili}
          <div class="article-note">
            <p>Bu sayfadaki bilgiler genel nitelikte olup hukuki görüş yerine geçmez. Her dosyanın
            koşulları farklıdır; somut durumunuz için ön görüşmede değerlendirme yapılır.</p>
          </div>
        </article>
      </div>
    </section>

    <section class="section section--sand" aria-labelledby="sss-baslik">
      <div class="container container--narrow">
        <div class="section-head reveal">
          <p class="eyebrow">Sık Sorulan Sorular</p>
          <h2 id="sss-baslik">{a["kisa"]} hakkında merak edilenler</h2>
        </div>
        <div class="accordion reveal">
{faq_html(a["sss"])}
        </div>
      </div>
    </section>
"""
    html += cta(metin=f"{a['kisa']} alanındaki sorularınız için büromuzla iletişime geçebilir, randevu talep edebilirsiniz.")
    html += foot()
    yaz(a["slug"], html)


def merkez_sayfa():
    slug = "calisma-alanlari.html"
    ld = {"@context": "https://schema.org", "@graph": [
        breadcrumb_ld([("", "Anasayfa"), (slug, "Çalışma Alanları")]),
        {"@type": "CollectionPage", "name": "Çalışma Alanları", "url": SITE + slug,
         "inLanguage": "tr-TR", "isPartOf": {"@id": SITE + "#website"}, "about": KURULUS,
         "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "name": a["kisa"], "url": SITE + a["slug"]}
             for i, a in enumerate(ALANLAR)]}},
    ]}
    kartlar = "".join(f"""          <article class="card post-card reveal">
            <p class="post-card__cat">Malatya</p>
            <h3><a href="{a["slug"]}">{a["kisa"]}</a></h3>
            <p>{a["kart"]}</p>
            <span class="post-card__more" aria-hidden="true">Ayrıntılar →</span>
          </article>
""" for a in ALANLAR)
    html = head("Çalışma Alanları | Malatya Avukat | Gelegen Hukuk Bürosu",
                "Gelegen Hukuk Bürosu'nun Malatya'da hizmet verdiği hukuk alanları: aile ve boşanma, ceza, iş, icra, gayrimenkul, miras, ticaret, idare ve vergi hukuku.",
                slug, ld, ogtitle="Çalışma Alanları | Gelegen Hukuk Bürosu")
    html += hero("Çalışma Alanları", [("index.html", "Anasayfa"), (None, "Çalışma Alanları")],
                 "Malatya merkezli büromuz, aşağıdaki alanlarda dava ve takip işlerini yürütmekte ve "
                 "önleyici hukuki danışmanlık sağlamaktadır. Ayrıntılı bilgi için ilgili alanı seçin.")
    html += f"""
    <section class="section">
      <div class="container">
        <div class="grid grid--auto">
{kartlar}        </div>
      </div>
    </section>
"""
    html += cta() + foot()
    yaz(slug, html)


# ============================================================ MAKALE
def makale_sayfasi(m):
    alan = alan_by_kat(m["cat"])
    ld = {"@context": "https://schema.org", "@graph": [
        breadcrumb_ld([("", "Anasayfa"), ("makaleler.html", "Makaleler"), (m["slug"], m["h1"])]),
        {"@type": "Article", "headline": m["h1"], "description": m["desc"], "inLanguage": "tr-TR",
         "articleSection": m["cat"], "datePublished": m["tarih"], "dateModified": m["tarih"],
         "mainEntityOfPage": {"@type": "WebPage", "@id": SITE + m["slug"]},
         "image": SITE + "assets/img/og-image.jpg",
         "author": {"@type": "Organization", "name": "Gelegen Hukuk Bürosu", "url": SITE},
         "publisher": KURULUS},
    ]}
    # Aynı alandaki diğer yazıların HEPSİ (şeritte 3'er görünür, kalanı kaydırılır).
    # Alanda 3'ten az yazı varsa diğer alanlardan 3'e tamamlanır.
    digerleri = [x for x in MAKALELER if x["cat"] == m["cat"] and x is not m]
    ayni_alan = len(digerleri)
    if len(digerleri) < 3:
        digerleri += [x for x in MAKALELER if x["cat"] != m["cat"]][:3 - len(digerleri)]
    body, basliklar = basliklara_kimlik(m["body"])
    toc = "\n".join(f'              <li><a href="#{k}">{t}</a></li>' for k, t in basliklar)
    alan_kart = ""
    if alan:
        alan_kart = f"""<p>İlgili çalışma alanı</p>
              <a href="{alan["slug"]}">{alan["h1"]}</a>"""
    kat_html = f'<a href="{alan["slug"]}">{m["cat"]}</a>' if alan else m["cat"]
    html = head(m["title"], m["desc"], m["slug"], ld, ogtype="article",
                ogtitle=m["h1"] + " | Gelegen Hukuk Bürosu")
    html += f"""
    <section class="page-hero article-hero">
      <div class="container page-hero__inner">
        <nav class="breadcrumb" aria-label="Sayfa yolu">
          <ol>
            <li><a href="index.html">Anasayfa</a></li>
            <li><a href="makaleler.html">Makaleler</a></li>
            <li aria-current="page">{m["cat"]}</li>
          </ol>
        </nav>
        <h1>{m["h1"]}</h1>
        <p class="article-hero__lead">{m["lead"]}</p>
        <ul class="article-hero__meta">
          <li>{kat_html}</li>
          <li><time datetime="{m["tarih"]}">{tarih_tr(m["tarih"])}</time></li>
          <li>{m["read"]}</li>
        </ul>
      </div>
    </section>

    <section class="article-section">
      <div class="container article-layout">
        <aside class="article-aside" aria-label="Yazı içi gezinme">
          <div class="article-aside__sticky">
            <nav class="toc" aria-label="İçindekiler">
              <p class="toc__title">Bu yazıda</p>
              <ol class="toc__list">
{toc}
              </ol>
            </nav>
            {'<div class="article-related">' + alan_kart + '</div>' if alan else ''}
          </div>
        </aside>

        <article class="article-body">
          <details class="toc-mobile">
            <summary>Bu yazıda</summary>
            <ol class="toc__list">
{toc}
            </ol>
          </details>
{body}
          <div class="article-disclaimer">
            <p>Bu yazı yalnızca genel bilgilendirme amaçlıdır; somut olayınıza ilişkin hukuki görüş yerine
            geçmez. Süreler ve şartlar dosyanın özelliklerine ve güncel mevzuata göre değişebilir. Hak kaybı
            yaşamamak için bir avukata danışmanız önerilir. Son güncelleme: {tarih_tr(m["tarih"])}.</p>
          </div>
          {'<div class="article-related article-related--mobile">' + alan_kart + '</div>' if alan else ''}
        </article>
      </div>
    </section>

    <section class="section section--sand related-posts" data-carousel aria-labelledby="diger-baslik">
      <div class="container">
        <div class="related-posts__head">
          <div class="section-head">
            <p class="eyebrow">{m["cat"] if ayni_alan else "Makaleler"}</p>
            <h2 id="diger-baslik">Diğer yazılarımız</h2>
          </div>
          {serit_nav("diger-yazilar", "yazılar")}
        </div>
{serit("diger-yazilar", "Diğer yazılarımız", digerleri)}
      </div>
    </section>
"""
    html += cta() + foot()
    yaz(m["slug"], html)


def makaleler_listesi():
    slug = "makaleler.html"
    ld = {"@context": "https://schema.org", "@graph": [
        breadcrumb_ld([("", "Anasayfa"), (slug, "Makaleler")]),
        {"@type": "CollectionPage", "name": "Makaleler", "inLanguage": "tr-TR",
         "description": "Gelegen Hukuk Bürosu bilgilendirici hukuk yazıları.",
         "url": SITE + slug, "isPartOf": {"@id": SITE + "#website"},
         "hasPart": [{"@type": "Article", "headline": m["h1"], "url": SITE + m["slug"]} for m in MAKALELER]},
    ]}
    # Kategori sırası: çalışma alanları sırası
    sira = [a["kategori"] for a in ALANLAR]
    kategoriler = sorted({m["cat"] for m in MAKALELER}, key=lambda c: sira.index(c) if c in sira else 99)
    bolumler = ""
    for i, kat in enumerate(kategoriler):
        yazilar = [m for m in MAKALELER if m["cat"] == kat]
        alan = alan_by_kat(kat)
        alan_link = (f'\n          <p><a href="{alan["slug"]}">{alan["h1"]} sayfasına git →</a></p>'
                     if alan else "")
        kid = "kat-" + str(i + 1)
        sinif = "section section--sand" if i % 2 else "section"
        if len(yazilar) > 3:
            # 3'ten fazla yazı: ilk 3 görünür, kalanı kaydırılarak gelir ("Diğer yazılarımız" ile aynı şerit)
            bolumler += f"""
    <section class="{sinif} related-posts" data-carousel aria-labelledby="{kid}">
      <div class="container">
        <div class="related-posts__head">
          <div class="section-head">
            <p class="eyebrow">{len(yazilar)} yazı</p>
            <h2 id="{kid}">{kat}</h2>{alan_link}
          </div>
          {serit_nav(kid + "-serit", kat + " yazıları")}
        </div>
{serit(kid + "-serit", kat + " yazıları", yazilar)}
      </div>
    </section>
"""
        else:
            bolumler += f"""
    <section class="{sinif}" aria-labelledby="{kid}">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{len(yazilar)} yazı</p>
          <h2 id="{kid}">{kat}</h2>{alan_link}
        </div>
        <div class="grid grid--auto">
{"".join(post_card(m) for m in yazilar)}        </div>
      </div>
    </section>
"""
    html = head("Makaleler | Malatya Gelegen Hukuk Bürosu",
                "Boşanma, nafaka, velayet, kıdem tazminatı, işe iade, icra takibine itiraz, ortaklığın giderilmesi, kira, miras ve ceza hukuku üzerine bilgilendirici yazılar.",
                slug, ld, ogtitle="Makaleler | Gelegen Hukuk Bürosu", aktif=slug)
    html += hero("Makaleler", [("index.html", "Anasayfa"), (None, "Makaleler")],
                 "Sık karşılaşılan hukuki soruları, güncel mevzuat çerçevesinde ve yalnızca bilgilendirme "
                 "amacıyla ele alıyoruz. Yazılar hukuki danışmanlık yerine geçmez.")
    html += bolumler + cta() + foot()
    yaz(slug, html)


if __name__ == "__main__":
    print("Çalışma alanları:")
    for a in ALANLAR:
        alan_sayfasi(a)
    merkez_sayfa()
    print("Makaleler:")
    for m in MAKALELER:
        makale_sayfasi(m)
    makaleler_listesi()
    print(f"TAMAM — {len(ALANLAR) + 1} alan sayfası, {len(MAKALELER) + 1} makale sayfası")
