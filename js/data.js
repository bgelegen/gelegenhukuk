/* ==========================================================================
   data.js — SİTE İÇERİK YAPILANDIRMASI
   --------------------------------------------------------------------------
   Sitenin değişken bilgileri (telefon, e-posta, adres, avukat profilleri)
   TEK YERDEN buradan yönetilir. Diğer JS dosyaları bu verileri okur.

   ÖNEMLİ (SEO): Sayfaların ana metinleri bilerek HTML içinde statik tutulmuştur.
   Arama motorları ve JavaScript kapalı tarayıcılar içeriği eksiksiz görsün diye.
   Bu dosya yalnızca (1) tekrar eden iletişim bilgilerini ve (2) profil
   modalindeki detay metinlerini besler.

   >>> DEĞİŞTİRİLECEK ALANLAR "TODO" ile işaretlendi. Yayına almadan önce
       gerçek bilgilerle güncelleyin ve HTML'deki karşılıklarını da düzeltin
       (index.html/iletisim.html footer + JSON-LD blokları).
   ========================================================================== */

(function () {
  "use strict";

  /* ---------------------------------------------------------------
     1) BÜRO / İLETİŞİM BİLGİLERİ
     --------------------------------------------------------------- */
  const SITE = {
    firma: "Gelegen Hukuk Bürosu",

    // TODO: Gerçek numara ile değiştirin. Format: uluslararası (tel: linki için)
    telefon: "+90 551 821 44 44",
    telefonGosterim: "+90 (551) 821 44 44",

    // TODO: Kurumsal e-posta adresi
    eposta: "gelegenhukuk@gmail.com",

    // Büro adresi
    adres: {
      satir1: "Saray Mahallesi, Şehit Fahri Koçyiğit Sokak",
      satir2: "Koçyiğit İş Merkezi No: 9, Kat: 2, Daire: 3",
      ilce: "Battalgazi",
      il: "Malatya",
      postaKodu: "",              // biliniyorsa ekleyin (Battalgazi merkez 44xxx)
      ulke: "Türkiye"
    },

    // Google Haritalar bağlantıları (API anahtarı GEREKTİRMEZ — bkz. GUVENLIK-PLANI.md)
    // Koordinat: büronun tam konumu (Koçyiğit İş Merkezi, Battalgazi/Malatya)
    // haritaLink: GOOGLE Haritalar yol tarifi (hedef = büro konumu)
    haritaLink: "https://www.google.com/maps/dir/?api=1&destination=38.34831614441364,38.32041685988208",
    // haritaAppleLink: APPLE Haritalar yol tarifi (aynı hedef)
    haritaAppleLink: "https://maps.apple.com/?daddr=38.34831614441364,38.32041685988208&dirflg=d",

    // Sosyal medya — kullanılmayanları boş bırakın, arayüzde gizlenir
    sosyal: {
      linkedin: "",
      x: "",
      instagram: ""
    },

    /* Form altyapısı: NETLIFY FORMS.
       Gönderimler sitenin kendi alan adına yapılır; Netlify sunucu tarafında
       işler, panelde saklar ve e-posta bildirimi gönderir. Bu yüzden burada
       API anahtarı veya sunucu adresi tutulmaz. */

    // Form gönderim sınırları (istemci tarafı kötüye kullanım freni)
    formLimit: {
      minDoldurmaSaniye: 4,     // 4 sn'den hızlı gönderim = bot şüphesi
      beklemeSaniye: 60,        // aynı ziyaretçi için art arda gönderim aralığı
      maxMesajKarakter: 2000
    }
  };

  /* ---------------------------------------------------------------
     2) AVUKAT PROFİLLERİ
     "Detaylı Profil" modalinde gösterilir.
     TODO: Özgeçmiş bilgilerini gerçek verilerle güncelleyin.
     NOT: TBB Reklam Yasağı Yönetmeliği gereği başarı oranı, kazanılmış
     dava sayısı, müvekkil yorumu ve iddialı nitelemeler EKLENMEMELİDİR.
     --------------------------------------------------------------- */
  const AVUKATLAR = [
    {
      id: "mustafa-gelegen",
      ad: "Mustafa Gelegen",
      unvan: "Avukat / Kurucu Ortak",
      foto: "assets/img/Mustafa_Gelegen.webp",
      ozet:
        "Aile, ceza, iş ve sosyal güvenlik, ticaret ve şirketler, icra ve iflas, gayrimenkul, " +
        "miras ile idare ve vergi hukuku alanlarında dava takibi ve danışmanlık hizmeti vermektedir.",
      alanlar: ["Aile Hukuku", "Ceza Hukuku", "İş ve Sosyal Güvenlik Hukuku", "Ticaret ve Şirketler Hukuku", "İcra ve İflas Hukuku", "Gayrimenkul Hukuku", "Miras Hukuku", "İdare ve Vergi Hukuku"],
      barolar: ["Malatya Barosu"],
      egitim: [
        "Hukuk Fakültesi — Lisans"      // TODO: üniversite ve yıl bilgisi
      ],
      deneyim: [
        "Aile hukukunda boşanma, velayet ve nafaka davaları ile mal rejiminin tasfiyesi süreçleri",
        "Ceza yargılamasının soruşturma ve kovuşturma aşamalarında şüpheli/sanık müdafiliği ve katılan vekilliği",
        "İş ve sosyal güvenlik hukukunda kıdem–ihbar tazminatı, işçilik alacakları ve iş kazasından doğan tazminat davaları",
        "Ticaret ve şirketler hukukunda ticari alacakların tahsili, çek–kambiyo takipleri ve şirket uyuşmazlıkları",
        "İcra ve iflas hukukunda ilamlı ve ilamsız takipler, itirazın iptali ve istihkak davaları",
        "Gayrimenkul hukukunda tapu iptali ve tescil, ortaklığın giderilmesi ve kamulaştırma davaları",
        "Miras hukukunda mirasçılık belgesinin alınması, tenkis ve mirasın paylaştırılması davaları",
        "İdare ve vergi hukukunda iptal ve tam yargı davaları ile vergi cezalarına itiraz süreçleri"
      ],
      uyelikler: ["Türkiye Barolar Birliği"]
    },
    {
      id: "merve-gelegen",
      ad: "Merve Gelegen",
      unvan: "Avukat / Kurucu Ortak",
      foto: "assets/img/Merve_Gelegen.webp",
      ozet:
        "Aile, ceza, iş ve sosyal güvenlik, ticaret ve şirketler, icra ve iflas, gayrimenkul, " +
        "miras ile idare ve vergi hukuku alanlarında dava takibi, sözleşme hazırlığı ve " +
        "kurumsal danışmanlık yürütmektedir.",
      alanlar: ["Aile Hukuku", "Ceza Hukuku", "İş ve Sosyal Güvenlik Hukuku", "Ticaret ve Şirketler Hukuku", "İcra ve İflas Hukuku", "Gayrimenkul Hukuku", "Miras Hukuku", "İdare ve Vergi Hukuku"],
      barolar: ["Malatya Barosu"],
      egitim: [
        "Hukuk Fakültesi — Lisans"      // TODO: üniversite ve yıl bilgisi
      ],
      deneyim: [
        "Aile hukukunda anlaşmalı ve çekişmeli boşanma, velayet ve iştirak nafakası ile aile konutu ve ziynet alacağı talepleri",
        "Ceza hukukunda şikâyet, uzlaştırma ve yargılama aşamalarında müdafilik ve suçtan zarar görenin vekilliği",
        "İş ve sosyal güvenlik hukukunda işe iade, hizmet tespiti ile fazla mesai ve yıllık izin alacakları davaları",
        "Ticaret ve şirketler hukukunda şirket kuruluşu, pay devri, genel kurul süreçleri ve ticari sözleşmelerin hazırlanması",
        "İcra ve iflas hukukunda alacağın tahsili, haciz işlemleri ve borca itirazın giderilmesi süreçleri",
        "Gayrimenkul hukukunda kira uyuşmazlıkları, tahliye davaları ve satış sözleşmelerinden doğan ihtilaflar",
        "Miras hukukunda vasiyetnamenin iptali, muris muvazaası ve saklı payın korunması davaları",
        "İdare ve vergi hukukunda idari başvuru ve dava süreçleri ile vergi uyuşmazlıklarında uzlaşma"
      ],
      uyelikler: ["Türkiye Barolar Birliği"]
    }
  ];

  /* ---------------------------------------------------------------
     3) Global erişim (diğer script'ler bu iki nesneyi okur)
     --------------------------------------------------------------- */
  window.SITE = Object.freeze(SITE);
  window.AVUKATLAR = Object.freeze(AVUKATLAR);
})();
