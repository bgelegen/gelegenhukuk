# Responsive (Mobil Uyum) Planı

**Proje:** Gelegen Hukuk Bürosu · **Yaklaşım:** Mobile First · **Uygulandığı dosya:** `css/responsive.css`

> Ziyaretçilerin önemli bir kısmı siteye telefondan, çoğu zaman acil bir hukuki
> sorunla girer. Bu nedenle mobil düzen "küçültülmüş masaüstü" değil, **birincil
> tasarım** olarak kurgulanmıştır.

---

## 1. Temel strateji

| İlke | Uygulama |
|---|---|
| Mobile first | `css/style.css` mobil düzeni tanımlar; büyük ekran kuralları yalnızca `min-width` sorgularıyla eklenir. Böylece telefonlar gereksiz CSS'i işlemez. |
| Akışkan tipografi | Font boyutları sabit `px` değil `clamp()` ile tanımlıdır (`--fs-h1: clamp(2rem, 1.5rem + 2.6vw, 3.6rem)`). Breakpoint olmadan da yumuşak ölçeklenir. |
| Akışkan boşluk | Bölüm boşlukları `--section-y: clamp(3.5rem, 2.5rem + 4vw, 7rem)`, kenar boşlukları `--gutter: clamp(1.15rem, 0.8rem + 1.6vw, 2.5rem)`. |
| Esnek grid | Kart alanları `repeat(auto-fit, minmax(min(100%, 260px), 1fr))` ile kendiliğinden sarar; breakpoint gerekmez. |
| İçerik önceliği | Mobilde önce başlık → özet → eylem butonu; dekoratif görseller (hero amblemi) küçük ekranda alta iner. |

---

## 2. Kırılım noktaları (breakpoints)

| Ad | Genişlik | Hedef cihaz | Bu noktada değişen |
|---|---|---|---|
| **xs** | `< 480px` | Küçük telefon | Tek sütun, tam genişlik butonlar, çekmece menü |
| **sm** | `≥ 480px` | Büyük telefon | Form alanları 2 sütun, butonlar min. 190px, footer alt bilgi yan yana |
| **md** | `≥ 768px` | Tablet / dikey iPad | `.grid--2/3/4` → 2 sütun, `.split` → metin+görsel yan yana, süreç adımları 2×2, footer 2 sütun |
| **lg** | `≥ 1024px` | Dizüstü | **Hamburger kapanır, yatay menü açılır**, grid 3–4 sütun, iletişim sayfası 2 sütun (form + bilgi), footer 4 sütun |
| **xl** | `≥ 1280px` | Masaüstü | Hero 2 sütuna ayrılır (metin + amblem kartı) |
| **2xl** | `≥ 1536px` | Geniş ekran | Konteyner 1200px → 1320px, bölüm boşluğu 8rem |

**Neden 1024px'te menü değişiyor?** 768–1023px arası tabletlerde yatay menü + logo + CTA
yan yana sıkışıyor. Çekmece menüyü tablette de korumak, dokunmatik hedefleri büyük tutar.

---

## 3. Navigasyon davranışı

| Ekran | Davranış |
|---|---|
| `< 1024px` | Sağdan açılan çekmece (`transform: translateX(100%)` → `0`), yarı saydam arka plan, `body.is-locked` ile arka plan kaydırması kilitlenir. ESC ile ve bağlantıya tıklayınca kapanır. |
| `≥ 1024px` | Yatay menü; aktif/hover bağlantıda altın alt çizgi animasyonu (`transform: scaleX()`), `aria-current="page"` ile aktif sayfa işaretlenir. |
| Geçiş anı | `matchMedia("(min-width: 1024px)")` dinlenir; masaüstüne geçildiğinde açık kalan çekmece otomatik sıfırlanır. |

---

## 4. Dokunmatik ve girdi türü uyumu

- **Dokunma hedefi:** Tüm butonlar ve form alanları en az **48px** yüksekliğinde (`--btn min-height: 48px`). WCAG 2.5.5 hedef boyutu karşılanır.
- **iOS zoom önleme:** Form girdilerinde `font-size: 16px` sabittir; daha küçük değerde Safari odaklanınca sayfayı otomatik büyütür.
- `@media (hover: none)` → dokunmatik cihazlarda hover ile beliren efektler kapatılır, kart vurgusu kalıcı gösterilir.
- `@media (pointer: fine)` → fare kullanılan cihazlarda buton yüksekliği 46px'e iner (daha kompakt görünüm).
- Telefon/e-posta/WhatsApp bağlantıları `tel:`, `mailto:`, `wa.me` protokolleriyle mobilde tek dokunuşla çalışır.

---

## 5. Görsel ve medya uyumu

- Tüm görsellerde `max-width: 100%; height: auto`.
- `width`/`height` nitelikleri HTML'de verilir → **CLS (layout shift) engellenir**, Core Web Vitals korunur.
- Avukat fotoğrafları `aspect-ratio: 4/5` kutuda `object-fit: cover` ile kırpılır; farklı boyutta fotoğraf yüklense de düzen bozulmaz.
- Görseller SVG'dir (çözünürlükten bağımsız, retina ekranlarda net). Gerçek fotoğraflara geçilince `loading="lazy"` + `srcset` önerilir (bkz. README).
- Dekoratif SVG'lerde `aria-hidden="true"`; anlam taşıyanlarda `role="img"` + `<title>`.

---

## 6. Yatay mod ve küçük yükseklik

`@media (max-height: 520px) and (orientation: landscape)`
→ Hero dikey boşluğu kısaltılır, çekmece menüde bağlantı aralıkları daraltılır.
Yatay tutulan telefonlarda menünün taşmasını engeller.

---

## 7. Erişilebilirlik uyumları

| Tercih | Uygulama |
|---|---|
| `prefers-reduced-motion: reduce` | Tüm animasyon/geçişler ~0'a indirilir, `scroll-behavior: auto`, kaydırma animasyonları devre dışı. |
| `prefers-contrast: more` | Metin ve çizgi renkleri koyulaştırılır, birincil buton kontrastı artırılır. |
| Klavye | "İçeriğe atla" bağlantısı, `:focus-visible` ile 3px altın odak halkası, modalde odak tuzağı. |
| Ekran okuyucu | `aria-expanded`, `aria-current`, `aria-live` (form hataları), `.sr-only` başlıklar. |

---

## 8. Konteyner sorguları (bileşen bazlı uyum)

`@supports (container-type: inline-size)` bloğunda kartlar, **içinde bulundukları
kolonun** genişliğine göre iç boşluklarını ayarlar. Böylece aynı kart bileşeni
2 sütunlu ve 4 sütunlu ızgarada da doğru görünür — ekran genişliğine bağlı kalmaz.

---

## 9. Test kontrol listesi

- [ ] 320px (iPhone SE) — yatay kaydırma çubuğu **oluşmamalı**
- [ ] 375 / 390 / 414px — hero başlığı 3 satırı geçmemeli, butonlar taşmamalı
- [ ] 768px — split bölümler yan yana, menü hâlâ çekmece
- [ ] 1024px — menü yatay, iletişim sayfası 2 sütun
- [ ] 1440 / 1920px — konteyner ortalanmalı, satır uzunluğu 75 karakteri geçmemeli
- [ ] Yatay mod (812×375) — menü ekrana sığmalı
- [ ] Tarayıcı yazı tipi boyutu %200 — düzen kırılmamalı (`rem` tabanlı ölçek)
- [ ] Chrome DevTools > Lighthouse > Mobile: Performance ve Accessibility ≥ 90

**Hızlı test komutu** (yerel sunucu):

```bash
npx serve "C:/Users/batuh/OneDrive/Desktop/Web"
```
