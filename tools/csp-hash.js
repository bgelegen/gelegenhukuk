#!/usr/bin/env node
/* ==========================================================================
   csp-hash.js — Content-Security-Policy için satır içi script hash üretici
   --------------------------------------------------------------------------
   NEDEN GEREKLİ?
   Sayfalarımızda çalıştırılabilir satır içi JavaScript YOKTUR; ancak SEO için
   satır içi JSON-LD (<script type="application/ld+json">) blokları vardır.
   CSP, tür fark etmeksizin tüm <script> etiketlerini script-src ile denetler.
   Bu yüzden 'unsafe-inline' açmak yerine her bloğun SHA-256 hash'ini
   politikaya eklemek en güvenli yoldur.

   KULLANIM:
     node tools/csp-hash.js
   Çıktıdaki 'sha256-...' değerlerini .htaccess / _headers dosyalarındaki
   script-src satırına yapıştırın.

   HATIRLATMA: JSON-LD içeriğini her düzenlediğinizde hash DEĞİŞİR;
   bu komutu yeniden çalıştırıp politikayı güncelleyin.
   ========================================================================== */

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const kok = path.resolve(__dirname, "..");
const htmlDosyalari = fs
  .readdirSync(kok)
  .filter((f) => f.endsWith(".html"));

const hashler = new Map();

htmlDosyalari.forEach((dosya) => {
  const icerik = fs.readFileSync(path.join(kok, dosya), "utf8");
  const regex = /<script(?![^>]*\ssrc=)[^>]*>([\s\S]*?)<\/script>/gi;
  let eslesme;
  while ((eslesme = regex.exec(icerik)) !== null) {
    const govde = eslesme[1];
    const hash = "sha256-" + crypto.createHash("sha256").update(govde, "utf8").digest("base64");
    if (!hashler.has(hash)) hashler.set(hash, []);
    hashler.get(hash).push(dosya);
  }
});

if (hashler.size === 0) {
  console.log("Satır içi script bulunamadı. script-src 'self' yeterlidir.");
  process.exit(0);
}

console.log("\n=== Satır içi script hash'leri (" + hashler.size + " adet) ===\n");
hashler.forEach((dosyalar, hash) => {
  console.log("'" + hash + "'   <- " + dosyalar.join(", "));
});

console.log("\n=== script-src satırı (kopyalayıp yapıştırın) ===\n");
console.log("script-src 'self' " + Array.from(hashler.keys()).map((h) => "'" + h + "'").join(" ") + ";\n");
