/* ==========================================================================
   hero-video.js — Anasayfa hero arka plan videosu ("Adliye Sütunları")
   --------------------------------------------------------------------------
   Video Blender'da render edilmiştir (kaynak: Blender/adliye_sahnesi.py) ve
   kesintisiz döngüdür. Bu dosya yalnızca oynatmayı yönetir:
   - JavaScript kapalıysa video oynamaz, sabit poster karesi görünür.
   - "Hareketi azalt" tercihinde poster görünür, video oynatılmaz.
   - "Veri tasarrufu" açık cihazlarda video hiç indirilmez (yalnızca poster).
   - Hero ekran dışındayken veya sekme gizliyken video duraklar.
   ========================================================================== */
(function () {
  "use strict";

  const video = document.querySelector(".hero__video");
  if (!video) return;

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  const conn = navigator.connection;
  if (conn && conn.saveData) {
    video.querySelectorAll("source").forEach((s) => s.remove());
    video.preload = "none";
    return;                                   // yalnızca poster
  }

  let visible = true;
  video.muted = true;                         // tarayıcıların otomatik oynatma şartı

  function apply() {
    const go = !reduce.matches && visible && !document.hidden;
    if (go) {
      const p = video.play();
      if (p && p.catch) p.catch(() => {});   // engellenirse poster kalır
    } else {
      video.pause();
    }
  }

  video.addEventListener("playing", () => video.classList.add("is-playing"), { once: true });

  if ("IntersectionObserver" in window) {
    new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; apply(); })
      .observe(video);
  }
  document.addEventListener("visibilitychange", apply);
  if (reduce.addEventListener) reduce.addEventListener("change", apply);
  apply();
})();
