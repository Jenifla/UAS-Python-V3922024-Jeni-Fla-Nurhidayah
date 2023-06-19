#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen #import modul urlopen untuk membuka url dan membaca halaman web
from bs4 import BeautifulSoup  #import modul BeautifulSoup dari pustaka bs4 untuk melakukan parsing HTML

category = "Computer-Printers"  #definisikan kategori produk yang akan diambil dari situs eBay 
page_numbers = [1, 2]  #definisikan nomor halaman yang akan diambil dari situs eBay

for page_number in page_numbers: #melalukan loop untuk setiap nomor halaman yang ditentukan
    url = f'https://www.ebay.com/b/{category}/1245/bn_320031?_pgn={page_number}'  #URL berdasarkan kategori produk dan nomor halaman yang akan dilakukan scrapping
    html = urlopen(url).read()  #buka URL dan membaca seluruh isi halaman web
    soup = BeautifulSoup(html, "html.parser") #Menginisialisasi objek BeautifulSoup dengan HTML yang dibaca
    
    produk = soup.find_all("li", class_="s-item s-item--large")  #mencari semua elemen <li> dengan kelas CSS "s-item s-item--large", yang merupakan kontainer untuk setiap produk di halaman web.
    
    for p in produk:  #loop untuk setiap elemen produk yang ditemukan.
        title = p.find('h3', class_='s-item__title').get_text()  #mencari elemen <h3> dengan kelas CSS "s-item__title" di dalam elemen produk dan get_text() untuk mendapatkan teks nama produk.
        
        #mencari elemen <span> dengan kelas CSS "s-item__price" di dalam elemen produk dan get_text() untuk mendapatkan teks harga produk.
        price = p.find('span', class_='s-item__price').get_text().replace('IDR','').replace(',','').replace('.','')   #replace() untuk menghapus string 'IDR', koma (',') dan titik ('.') agar hanya tersisa angka.
    
        print("Nama Produk:", title) #mencetak nama produk yang nilainya diambil dari variabel title
        print("Harga Produk:", price) #Mencetak harga produk yang nilainya diambil dari variabel price
        print("Kategori:", category) #Mencetak kategori produk yang nilainya diambil dari variabel category
        print()


# In[2]:


from urllib.request import urlopen  #import modul urlopen untuk membuka url dan membaca halaman web
from bs4 import BeautifulSoup  #import modul BeautifulSoup dari pustaka bs4 untuk melakukan parsing HTML
import csv #import modul csv untuk membantu menulis data ke file CSV.

category = "Computer-Printers" #definisikan kategori produk yang akan diambil dari situs eBay 
page_numbers = [1, 2] #definisikan nomor halaman yang akan diambil dari situs eBay

#Membuka file CSV untuk penulisan
with open('Scraping Ebay.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile) #Membuat objek writer untuk menulis data ke file CSV.
    writer.writerow(['Nama Produk', 'Harga Produk', 'Kategori'])  #Menulis header kolom

    for page_number in page_numbers:  #melalukan loop untuk setiap nomor halaman yang ditentukan
        url = f'https://www.ebay.com/b/{category}/1245/bn_320031?_pgn={page_number}'  #URL berdasarkan kategori produk dan nomor halaman yang akan dilakukan scrapping
        html = urlopen(url).read()  #buka URL dan membaca seluruh isi halaman web
        soup = BeautifulSoup(html, "html.parser")  #Menginisialisasi objek BeautifulSoup dengan HTML yang dibaca

        produk = soup.find_all("li", class_="s-item s-item--large") #mencari semua elemen <li> dengan kelas CSS "s-item s-item--large", yang merupakan kontainer untuk setiap produk di halaman web.

        for p in produk: #loop untuk setiap elemen produk yang ditemukan.
            title = p.find('h3', class_='s-item__title').get_text() #mencari elemen <h3> dengan kelas CSS "s-item__title" di dalam elemen produk dan get_text() untuk mendapatkan teks nama produk.
            
            #mencari elemen <span> dengan kelas CSS "s-item__price" di dalam elemen produk dan get_text() untuk mendapatkan teks harga produk.
            price = p.find('span', class_='s-item__price').get_text().replace('IDR','').replace(',','').replace('.','')   #replace() untuk menghapus string 'IDR', koma (',') dan titik ('.') agar hanya tersisa angka.

            # Menulis data produk ke dalam file CSV
            writer.writerow([title, price, category])

#Menampilkan pesan 
print("Data telah disimpan ke dalam file Scraping Ebay.csv")


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

# Membaca database
data = pd.read_csv("Scraping Ebay.csv")

# Scatter plot dengan Nama Produk pada sumbu x dan Harga Produk pada sumbu y
plt.scatter(data['Nama Produk'], data['Harga Produk'])

# Menambahkan judul pada plot
plt.title("Scatter Plot")

# Mengatur label sumbu x dan y
plt.xlabel('Nama Produk')
plt.ylabel('Harga Produk')

# Menyimpan gambar
plt.savefig("Scatter Plot.jpg")

# Menampilkan plot
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

#Membaca database 
data = pd.read_csv("Scraping Ebay.csv")

#Membuat bar chart dengan Nama Produk pada sumbu x dan Harga Produk pada sumbu y
plt.bar(data['Nama Produk'], data['Harga Produk'])

#Menambahkan judul
plt.title("Bar Chart")

#Mengatur label sumbu x dan y
plt.xlabel('Nama Produk')
plt.ylabel('Harga Produk')

#Saving the figure.
plt.savefig("Bar Chart.jpg")

#Menampilkan plot
plt.show()


# In[ ]:




