#!/usr/bin/env python3
#crete by TegarDev
#this project is open source
#please give me credit, if you modified this project
#this is priject youtube video downloader using tkinter
#credit : api by JOJO APIs


# import module
from tkinter import *
from tkinter import ttk, filedialog
import requests, json, shutil, os

# rest api by JOJO APIs
api = "https://docs-jojo.herokuapp.com/api/ytmp4?url="

# build new windows
root = Tk()
root.title("YT Video Downloader")
root.config(background="#fff")

root.geometry("450x450")
root.columnconfigure(0, weight=1)

# variabel untuk membuat nama folder
nama_folder = ""

# file
def bukaLokasi():
    global nama_folder
    nama_folder = filedialog.askdirectory()
    if (len(nama_folder) > 1):
        lokasiError.config(text=nama_folder, fg="green")

    else:
        lokasiError.config(text="Pilih folder dulu!", fg="red")

# cek url
def cekURL():
    url = entry_url.get()
    req = requests.get(api+url)
    jeson = json.loads(req.text)
    data = jeson
    try:
        UrlError.config(text=f"judul : {data['title']}\nresult : {data['result']}\nthumbnail : {data['thumb']}\nukuran file : {data['filesize']}", fg="green")
    except:
        UrlError.config(text=f"result : {data['result']}")



# download video
def Download():
    url_vid = entry_url.get()
    requ = requests.get(api+url_vid)
    jeeson = json.loads(requ.text)
    dataa = jeeson
    link = dataa['result']
    vid_url = link
    nama_file = vid_url.split("/")[-1]
    file = nama_file+'.mp4'
    folder = nama_folder
    r = requests.get(vid_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(file,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            os.system(f"mv {file} {folder}")
            hasil = Label(root,
                    text=f'Berhasil, Disimpan di : {folder}\nNama file : {file}',
                    font=("Roboto", 16),
                    fg="green")
            hasil.grid(pady=1)
    else:
        hasil = Label(root,
                text='Terjadi Kesalahan',
                font=("Roboto", 16),
                fg="green")
        hasil.grid(pady=1)




# judul
judul = Label(root,
        text="YT Video Downloader by Tegar",
        font=("Roboto", 18))
judul.grid(pady=1)

# lebel url
url_label = Label(root,
        text="Masukan URL:",
        bg="#fff",
        font=("Roboto", 16))
url_label.grid(pady=1)

# input url
entry_url_var = StringVar()
entry_url = Entry(root,
        width=50,
        textvariable = entry_url_var,
        font=("Roboto", 16),
        justify="center")
entry_url.grid(pady=1)

# cek URL
url_cek = Button(root,
        width=10,
        text="Cek URL",
        bg="#ef5350",
        fg="white",
        font=("Roboto", 16),
        command=cekURL)
url_cek.grid(pady=1)

# url error
UrlError = Label(root,
        text="URL belum di pilih",
        bg="#fff",
        fg="red",
        font=("Roboto", 16))
UrlError.grid(pady=1)

# lebel pilih lokasi folder
file_label = Label(root,
        text="Pilih lokasi simpan video",
        bg="#fff",
        font=("Roboto", 16))
file_label.grid(pady=1)

# pilih lokasi folder
choose_file = Button(root,
        text="Pilih Lokasi",
        bg="#ef5350",
        font=("Roboto", 16),
        fg="white",
        command=bukaLokasi)
choose_file.grid(pady=1)

# error lokasi folder
lokasiError = Label(root,
        text="Lokasi file belum dipilih",
        bg="#fff",
        fg="red",
        font=("Roboto", 16))
lokasiError.grid(pady=1)

# download
donlot = Button(root,
        text="Download",
        bg="#ef5350",
        fg="white",
        font=("Roboto", 16),
        command=Download)
donlot.grid(pady=1)

root.mainloop()
