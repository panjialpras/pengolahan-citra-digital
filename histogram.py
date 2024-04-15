import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# baca gambar dari direktori yang ditentukan
image_dir = ("D:/Berkas Penting/Tugas Kuliah/Code/Py/image processing/chelsea-rgb.jpg")
image = cv.imread(image_dir)
# cv.imshow("Default", image)
# menyimpan channel warna RGB dan menyimpannya ke dalam variabel terpisah
b = image[:,:,0] #menyimpan channel biru
g = image[:,:,1] #menyimpan channel green
r = image[:,:,2] #menyimpan channel red

# simpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(image)
jum_kolom = len(image[0])
total_pixel = jum_baris * jum_kolom

#menyiapkan citra baru dengan nilai 0
image_gray = np.zeros((jum_baris, jum_kolom))

# menghitung histogram
hist_gray = np.zeros((256)) #buat histogram
# htiung nilai pixel grayscale
for i in range (jum_baris):
    for h in range (jum_kolom) :
        image_gray[i, h] = round(0.299 * r[i, h] + 0.587 * g[i, h] + 0.114 * b[i, h])

        # hitung kemunculan pixel
        pixel = int(image_gray[i, h])
        hist_gray[pixel] += 1

image_gray = image_gray.astype(np.uint8)

cv.imshow("Chelsea grayscale", image_gray)

# menampilkan histogram
plt.bar(range(256), hist_gray)
plt.waitforbuttonpress()

# tutup window

# WARNING: You are using pip version 21.2.4; however, version 21.3 is available.
# You should consider upgrading via the 'c:\users\panji\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip' command.
# 