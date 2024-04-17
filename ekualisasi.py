import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# baca gambar dari direktori yang ditentukan
image_dir = ("img/chelsea - rgb - high brightness.jpg")
image = cv.imread(image_dir)
# cv.imshow("Default", image)
# menyimpan channel warna RGB dan menyimpannya ke dalam variabel terpisah

b = image[:, :, 0]  # menyimpan channel biru
g = image[:, :, 1]  # menyimpan channel green
r = image[:, :, 2]  # menyimpan channel red

# simpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(image)
jum_kolom = len(image[0])
total_pixel = jum_baris * jum_kolom

# citra baru dengan nilai 0
image_gray = np.zeros((jum_baris, jum_kolom))

# menghitung histogram
hist_gray = np.zeros((256))  # buat histogram
# htiung nilai pixel grayscale
for i in range(jum_baris):
    for h in range(jum_kolom):
        image_gray[i, h] = round(
            0.299 * r[i, h] + 0.587 * g[i, h] + 0.114 * b[i, h])

        # hitung kemunculan pixel
        pixel = int(image_gray[i, h])
        hist_gray[pixel] += 1 / total_pixel

image_gray = image_gray.astype(np.uint8)

# ekualisasi histogram
pixel_baru = np.zeros((256))  # buat histogram untuk hasil ekualisasi
temp_sum = 0
for i in range(256):
    temp_sum += hist_gray[i]
    pixel_baru[i] = int(round(255 * temp_sum))

# konversi float array pada numpy menjadi integer
pixel_baru = pixel_baru.astype(np.uint8)

hist_gray_eq = np.zeros((256))  # buat histogram hasil ekualisasi baru
# buat citra baru hasil ekualisasi
image_gray_eq = np.zeros((jum_baris, jum_kolom))
for i in range(jum_baris):
    for j in range(jum_kolom):
        # ganti pixel lama ke pixel_baru hasil ekualisasi
        pixel = image_gray[i][h]  # baca pixel lama
        pixel = pixel_baru[pixel]  # isi pixel lama ganti ke pixel_baru

        image_gray_eq[i][h] = pixel

        # hitung kemunculan pixel
        hist_gray_eq[pixel] += 1 / total_pixel  # Di normalisasi

pixel_baru = pixel_baru.astype(np.uint8)

cv.imshow("grayscale awal", image_gray)
cv.imshow("grayscale eq", image_gray)

# menampilkan histogram
plt.bar(range(256), hist_gray)
plt.bar(range(256), hist_gray_eq)
# auto close ketika ketik apapun
plt.waitforbuttonpress()

# WARNING: You are using pip version 21.2.4; however, version 21.3 is available.
# You should consider upgrading via the 'c:\users\panji\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip' command.
