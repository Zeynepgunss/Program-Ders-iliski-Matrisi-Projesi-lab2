import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://ebs.kocaelisaglik.edu.tr/Pages/CourseDetail.aspx?lang=tr-TR&academicYear=2024&facultyId=5&programId=1&menuType=course&catalogId=2227"

# Perform GET request
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all tables
    tables = soup.find_all('table')

    all_data = []  # List to store all rows from tables

    for table in tables:
        # Extract headers
        headers = [header.text.strip() for header in table.find_all('th')]

        # Extract rows
        rows = []
        for row in table.find_all('tr'):
            cells = [cell.text.strip() for cell in row.find_all(['td', 'th'])]

            # Skip "Loading..." rows
            if "Loading" not in cells and cells:
                rows.append(cells)

        # Convert to DataFrame
        if headers and len(rows) > 1:
            df = pd.DataFrame(rows[1:], columns=headers)  # Skip header row in rows
        else:
            df = pd.DataFrame(rows)

        all_data.append(df)

    # Combine all tables into one DataFrame (alt alta ekle)
    combined_df = pd.concat(all_data, ignore_index=True)

    # Save to a single Excel sheet
    combined_df.to_excel("combined_course_details.xlsx", sheet_name="Tüm Tablolar", index=False)

    print("Tablolar tek sekmede 'combined_course_details.xlsx' dosyasına kaydedildi.")
else:
    print(f"Sayfaya erişim başarısız. HTTP Durum Kodu: {response.status_code}")
