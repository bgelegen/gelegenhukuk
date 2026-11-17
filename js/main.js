/* ==========================================================================
   main.js — Arayüz davranışları
   --------------------------------------------------------------------------
   Modüller:
     1) Mobil menü (çekmece)      5) Akordeon (SSS) tek-açık davranışı
     2) Sticky header gölgesi     6) Avukat profil modali
     3) Aktif menü bağlantısı     7) Yukarı çık butonu
     4) Kaydırma animasyonu       8) data.js bağlama (iletişim bilgileri)

   İlkeler:
     - Progressive enhancement: JS çalışmasa da site tam okunur kalır.
     - DOM'a metin yazarken innerHTML KULLANILMAZ (XSS önlemi) — textContent.
     - prefers-reduced-motion tercihine saygı gösterilir.
   ========================================================================== */

(function () {
  "use strict";

  const $ = (sel, ctx) => (ctx || document).querySelector(sel);
  const $$ = (sel, ctx) => Array.from((ctx || document).querySelectorAll(sel));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const site = window.SITE || {};

  /* =========================================================
     1) MOBİL MENÜ
     ========================================================= */
  function initNav() {
    const toggle = $(".nav-toggle");
    const nav = $("#site-nav");
    const backdrop = $(".nav-backdrop");
    if (!toggle || !nav) return;

    const setOpen = (open) => {
      toggle.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-open", open);
      if (backdrop) backdrop.classList.toggle("is-open", open);
      document.body.classList.toggle("is-locked", open);
      if (open) {
        const firstLink = $("a", nav);
        if (firstLink) firstLink.focus();
      }
    };

    toggle.addEventListener("click", () => {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });

    if (backdrop) backdrop.addEventListener("click", () => setOpen(false));

    // Menüden bir bağlantıya tıklanınca kapan
    $$("a", nav).forEach((a) => a.addEventListener("click", () => setOpen(false)));

    // ESC ile kapan
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });

    // Masaüstü genişliğine geçilince çekmeceyi sıfırla
    const mq = window.matchMedia("(min-width: 1024px)");
    const onChange = (e) => { if (e.matches) setOpen(false); };
    mq.addEventListener ? mq.addEventListener("change", onChange) : mq.addListener(onChange);
  }

  /* =========================================================
     2) STICKY HEADER — kaydırınca gölge
     ========================================================= */
  function initHeader() {
    const header = $(".site-header");
    if (!header) return;
    let ticking = false;
    const update = () => {
      header.classList.toggle("is-stuck", window.scrollY > 8);
      ticking = false;
    };
    window.addEventListener("scroll", () => {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* =========================================================
     3) AKTİF MENÜ BAĞLANTISI
     HTML'de aria-current elle verilmemişse dosya adına göre işaretle.
     ========================================================= */
  function initActiveLink() {
    const nav = $("#site-nav");
    if (!nav || $("a[aria-current='page']", nav)) return;
    let path = window.location.pathname.split("/").pop() || "index.html";
    $$("a", nav).forEach((a) => {
      const href = (a.getAttribute("href") || "").split("#")[0];
      if (href && href === path) a.setAttribute("aria-current", "page");
    });
  }

  /* =========================================================
     4) KAYDIRMA ANİMASYONU (IntersectionObserver)
     ========================================================= */
  function initReveal() {
    const items = $$(".reveal");
    if (!items.length) return;

    // Hareket azaltma tercihi, IO desteği yokluğu veya sekme arka plandaysa
    // (arka plan sekmelerinde IntersectionObserver tetiklenmeyebilir) doğrudan göster.
    if (reduceMotion || !("IntersectionObserver" in window) || document.visibilityState !== "visible") {
      items.forEach((el) => el.classList.add("is-visible"));
      return;
    }

    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        // Kartların sırayla belirmesi için küçük gecikme
        const delay = Number(entry.target.dataset.delay || 0);
        setTimeout(() => entry.target.classList.add("is-visible"), delay);
        io.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -60px 0px" });

    items.forEach((el) => io.observe(el));

    // Güvenlik ağı: ekranda hâlihazırda duran ögeleri gözlemciyi beklemeden göster.
    // (bfcache'ten dönüş, ilk boyama gecikmesi gibi durumlarda içeriğin
    //  görünmez kalmasını kesin olarak engeller.)
    const ilkGecis = () => {
      const h = window.innerHeight || document.documentElement.clientHeight;
      items.forEach((el) => {
        if (el.classList.contains("is-visible")) return;
        const r = el.getBoundingClientRect();
        if (r.top < h * 1.05 && r.bottom > 0) el.classList.add("is-visible");
      });
    };
    ilkGecis();
    window.addEventListener("load", ilkGecis);
    window.addEventListener("pageshow", ilkGecis);
  }

  /* =========================================================
     5) AKORDEON — aynı anda tek panel açık
     ========================================================= */
  function initAccordion() {
    const groups = $$(".accordion");
    groups.forEach((group) => {
      const items = $$("details", group);
      items.forEach((d) => {
        d.addEventListener("toggle", () => {
          if (!d.open) return;
          items.forEach((other) => { if (other !== d) other.open = false; });
        });
      });
    });
  }

  /* =========================================================
     6) AVUKAT PROFİL MODALİ
     ========================================================= */
  function initLawyerModal() {
    const modal = $("#lawyerModal");
    const triggers = $$("[data-lawyer]");
    if (!modal || !triggers.length || !Array.isArray(window.AVUKATLAR)) return;

    const dialog = $(".modal__dialog", modal);
    const body = $(".modal__body", modal);
    const titleEl = $("#lawyerModalTitle", modal);
    const closeBtn = $(".modal__close", modal);
    let lastFocused = null;

    // Yardımcı: güvenli liste oluşturma (innerHTML yok → XSS riski yok)
    const buildList = (baslik, dizi) => {
      if (!Array.isArray(dizi) || !dizi.length) return null;
      const frag = document.createDocumentFragment();
      const h = document.createElement("h4");
      h.textContent = baslik;
      const ul = document.createElement("ul");
      dizi.forEach((metin) => {
        const li = document.createElement("li");
        li.textContent = metin;
        ul.appendChild(li);
      });
      frag.appendChild(h);
      frag.appendChild(ul);
      return frag;
    };

    const open = (id, trigger) => {
      const av = window.AVUKATLAR.find((a) => a.id === id);
      if (!av) return;

      lastFocused = trigger;
      titleEl.textContent = "Av. " + av.ad;

      body.textContent = "";
      const unvan = document.createElement("p");
      unvan.className = "lawyer__role";
      unvan.textContent = av.unvan;
      body.appendChild(unvan);

      const ozet = document.createElement("p");
      ozet.textContent = av.ozet;
      body.appendChild(ozet);

      [
        buildList("Çalışma Alanları", av.alanlar),
        buildList("Öne Çıkan Dava ve İşlemler", av.deneyim),
        buildList("Eğitim", av.egitim),
        buildList("Baro Kaydı", av.barolar),
        buildList("Üyelikler", av.uyelikler)
      ].forEach((frag) => { if (frag) body.appendChild(frag); });

      modal.hidden = false;
      document.body.classList.add("is-locked");
      closeBtn.focus();
    };

    const close = () => {
      modal.hidden = true;
      document.body.classList.remove("is-locked");
      if (lastFocused) lastFocused.focus();
    };

    triggers.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        open(btn.dataset.lawyer, btn);
      });
    });

    closeBtn.addEventListener("click", close);
    $(".modal__backdrop", modal).addEventListener("click", close);

    modal.addEventListener("keydown", (e) => {
      if (e.key === "Escape") { close(); return; }
      if (e.key !== "Tab") return;

      // Basit odak tuzağı: odak modal içinde döner
      const focusables = $$(
        'a[href], button:not([disabled]), input, textarea, select, [tabindex]:not([tabindex="-1"])',
        dialog
      ).filter((el) => el.offsetParent !== null);
      if (!focusables.length) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }

  /* =========================================================
     7) YUKARI ÇIK
     ========================================================= */
  function initBackToTop() {
    const btn = $("#backToTop");
    if (!btn) return;
    let ticking = false;
    const update = () => {
      btn.classList.toggle("is-visible", window.scrollY > 600);
      ticking = false;
    };
    window.addEventListener("scroll", () => {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    btn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
    });
    update();
  }

  /* =========================================================
     8) data.js BAĞLAMA
     HTML'deki statik değerler (SEO/JS-siz erişim için) data.js ile
     senkronlanır. Böylece bilgi tek yerden güncellenir.
     Kullanım:  <a data-site="telefon">…</a>
     ========================================================= */
  function initDataBinding() {
    if (!site.firma) return;

    const adresTamMetin = site.adres
      ? [
          site.adres.satir1,
          site.adres.satir2,
          // posta kodu varsa başa ekle; yoksa baştaki boşluk oluşmasın
          ((site.adres.postaKodu ? site.adres.postaKodu + " " : "") + site.adres.ilce + " / " + site.adres.il)
        ].filter(Boolean).join(", ")
      : "";

    const map = {
      firma: { text: site.firma },
      telefon: { text: site.telefonGosterim, href: "tel:" + String(site.telefon).replace(/\s/g, "") },
      eposta: { text: site.eposta, href: "mailto:" + site.eposta },
      adres: { text: adresTamMetin, href: site.haritaLink },
      harita: { href: site.haritaLink }
    };

    $$("[data-site]").forEach((el) => {
      const conf = map[el.dataset.site];
      if (!conf) return;
      // Metni yalnızca elemanda "data-site-keep" yoksa değiştir
      if (conf.text && !el.hasAttribute("data-site-keep")) el.textContent = conf.text;
      if (conf.href && el.tagName === "A") el.setAttribute("href", conf.href);
    });

    // Footer yılı
    $$("[data-year]").forEach((el) => { el.textContent = String(new Date().getFullYear()); });

    // Sosyal medya bağlantıları — tanımsızsa gizle
    $$("[data-social]").forEach((el) => {
      const url = (site.sosyal || {})[el.dataset.social];
      if (url) { el.setAttribute("href", url); }
      else { el.hidden = true; }
    });
  }

  /* =========================================================
     9) HARİTA YOL TARİFİ — uygulama seçimi (Google / Apple)
     Harita HTML'de gömülü (hep görünür). Haritaya tıklanınca
     hangi uygulamada yol tarifi açılacağı sorulur.
     ========================================================= */
  function initMap() {
    const tetik = $("[data-map-directions]");
    const secim = $("#mapChoice");
    if (!tetik || !secim) return;

    const googleBtn = $("#mapChoiceGoogle", secim);
    const appleBtn = $("#mapChoiceApple", secim);
    // data.js'ten yol tarifi adreslerini yerleştir
    if (googleBtn && site.haritaLink) googleBtn.href = site.haritaLink;
    if (appleBtn && site.haritaAppleLink) appleBtn.href = site.haritaAppleLink;

    const ac = () => {
      secim.hidden = false;
      document.body.classList.add("is-locked");
      if (googleBtn) googleBtn.focus();
    };
    const kapat = () => {
      secim.hidden = true;
      document.body.classList.remove("is-locked");
    };

    // Haritaya (tıklama katmanına) tıklanınca seçim penceresini aç
    tetik.addEventListener("click", (e) => {
      e.preventDefault();
      ac();
    });

    // Bir uygulama seçilince pencereyi kapat (bağlantı yeni sekmede açılır)
    [googleBtn, appleBtn].forEach((b) => b && b.addEventListener("click", () => setTimeout(kapat, 60)));

    // Kapatma: arka plan, çarpı, ESC
    $$("[data-map-close]", secim).forEach((el) => el.addEventListener("click", kapat));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !secim.hidden) kapat();
    });
  }

  /* =========================================================
     10) MAKALE SAYFASI — okuma ilerleme çubuğu + içindekiler
         Yalnızca .article-layout bulunan sayfalarda çalışır.
     ========================================================= */
  function initArticle() {
    const body = $(".article-layout .article-body");
    const header = $(".site-header");
    if (!body) return;

    // İlerleme çubuğu: kaydırmayla doğrudan eşlenir (animasyon değil)
    if (header) {
      const bar = document.createElement("div");
      bar.className = "read-progress";
      bar.setAttribute("aria-hidden", "true");
      header.appendChild(bar);
      let ticking = false;
      const update = () => {
        const r = body.getBoundingClientRect();
        const total = r.height - window.innerHeight * 0.6;
        const done = Math.min(1, Math.max(0, -r.top / (total > 0 ? total : 1)));
        bar.style.transform = "scaleX(" + done.toFixed(4) + ")";
        ticking = false;
      };
      window.addEventListener("scroll", () => {
        if (!ticking) { ticking = true; requestAnimationFrame(update); }
      }, { passive: true });
      window.addEventListener("resize", update);
      update();
    }

    // İçindekiler: okunan bölümü işaretle (ekranın üst %30'unu geçen son başlık);
    // mobilde bağlantıya basınca kutuyu kapat
    const links = $$(".toc__list a");
    const heads = $$(".article-body h2[id]");
    if (links.length && heads.length) {
      let current = "";
      const mark = () => {
        const line = window.innerHeight * 0.3;
        let id = "";
        heads.forEach((h) => { if (h.getBoundingClientRect().top <= line) id = h.id; });
        if (id === current) return;
        current = id;
        links.forEach((a) => {
          if (a.getAttribute("href") === "#" + id) a.setAttribute("aria-current", "true");
          else a.removeAttribute("aria-current");
        });
      };
      window.addEventListener("scroll", () => requestAnimationFrame(mark), { passive: true });
      mark();
    }
    $$(".toc-mobile a").forEach((a) => a.addEventListener("click", () => {
      const d = a.closest("details");
      if (d) d.open = false;
    }));
  }

  /* =========================================================
     11) YAZI ŞERİDİ — "Diğer yazılarımız"
         Kaydırma tarayıcının kendisine ait (parmak, tekerlek, klavye);
         oklar bir kart ilerletir, uçlarda pasifleşir; alttaki çizgi konumu
         gösterir. Hepsi sığıyorsa oklar ve çizgi gizlenir.
     ========================================================= */
  function initCarousel() {
    $$(".related-posts").forEach((sec) => {
      const track = $(".carousel__track", sec);
      const nav = $(".carousel-nav", sec);
      const bar = $(".carousel-progress", sec);
      if (!track) return;
      const prev = $('[data-dir="-1"]', sec);
      const next = $('[data-dir="1"]', sec);
      const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

      const step = () => {
        const card = track.firstElementChild;
        if (!card) return track.clientWidth;
        const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
        return card.getBoundingClientRect().width + gap;
      };

      const update = () => {
        const max = track.scrollWidth - track.clientWidth;
        const scrollable = max > 2;
        if (nav) nav.hidden = !scrollable;
        if (bar) bar.hidden = !scrollable;
        if (!scrollable) return;
        const x = track.scrollLeft;
        if (prev) prev.disabled = x <= 2;
        if (next) next.disabled = x >= max - 2;
        if (bar) {
          const w = track.clientWidth / track.scrollWidth;
          bar.style.setProperty("--w", (w * 100).toFixed(2) + "%");
          bar.style.setProperty("--x", ((x / max) * (1 - w) * 100).toFixed(2) + "%");
        }
      };

      [prev, next].forEach((btn) => btn && btn.addEventListener("click", () => {
        const dir = Number(btn.dataset.dir) || 1;
        track.scrollBy({ left: dir * step(), behavior: reduce ? "auto" : "smooth" });
      }));
      // Şeride odaklanınca sol/sağ ok tuşları da bir kart ilerletsin
      const region = track.parentElement;
      if (region) region.addEventListener("keydown", (e) => {
        if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
        e.preventDefault();
        track.scrollBy({ left: (e.key === "ArrowRight" ? 1 : -1) * step(), behavior: reduce ? "auto" : "smooth" });
      });

      let raf = 0;
      track.addEventListener("scroll", () => {
        cancelAnimationFrame(raf);
        raf = requestAnimationFrame(update);
      }, { passive: true });
      window.addEventListener("resize", update);
      update();
    });
  }

  /* =========================================================
     BAŞLAT
     ========================================================= */
  function init() {
    initNav();
    initHeader();
    initActiveLink();
    initReveal();
    initAccordion();
    initLawyerModal();
    initBackToTop();
    initDataBinding();
    initMap();
    initArticle();
    initCarousel();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
