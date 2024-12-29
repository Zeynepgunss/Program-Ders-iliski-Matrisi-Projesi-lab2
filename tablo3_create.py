import pandas as pd
import numpy as np

# Veri Yapısı Hazırlığı
program_ciktilari = [f"Program Çıktı {i}" for i in range(1, 6)]
ders_ciktilari = [f"Ders Çıktı {i}" for i in range(1, 6)]

değerlendirme_kriterleri = {
    "Odev1": 0, "Odev2": 0, "Quiz": 0, "Vize": 0, "Final": 0
}

# 1. Program Çıktıları / Ders Çıktıları İlişki Matrisi (Tablo1)
program_ders_matrisi = pd.read_excel("tablo1.xlsx")

# 2. Ders Çıktıları / Değerlendirme Kriterleri İlişki Matrisi (Tablo2)
ders_kriter_matrisi = pd.read_excel("tablo2.xlsx")

# Sütunları değerlendirme kriterlerine göre adlandır
expected_columns = list(değerlendirme_kriterleri.keys())
if len(ders_kriter_matrisi.columns) == len(expected_columns) + 1:
    ders_kriter_matrisi.columns = ["Ders Çıktı"] + expected_columns
else:
    raise ValueError("Ders kriter matrisi sütun sayısı, beklenen kriterlere uymuyor.")




# Ağırlıkları yüzdeliklere göre düzelt
weights = [int(ders_kriter_matrisi.loc[1,"Odev1"]),int( ders_kriter_matrisi.loc[1,"Odev2"]), int(ders_kriter_matrisi.loc[1,"Quiz"]),int( ders_kriter_matrisi.loc[1,"Vize"]),int( ders_kriter_matrisi.loc[1,"Final"])]



for i, kriter in enumerate(değerlendirme_kriterleri.keys()):
    değerlendirme_kriterleri[kriter] = weights[i] / 100  # Yüzdelikleri ağırlığa dönüştür


# 3. Ağırlıklı Değerlendirme Tablosu (Tablo3)
ağırlıklı_degerlendirme = ders_kriter_matrisi.iloc[:, 1:].copy()



# Sütunları sayısal değerlere dönüştür
for col in ağırlıklı_degerlendirme.columns:
    ağırlıklı_degerlendirme[col] = pd.to_numeric(ağırlıklı_degerlendirme[col], errors='coerce')


# Ağırlıkları çarp
for kriter, agirlik in değerlendirme_kriterleri.items():
    ağırlıklı_degerlendirme[kriter] = ağırlıklı_degerlendirme[kriter] * agirlik

ağırlıklı_degerlendirme["TOPLAM"] = ağırlıklı_degerlendirme.sum(axis=1)

# Tablo 3'ü Excel'e kaydet
# ağırlıklı_degerlendirme.to_excel("Tablo3_Output.xlsx", sheet_name="Tablo 3", index_label="Ders Çıktı")

ağırlıklı_degerlendirme.drop(0,axis=0,inplace=True)
ağırlıklı_degerlendirme.drop(1,axis=0,inplace=True)

ağırlıklı_degerlendirme.reset_index(inplace=True)
# ağırlıklı_degerlendirme.index=["a","y","s","e","l"]
ağırlıklı_degerlendirme.index=[1,2,3,4,5]
ağırlıklı_degerlendirme.to_excel("tablo3.xlsx", sheet_name="Tablo 3", index_label="Ders Çıktı")





