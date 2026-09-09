/* ==========================================================================
   form.js — İletişim formu: doğrulama + güvenlik katmanı
   --------------------------------------------------------------------------
   İSTEMCİ TARAFI önlemler (detay: docs/GUVENLIK-PLANI.md):
     1. Honeypot alanı        → basit botları eler
     2. Süre kontrolü         → 4 sn'den hızlı gönderimi reddeder
     3. Gönderim aralığı      → sessionStorage ile art arda spam'i frenler
     4. Alan doğrulama        → tip/uzunluk/biçim (regex) kontrolleri
     5. Girdi temizleme       → kontrol karakterleri ve fazla boşluk temizlenir
     6. Kaçırma (escape)      → ekrana yazarken innerHTML kullanılmaz
     7. KVKK açık rıza        → onay kutusu zorunlu
     8. AbortController       → 15 sn'de yanıt gelmezse istek iptal

   !!! KRİTİK: İstemci doğrulaması KULLANICI DENEYİMİ içindir, güvenlik
   sınırı DEĞİLDİR. Aynı kontroller sunucu tarafında tekrar yapılmalıdır.
   ========================================================================== */

(function () {
  "use strict";

  const form = document.getElementById("iletisimForm");
  if (!form) return;

  const site = window.SITE || {};
  const limit = site.formLimit || { minDoldurmaSaniye: 4, beklemeSaniye: 60, maxMesajKarakter: 2000 };
  const statusEl = document.getElementById("formStatus");
  const submitBtn = form.querySelector('[type="submit"]');
  const openedAt = Date.now();

  /* ---------------------------------------------------------
     Doğrulama kuralları
     --------------------------------------------------------- */
  const KURALLAR = {
    adSoyad: {
      test: (v) => v.length >= 3 && v.length <= 80 && /^[\p{L}\s.'-]+$/u.test(v),
      hata: "Lütfen adınızı ve soyadınızı yazın (en az 3 harf)."
    },
    eposta: {
      test: (v) => v.length <= 254 && /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/.test(v),
      hata: "Geçerli bir e-posta adresi girin. Örn: ad@ornek.com"
    },
    telefon: {
      // İsteğe bağlı alan; doluysa 10-15 rakam
      test: (v) => v === "" || /^[0-9]{10,15}$/.test(v.replace(/[\s()+.-]/g, "")),
      hata: "Telefonu 05XX XXX XX XX biçiminde girin."
    },
    konu: {
      test: (v) => v !== "",
      hata: "Lütfen bir hukuk alanı seçin."
    },
    avukat: {
      test: (v) => v !== "",
      hata: "Lütfen görüşmek istediğiniz avukatı seçin."
    },
    mesaj: {
      test: (v) => v.length >= 20 && v.length <= limit.maxMesajKarakter,
      hata: "Talebinizi en az 20 karakterle özetleyin (en fazla " + limit.maxMesajKarakter + ")."
    },
    kvkk: {
      test: (v, el) => el.checked,
      hata: "Devam edebilmek için aydınlatma metnini onaylamanız gerekir."
    }
  };

  /* ---------------------------------------------------------
     Girdi temizleme — görünmez kontrol karakterleri ve
     tekrar eden boşluklar kaldırılır.
     --------------------------------------------------------- */
  function temizle(deger) {
    const temizKarakter = (ch) => {
      const kod = ch.charCodeAt(0);
      if (ch === "\n") return true;                       // satır sonu korunur
      if (kod < 32 || kod === 127) return false;           // C0 kontrol karakterleri
      if (kod >= 0x200B && kod <= 0x200D) return false;    // sıfır genişlikli birleştiriciler
      if (kod === 0xFEFF) return false;                    // BOM
      return true;
    };
    return Array.from(String(deger))
      .filter(temizKarakter)
      .join("")
      .replace(/[ \t]{2,}/g, " ")
      .trim();
  }

  /* ---------------------------------------------------------
     Durum mesajı — daima textContent ile (XSS önlemi)
     --------------------------------------------------------- */
  function durum(tip, mesaj) {
    if (!statusEl) return;
    statusEl.className = "form-status is-visible form-status--" + tip;
    statusEl.textContent = mesaj;
    statusEl.setAttribute("role", tip === "err" ? "alert" : "status");
  }

  function alanHata(el, mesaj) {
    const field = el.closest(".field") || el.closest(".checkbox-wrap") || el.parentElement;
    const kutu = field ? field.querySelector(".field__error") : null;
    if (field) field.classList.toggle("has-error", Boolean(mesaj));
    if (kutu) kutu.textContent = mesaj || "";
    el.setAttribute("aria-invalid", mesaj ? "true" : "false");
  }

  function alanDogrula(el) {
    const kural = KURALLAR[el.name];
    if (!kural) return true;
    const deger = el.type === "checkbox" ? "" : temizle(el.value);
    const gecerli = kural.test(deger, el);
    alanHata(el, gecerli ? "" : kural.hata);
    return gecerli;
  }

  /* ---------------------------------------------------------
     Anlık geri bildirim: alandan çıkınca doğrula,
     yazarken hatayı temizle
     --------------------------------------------------------- */
  Object.keys(KURALLAR).forEach((ad) => {
    const el = form.elements[ad];
    if (!el) return;
    el.addEventListener("blur", () => alanDogrula(el));
    el.addEventListener("input", () => {
      const field = el.closest(".field");
      if (field && field.classList.contains("has-error")) alanDogrula(el);
    });
    if (el.type === "checkbox") el.addEventListener("change", () => alanDogrula(el));
  });

  // Mesaj karakter sayacı
  const mesajEl = form.elements.mesaj;
  const sayac = document.getElementById("mesajSayac");
  if (mesajEl && sayac) {
    mesajEl.setAttribute("maxlength", String(limit.maxMesajKarakter));
    const guncelle = () => {
      sayac.textContent = mesajEl.value.length + " / " + limit.maxMesajKarakter;
    };
    mesajEl.addEventListener("input", guncelle);
    guncelle();
  }

  /* ---------------------------------------------------------
     Gönderim
     --------------------------------------------------------- */
  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    // (1) Honeypot — insan bu alanı göremez, bot doldurur
    const tuzak = form.elements.website;
    if (tuzak && tuzak.value !== "") {
      durum("err", "Gönderim doğrulanamadı. Lütfen sayfayı yenileyip tekrar deneyin.");
      return;
    }

    // (2) Süre kontrolü
    const gecenSaniye = (Date.now() - openedAt) / 1000;
    if (gecenSaniye < limit.minDoldurmaSaniye) {
      durum("err", "Form beklenenden hızlı gönderildi. Lütfen birkaç saniye sonra tekrar deneyin.");
      return;
    }

    // (3) Art arda gönderim freni
    try {
      const sonGonderim = Number(sessionStorage.getItem("gelegen_form_ts") || 0);
      const fark = (Date.now() - sonGonderim) / 1000;
      if (sonGonderim && fark < limit.beklemeSaniye) {
        durum("err", "Az önce bir mesaj gönderdiniz. Lütfen " +
          Math.ceil(limit.beklemeSaniye - fark) + " saniye sonra tekrar deneyin.");
        return;
      }
    } catch (_) { /* sessionStorage kapalıysa sessizce geç */ }

    // (4) Alan doğrulama
    let ilkHataliAlan = null;
    let gecerli = true;
    Object.keys(KURALLAR).forEach((ad) => {
      const el = form.elements[ad];
      if (!el) return;
      if (!alanDogrula(el)) {
        gecerli = false;
        if (!ilkHataliAlan) ilkHataliAlan = el;
      }
    });

    if (!gecerli) {
      durum("err", "Lütfen işaretli alanları kontrol edin.");
      if (ilkHataliAlan) ilkHataliAlan.focus();
      return;
    }

    // (5) Temizlenmiş veriyi hazırla
    const veri = {
      adSoyad: temizle(form.elements.adSoyad.value),
      eposta: temizle(form.elements.eposta.value).toLowerCase(),
      telefon: temizle(form.elements.telefon.value),
      konu: temizle(form.elements.konu.value),
      avukat: temizle(form.elements.avukat.value),
      mesaj: temizle(form.elements.mesaj.value),
      kvkkOnay: true,
      gonderimZamani: new Date().toISOString()
    };

    // (6) Gönder — altyapı Netlify Forms'tur; API anahtarı veya
    //     ayrı bir sunucu adresi gerektirmez.
    const eskiMetin = submitBtn ? submitBtn.textContent : "";
    if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = "Gönderiliyor…"; }
    durum("info", "Mesajınız iletiliyor…");

    const controller = new AbortController();
    const zamanAsimi = setTimeout(() => controller.abort(), 15000);

    // İnsan-okunur konu ve gönderim zamanı
    const zaman = new Date().toLocaleString("tr-TR", { dateStyle: "long", timeStyle: "short" });
    const konuBasligi = "Yeni Randevu Talebi — " + veri.adSoyad + " (" + veri.konu + ")";

    /* --- Netlify Forms gönderimi -----------------------------------------
       Gönderim kendi alan adımıza (same-origin) yapılır; Netlify sunucu
       tarafında işler, panelde saklar ve e-posta bildirimi gönderir.
       Biçim: application/x-www-form-urlencoded + zorunlu "form-name" alanı.
       Açıkta duran API anahtarı YOKTUR → anahtar toplayan spam botları
       doğrudan API'ye istek atamaz. Ayrıca Netlify honeypot + Akismet süzer. */
    /* ÖNEMLİ: Anahtarlar iletisim.html'deki name="..." değerleriyle
       BİREBİR AYNI olmalıdır. Netlify formu HTML'den tanır; farklı bir ad
       gönderilirse o alan bildirim e-postasında BOŞ görünür.
       E-postadaki Türkçe başlıklar HTML'deki <label> metinlerinden gelir. */
    const alanlar = {
      "form-name": "randevu",
      adSoyad: veri.adSoyad,
      eposta:  veri.eposta,
      telefon: veri.telefon || "—",
      konu:    veri.konu,
      avukat:  veri.avukat,
      mesaj:   veri.mesaj,
      kvkk:    "Onaylandı — " + zaman
    };

    const govde = new URLSearchParams();
    Object.keys(alanlar).forEach(function (k) { govde.append(k, alanlar[k]); });

    try {
      const yanit = await fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: govde.toString(),
        signal: controller.signal,
        credentials: "omit",       // çerez gönderme → CSRF yüzeyini daraltır
        referrerPolicy: "strict-origin-when-cross-origin"
      });

      if (!yanit.ok) throw new Error("HTTP " + yanit.status);

      try { sessionStorage.setItem("gelegen_form_ts", String(Date.now())); } catch (_) {}
      form.reset();
      if (sayac) sayac.textContent = "0 / " + limit.maxMesajKarakter;
      durum("ok", "Talebiniz alındı. En kısa sürede size dönüş yapılacaktır. " +
                  "Acil durumlar için lütfen telefonla arayın.");
    } catch (hata) {
      const mesaj = hata && hata.name === "AbortError"
        ? "Bağlantı zaman aşımına uğradı."
        : "Talep gönderilemedi.";
      durum("err", mesaj + " Lütfen " + (site.telefonGosterim || "") +
                   " numarasından veya " + (site.eposta || "") + " adresinden ulaşın.");
    } finally {
      clearTimeout(zamanAsimi);
      if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = eskiMetin; }
    }
  });
})();
