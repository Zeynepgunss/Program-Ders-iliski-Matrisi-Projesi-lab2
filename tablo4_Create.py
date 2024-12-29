import pandas as pd
import numpy as np
# Load data files
# Load your specific Excel files as needed
# Tablo1, Tablo2, Tablo3, and ogrenci_notlari are already assumed to be loaded

def calculate_tablo4(tablo3, ogrenci_notlari, tablo1):
    valid_columns = ["Odev1", "Odev2", "Quiz", "Vize", "Final"]
    final_corrected_tablo4 = []

    # Check and rename columns in ogrenci_notlari to match valid_columns
    ogrenci_notlari = ogrenci_notlari.rename(columns={
        'Ödev1': 'Odev1',
        'Ödev2': 'Odev2',
        'Quiz': 'Quiz',
        'Vize': 'Vize',
        'Final': 'Final'
    })

    for index, ogrenci in ogrenci_notlari.iterrows():
        ogrenci_no = ogrenci["Öğrenci No"]
        ogrenci_tablosu = tablo3.copy()

        # Multiply Tablo 3 values by the corresponding student grades
        for kriter in valid_columns:
            if kriter not in ogrenci_tablosu.columns:
                raise KeyError(f"'{kriter}' column is missing in Tablo 3.")
            if kriter not in ogrenci.index:
                raise KeyError(f"'{kriter}' column is missing in Öğrenci Notları.")

            # Multiply Tablo 3 values by student grades and scale by 100
            ogrenci_tablosu[kriter] = ogrenci_tablosu[kriter] * (ogrenci[kriter] / 100) * 100

        # Calculate TOPLAM based on the weighted values
        ogrenci_tablosu["TOPLAM"] = ogrenci_tablosu[valid_columns].sum(axis=1)

        # Calculate MAX using Tablo1's relationship values multiplied by 100
        ogrenci_tablosu["MAX"] = tablo3["TOPLAM"] * 100

        # Calculate %Başarı
        ogrenci_tablosu["%Başarı"] = (ogrenci_tablosu["TOPLAM"] / ogrenci_tablosu["MAX"]) * 100

        # Add student information and format the table
        ogrenci_tablosu["Ders Çıktı"] = ogrenci_tablosu.index + 1
        ogrenci_tablosu["Öğrenci"] = ogrenci_no

        # Append the final format for this student
        final_corrected_tablo4.append(ogrenci_tablosu[[
            "Ders Çıktı", "Odev1", "Odev2", "Quiz", "Vize", "Final", "TOPLAM", "MAX", "%Başarı"
        ]])

    # Combine all student tables into one DataFrame
    final_corrected_tablo4 = pd.concat(final_corrected_tablo4, ignore_index=True)

    return final_corrected_tablo4

# Load data files
tablo3dataframe = pd.read_excel("tablo3.xlsx")
ogrencinotlari = pd.read_excel("ogrenci_notlari.xlsx")
tablo1dataframe = pd.read_excel("tablo1.xlsx")

# Calculate and save Tablo 4
final_tablo4 = calculate_tablo4(tablo3dataframe, ogrencinotlari, tablo1dataframe)
final_tablo4.to_excel("Final_Corrected_Tablo4_Output.xlsx", index=False)
# print(final_tablo4)
print("Tablo 4 has been successfully created.")



df = pd.DataFrame(final_tablo4)  # DataFrame oluşturulur

# DataFrame'i 5 parçaya bölelim
split_dfs = np.array_split(df, 25)  # DataFrame, 5 parçaya eşit olarak bölünür
sayac=2
# Bölünen parçaları yazdır
for i, part in enumerate(split_dfs):  # Her parçayı sırasıyla döngü içinde ele al
    # print(f"Parça {i+1}:")  # Parçanın sıra numarasını yazdır
    # print(part)  # O parçayı ekrana yazdır
    dfff=pd.DataFrame(part)
    dfff.to_excel("tablo4ler/tablo4_"+str(sayac)+".xlsx")
    sayac=sayac+1
