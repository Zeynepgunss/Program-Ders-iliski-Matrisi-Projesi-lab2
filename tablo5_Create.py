import pandas as pd
import numpy as np

# Tablo1 ve Tablo4 dosyalarını yükle
tablo1 = pd.read_excel("tablo1.xlsx")
tablo4 = pd.read_excel("Final_Corrected_Tablo4_Output.xlsx")

# Öğrencileri belirle (ilk satır genel, sonraki her 5 satır bir öğrenci)
tablo4['Öğrenci'] = np.nan
num_students = (len(tablo4) - 1) // 5
for i in range(num_students):
    tablo4.loc[i * 5 + 1:(i + 1) * 5 + 1, 'Öğrenci'] = i + 1

# İlk satır genel %Başarı olarak bırakılır
tablo4['Öğrenci'] = tablo4['Öğrenci'].ffill()

# NaN değerlerini filtrele
ogrenci_listesi = tablo4['Öğrenci'].dropna().unique()

# Her öğrenci için ayrı tablo oluştur
for ogrenci in ogrenci_listesi:
    if pd.isna(ogrenci) or ogrenci == 0:
        continue  # İlk satırı atla (genel %Başarı satırı)

    ogrenci_veri = tablo4[tablo4['Öğrenci'] == ogrenci]  # İlk satırı atla
    columns = ['Prg Çıktı'] + [str(x) for x in tablo1.columns[1:] if x != 'İlişki Değ.']  # Sütun başlıkları
    ogrenci_tablo = pd.DataFrame(columns=columns + ['Başarı Oranı'])

    for prg_cikti in range(1, 11):  # 1'den 10'a kadar PRG çıktıları
        tablo_row = {'Prg Çıktı': prg_cikti}
        prg_degerleri = tablo1.iloc[prg_cikti - 1, 1:].values  # PRG çıktıları satırındaki değerler
        basari_degerleri = ogrenci_veri['%Başarı'].tolist()

        # Çarpma işlemi ve yerleştirme (kaymayı önle)
        for j in range(5):  # 5 ders çıktısı varsayıyoruz
            tablo_row[columns[j + 1]] = basari_degerleri[j] * prg_degerleri[j] if j < len(basari_degerleri) else 0.0

            # Başarı oranını hesapla ve ekle
        ortalama = sum(list(tablo_row.values())[1:6]) / 5  # Başarı değerlerini topla
        iliski_degeri = tablo1.iloc[prg_cikti - 1]['İlişki Değ.']  # İlgili PRG çıktısı için ilişki değeri
        basari_orani = round(ortalama / iliski_degeri, 1) if iliski_degeri != 0 else 0.0
        tablo_row['Başarı Oranı'] = basari_orani

        ogrenci_tablo = pd.concat([ogrenci_tablo, pd.DataFrame([tablo_row])], ignore_index=True)

    # NaN kontrolü ve dosya oluşturma
    if not ogrenci_tablo.dropna(how='all').empty:
        ogrenci_tablo.to_excel(f'tablo5_ogrenci_{int(ogrenci)}.xlsx', index=False)
        print(f'Tablo 5 {int(ogrenci)} için başarıyla oluşturuldu.')
