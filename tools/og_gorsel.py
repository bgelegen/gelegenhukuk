# -*- coding: utf-8 -*-
"""
Paylaşım görseli (og-image) üretici — giriş videosundaki adliye sütunları karesini
mevcut görselin (yazı + logo) arkasına yerleştirir.

    /Applications/Blender.app/Contents/MacOS/Blender -b --python tools/og_gorsel.py -- \
        <kare.png> <og-image.png (yazı katmanı)> <cikti.png>

Yöntem: Kare 1200x630'a ölçeklenip kırpılır, laciverte boyanır ve koyulaştırılır
(yazıların bulunduğu sol taraf daha koyu). Ardından mevcut görselle "açığı seç"
(lighten) karışımı yapılır: beyaz/altın yazı ve logo aynen üstte kalır, lacivert
zemin yerine sütunlu sahne görünür.
"""
import sys
import bpy
import numpy as np

kare_yol, yazi_yol, cikti = sys.argv[sys.argv.index("--") + 1:][:3]
W, H = 1200, 630


def yukle(yol):
    im = bpy.data.images.load(yol)
    im.colorspace_settings.name = "Non-Color"      # renk dönüşümü olmadan ham değerler
    return im


# --- Arka plan karesi: 1200 genişliğe ölçekle, ortadan 630 yükseklik kırp
kare = yukle(kare_yol)
kw, kh = kare.size
yeni_h = round(kh * W / kw)
kare.scale(W, yeni_h)
a = np.array(kare.pixels[:], dtype=np.float32).reshape(yeni_h, W, 4)
ust = (yeni_h - H) // 2
a = a[ust:ust + H, :, :3]                         # (Blender satırları alttan başlar; simetrik kırpma)

# --- Laciverte boya: parlaklığı al, lacivert/mavi tonla yeniden renklendir
lum = a[..., 0] * 0.2126 + a[..., 1] * 0.7152 + a[..., 2] * 0.0722
ton = np.array([0.66, 0.78, 1.0], dtype=np.float32)
taban = np.array([0.035, 0.065, 0.12], dtype=np.float32)   # sitedeki lacivert (#0A1424 civarı)
b = taban + lum[..., None] * ton

# --- Koyulaştırma maskesi: solda (yazılar) güçlü, sağda (logo) daha hafif; üst-altta hafif kararma
x = np.linspace(0, 1, W, dtype=np.float32)
yatay = np.interp(x, [0.0, 0.50, 0.66, 1.0], [0.32, 0.36, 0.62, 0.72]).astype(np.float32)
y = np.linspace(0, 1, H, dtype=np.float32)
dikey = np.interp(y, [0.0, 0.12, 0.88, 1.0], [0.70, 1.0, 1.0, 0.75]).astype(np.float32)
maske = dikey[:, None] * yatay[None, :]
# Logonun arkasında yumuşak bir koyuluk (parlak sütun kenarı amblemi kalabalıklaştırmasın).
# Logo merkezi ~ (945, 315); Blender satırları alttan başladığı için y = H - 315.
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.sqrt((xx - 945) ** 2 + (yy - (H - 315)) ** 2)
logo_koyu = np.interp(r, [0, 150, 260], [0.55, 0.62, 1.0]).astype(np.float32)
maske = maske * logo_koyu
b = taban + (b - taban) * maske[..., None]

# --- Yazı katmanı: mevcut görsel
yazi = yukle(yazi_yol)
assert tuple(yazi.size) == (W, H), yazi.size
t = np.array(yazi.pixels[:], dtype=np.float32).reshape(H, W, 4)[..., :3]

sonuc = np.maximum(b, t)                          # açığı seç: yazı/logo üstte kalır
sonuc = np.clip(sonuc, 0, 1)

out = bpy.data.images.new("og", W, H, alpha=False)
out.colorspace_settings.name = "Non-Color"
rgba = np.concatenate([sonuc, np.ones((H, W, 1), dtype=np.float32)], axis=2)
out.pixels = rgba.ravel()
out.filepath_raw = cikti
out.file_format = "PNG"
out.save()
print("YAZILDI", cikti)
