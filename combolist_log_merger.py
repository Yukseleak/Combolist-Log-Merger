import os
import random
import string
import zipfile
import shutil
import re
from colorama import Fore, Style, init

init(autoreset=True)  # Colorama'yı başlat

def random_filename(extension=".txt"):
    """Rastgele bir dosya adı oluşturur."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) + extension

def combine_combolists_from_folder():
    folder_path = input("Comboların bulunduğu klasörün yolunu girin: ")

    combined_data = []

    # Klasördeki tüm .txt dosyalarını oku
    if not os.path.isdir(folder_path):
        print("Geçersiz klasör yolu. Lütfen doğru bir yol girin.")
        return

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    combined_data.extend(file.readlines())
            except Exception as e:
                print(f"Dosya okunurken hata: {file_path} - Hata: {e}")
    
    # Birleştirilen verinin boş olup olmadığını kontrol et
    if not combined_data:
        print("Birleştirilen veriler boş. Lütfen dosyaları kontrol edin.")
        return

    # Kaydetme işlemi için seçenek sun
    print("1. Masaüstüne rastgele isimle kaydet")
    print("2. Kendi belirlediğin bir yere kaydet")
    save_choice = input("Seçiminizi yapın (1/2): ")

    if save_choice == '1':
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        random_file_name = random_filename()
        save_path = os.path.join(desktop_path, random_file_name)
        print(f"Birleştirilmiş dosya masaüstüne şu isimle kaydedilecek: {random_file_name}")
    elif save_choice == '2':
        save_path = input("Birleştirilmiş dosyayı nereye kaydetmek istiyorsunuz (dosya adıyla birlikte)? ")
    else:
        print("Geçersiz seçim.")
        return
    
    # Birleştirilmiş dosyayı kaydet
    try:
        with open(save_path, 'w', encoding='utf-8') as save_file:
            save_file.writelines(combined_data)
        print(f"Birleştirilmiş dosya başarıyla kaydedildi: {save_path}")
    except Exception as e:
        print(f"Dosya kaydedilirken hata: {save_path} - Hata: {e}")

def combine_logs():
    folder_or_zip = input("Bir klasör veya zip dosyası yolunu girin: ")

    combined_data = []

    if zipfile.is_zipfile(folder_or_zip):
        with zipfile.ZipFile(folder_or_zip, 'r') as zip_ref:
            zip_ref.extractall("temp_extracted")
            folder_or_zip = "temp_extracted"

    # Klasördeki tüm dosyaları oku
    for root, dirs, files in os.walk(folder_or_zip):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    combined_data.extend(file.readlines())
            except Exception as e:
                print(f"Dosya okunurken hata: {file_path} - Hata: {e}")

    # Birleştirilen verinin boş olup olmadığını kontrol et
    if not combined_data:
        print("Birleştirilen veriler boş. Lütfen dosyaları kontrol edin.")
        return

    # Kaydetme işlemi için seçenek sun
    print("1. Masaüstüne rastgele isimle kaydet")
    print("2. Kendi belirlediğin bir yere kaydet")
    save_choice = input("Seçiminizi yapın (1/2): ")

    if save_choice == '1':
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        random_file_name = random_filename()
        save_path = os.path.join(desktop_path, random_file_name)
        print(f"Birleştirilmiş dosya masaüstüne şu isimle kaydedilecek: {random_file_name}")
    elif save_choice == '2':
        save_path = input("Birleştirilmiş dosyayı nereye kaydetmek istiyorsunuz (dosya adıyla birlikte)? ")
    else:
        print("Geçersiz seçim.")
        return
    
    # Birleştirilmiş dosyayı kaydet
    try:
        with open(save_path, 'w', encoding='utf-8') as save_file:
            save_file.writelines(combined_data)
        print(f"Birleştirilmiş dosya başarıyla kaydedildi: {save_path}")
    except Exception as e:
        print(f"Dosya kaydedilirken hata: {save_path} - Hata: {e}")

    # Geçici dosyaları temizle
    if os.path.exists("temp_extracted"):
        shutil.rmtree("temp_extracted")

def other_tasks():
    print("Diğer ıvır zıvır görevler için buraya eklemeler yapabilirsiniz.")

def print_ascii_art():
    ascii_art = r"""
 
 ▄· ▄▌▄• ▄▌▄ •▄ .▄▄ · ▄▄▄ .▄▄▌  ▄▄▄ . ▄▄▄· ▄ •▄ 
▐█▪██▌█▪██▌█▌▄▌▪▐█ ▀. ▀▄.▀·██•  ▀▄.▀·▐█ ▀█ █▌▄▌▪
▐█▌▐█▪█▌▐█▌▐▀▀▄·▄▀▀▀█▄▐▀▀▪▄██▪  ▐▀▀▪▄▄█▀▀█ ▐▀▀▄·
 ▐█▀·.▐█▄█▌▐█.█▌▐█▄▪▐█▐█▄▄▌▐█▌▐▌▐█▄▄▌▐█ ▪▐▌▐█.█▌
  ▀ •  ▀▀▀ ·▀  ▀ ▀▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀  ▀  ▀ ·▀  ▀
             Combo Ve Log Birleştirme 
                       TOOLU
https://t.me/yukseleaktool ||| CRACKERMAİN.NET
    """

    print(Fore.LIGHTBLACK_EX + Fore.LIGHTYELLOW_EX + ascii_art + Style.RESET_ALL)
  

def print_menu():
      
    print(Fore.WHITE + "1. Combolist Birleştir" + Style.RESET_ALL)
    print(Fore.WHITE + "2. Log Birleştir" + Style.RESET_ALL)
    print(Fore.WHITE + "3. Diğer Ivır Zıvır" + Style.RESET_ALL)

    choice = input  (Fore.LIGHTYELLOW_EX + "Seçiminizi yapın (1/2/3): ")

    if choice == '1':
        combine_combolists_from_folder()
    elif choice == '2':
        combine_logs()
    elif choice == '3':
        other_tasks()
    else:
        print("Geçersiz seçim.")

def main():
    print_ascii_art()  # ASCII sanatını başta göster
    print_menu()       # Menü

if __name__ == "__main__":
    main()
