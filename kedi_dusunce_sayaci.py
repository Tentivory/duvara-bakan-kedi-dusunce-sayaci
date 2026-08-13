#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Duvara Bakan Kedi Düşünce Sayacı (DBKDS)
Bilimsel olarak kanıtlanmamış ama son derece ikna edici bir sistem.
"""

import random
import time
import sys

DUSUNCELER = [
    "Acaba duvarın arkasında başka bir duvar var mı?",
    "Ben bir kedi miyim yoksa duvar mı?",
    "Bu duvar bana bakıyor olabilir mi?",
    "Varoluşun anlamı... miyav.",
    "Eğer gözlerimi kapatsam duvar kaybolur mu?",
    "İnsanlar neden bu kadar telaşlı? Ben duvara bakıyorum, mutluyum.",
    "Belki de duvar beni seviyor.",
    "Sonsuzluk bir duvara bakmak gibi olabilir.",
    "Bu anın değeri nedir? Muhtemelen 3.7 düşünce.",
    "Kedilik felsefesi: Bak, düşün, uyuyakal.",
    "Duvarın rengi değişiyor mu yoksa ben mi değişiyorum?",
    "Bir gün duvar hareket edecek. O gün hazır olacağım.",
    "Miyav... yani... derin bir düşünce.",
    "Belki de ben duvarım ve kedi bana bakıyor.",
    "Zaman nedir? Duvara bakmak dışında hiçbir şey.",
]

FELSEFI_DERINLIK = [
    "Sığ (sadece miyav)",
    "Orta (hafif varoluşsal)",
    "Derin (Nietzsche seviyesinde)",
    "Uçurum (Schopenhauer + kedi)",
    "Kara delik (anlamı yok, sadece boşluk)",
]

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def ana_program():
    print("=" * 60)
    yavas_yaz("🐈 DUVARA BAKAN KEDİ DÜŞÜNCE SAYACI v1.0")
    print("=" * 60)
    print()
    yavas_yaz("Sistem başlatılıyor...")
    time.sleep(1)
    yavas_yaz("Hayali kedi oluşturuluyor...")
    time.sleep(0.8)
    yavas_yaz("Duvar algılandı. Kedi pozisyonu: sabit.")
    time.sleep(0.7)
    yavas_yaz("Düşünce ölçümü başlıyor...")
    print()

    bakis_suresi = random.randint(12, 487)
    dusunce_sayisi = random.randint(3, 42)
    
    yavas_yaz(f"Ölçülen bakış süresi: {bakis_suresi} saniye")
    time.sleep(0.5)
    yavas_yaz(f"Tespit edilen düşünce sayısı: {dusunce_sayisi}")
    print()
    yavas_yaz("Düşünceler çözümleniyor...")
    print("-" * 40)

    for i in range(1, dusunce_sayisi + 1):
        dusunce = random.choice(DUSUNCELER)
        derinlik = random.choice(FELSEFI_DERINLIK)
        print(f"{i:02d}. [{derinlik}] {dusunce}")
        time.sleep(0.4)

    print("-" * 40)
    print()
    yavas_yaz("Analiz tamamlandı.")
    time.sleep(0.6)
    
    ortalama = round(dusunce_sayisi / max(bakis_suresi, 1) * 60, 2)
    yavas_yaz(f"Dakikadaki ortalama düşünce: {ortalama}")
    yavas_yaz("Sonuç: Kediniz ya çok düşünüyor ya da hiç düşünmüyor. İkisi de mümkün.")
    print()
    print("=" * 60)
    yavas_yaz("Program sona erdi. Artık siz de duvara bakabilirsiniz.")
    print("=" * 60)

if __name__ == "__main__":
    try:
        ana_program()
    except KeyboardInterrupt:
        print("\n\nKedi kaçtı. Ölçüm yarıda kaldı.")
