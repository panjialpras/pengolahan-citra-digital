import cv2 as cv
import numpy as np

image1 = cv.imread("D:/Berkas Penting/Tugas Kuliah/Code/Py/image processing/chelsea-rgb.jpg")
image2 = cv.imread("D:/Berkas Penting/Tugas Kuliah/Code/Py/image processing/kacamata.jpg")

# baca variabel warna RGB + simpan ke dalam variabel terpisah
b1 = image1[:, :, 0]
g1 = image1[:, :, 1]
r1 = image1[:, :, 2]

b2 = image2[:, :, 0]
g2 = image2[:, :, 1]
r2 = image2[:, :, 2]

# simpan jumlah baris dan kolom dari citra
jum_baris = len(image1)
jum_kolom = len(image1[0])

# simpan citra baru dengan nilai 0
image_add = np.zeros((jum_baris, jum_kolom, 3))

# hitung nilai pixel grayscale
for a in range(jum_baris):
    for b in range(jum_kolom):
        image_add[a, b, 0] = int(b1[a, b]) + int(b2[a, b])
        image_add[a, b, 1] = int(g1[a, b]) + int(g2[a, b])
        image_add[a, b, 2] = int(r1[a, b]) + int(r2[a, b])

        # mengulang nilai pixel jika > 255
        if (image_add[a, b, 0] > 255) :
            image_add[a, b, 0] = 255

        if (image_add[a, b, 1] > 255) :
            image_add[a, b, 1] = 255

        if (image_add[a, b, 2] > 255) :
            image_add[a,++ b, 2] = 255

image_add = image_add.astype(np.uint8)

cv.imshow("Chelsea RGB", image1)
cv.imshow("kacamata", image2)
cv.imshow("ADD", image_add)

cv.waitKey()