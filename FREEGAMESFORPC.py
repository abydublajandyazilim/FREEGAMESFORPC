import tkinter as tk
import webbrowser

# Butonlara basınca açılacak URL'ler
linkler = {
    "minecraft PC": "https://cloud.mail.ru/public/qGzf/gceoG8pHh",
    "GTA SA PC": "https://cloud.mail.ru/public/qGzf/gceoG8pHh",
    "HALF LİFE ": "hatgpt.com/c/6765afff-6608-8000-bca4-7bfac8ab4e6d",
    "youtube": "https://github.com/inotia00/revanced-manager/releases/download/v1.21.1/rvx-manager-v1.21.1-universal.apk"
}

# Link açma fonksiyonu
def linke_git(url):
    webbrowser.open_new_tab(url)

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("korsanoyun")
pencere.geometry("300x250")
pencere.configure(bg="#f0f0f0")

# Başlık etiketi
etiket = tk.Label(pencere, text="half llife şifresi:oyunindir.cafe", font=("Arial", 14), bg="#f0f0f0")
etiket.pack(pady=10)

# Butonları oluştur
for isim, url in linkler.items():
    buton = tk.Button(pencere, text=isim, font=("Arial", 12), width=20, command=lambda u=url: linke_git(u))
    buton.pack(pady=5)

# Pencereyi çalıştır
pencere.mainloop()