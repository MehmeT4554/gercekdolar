import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# Dolar fiyatını alma fonksiyonu
def get_dolar_price():
    url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # HTML içeriğini parse et
        soup = BeautifulSoup(response.text, "html.parser")
        dolar_section = soup.find("span", {"class": "value"})
        if dolar_section:
            dolar_fiyati = dolar_section.text.strip()
            dolar_fiyati = dolar_fiyati.replace(".", "").replace(",", ".")
            return dolar_fiyati
        else:
            return "Dolar fiyatı bulunamadı!"
    except Exception as e:
        return f"Hata: {e}"

# Text dosyasına yazma fonksiyonu
def save_to_desktop(dolar_price):
    # Mevcut tarih
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Kullanıcının masaüstü yolu
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Dosya adı
    file_name = f"Dolar_Fiyati_{datetime.now().strftime('%Y-%m-%d')}.txt"
    file_path = os.path.join(desktop_path, file_name)
    
    # Dosya içeriği
    content = f"Tarih: {current_date}\nGüncel Dolar Fiyatı: {dolar_price} TL\n"
    
    # Dosyayı yaz
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Dolar fiyatı şu dosyaya kaydedildi: {file_path}")

# Ana işlem
dolar_fiyati = get_dolar_price()
save_to_desktop(dolar_fiyati)
