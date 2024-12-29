


#  TABLO1 VE TABLO 2  OLUŞTURUYORRRRRR
import pandas as pd

tablo2_data = [
    ["Ders Çıktı",    "Odev1",            "Odev2",            "Quiz",            "Vize",            "Final"],
    ["TABLO 2",  "YÜZDELİK",   "YÜZDELİK",   "YÜZDELİK",   "YÜZDELİK",   "YÜZDELİK"],
    [1, "", "", "", "", ""],
    [2, "", "", "", "", ""],
    [3, "", "", "", "", ""],
    [4, "", "", "", "", ""],
    [5, "", "", "", "", ""],
]
df_tablo2 = pd.DataFrame(tablo2_data)

# Öncelikle tabloya ait başlık satırı:
columns = ["Prg Çıktı", "1", "2", "3", "4", "5", "İlişki Değ."]

# 1’den 10’a kadar giden satırlar oluşturuyoruz.
# Bu satırlarda "Prg Çıktı" sütununa 1..10 değerlerini, diğer sütunlara boş değer ("") atıyoruz.
data = []
for i in range(1, 11):
    # Burada ilk hücre (Prg Çıktı) i değerini alıyor, geri kalanı boş
    row = [i, "", "", "", "", "", ""]
    data.append(row)

# DataFrame'i oluştur
df_tablo1 = pd.DataFrame(data, columns=columns)

# Excel'e kaydet (index=False diyerek DataFrame indeksini yazdırmıyoruz)


df_tablo1.to_excel("tablo1.xlsx", index=False)

df_tablo2.to_excel("tablo2.xlsx",index=False)


