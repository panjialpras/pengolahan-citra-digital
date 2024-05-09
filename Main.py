import cv2 as cv
import numpy as np
from tubes import *

citra2 = cv.imread("latar1.jpg")
b1 = citra1[:,:,0]
g1 = citra1[:,:,1]
r1 = citra1[:,:,2]

b2 = citra2[:,:,0]
g2 = citra2[:,:,1]
r2 = citra2[:,:,2]

jm_brs = len(citra2[:])
jm_klm = len(citra2[0,:])
faktor_skala = 0.2      #faktor skala > 1: zoom in, faktor skala < 1: zoom out

#buat matrix zero untuk menampung gambar hasil translasi
jum_baris_baru = round(faktor_skala * jm_brs)
jum_kolom_baru = round(faktor_skala * jm_klm)
citra_skala = np.zeros((jum_baris_baru, jum_kolom_baru, 3))      #angka 3 menyatakan 3 channel RGB

for brs_baru in range(jum_baris_baru):
    for klm_baru in range(jum_kolom_baru):
        #cek posisi brs dan klm pixel pada citra awal
        brs = int(brs_baru / faktor_skala)
        klm = int(klm_baru / faktor_skala)

        #isi pixel pada citra baru (citra skala)
        citra_skala[brs_baru, klm_baru] = citra2[brs, klm]
jum_baris = len(citra1)
jum_kolom = len(citra1[0])

#menyiapkan citra baru dengan nilai 0
citra_addition = np.zeros((jum_baris, jum_kolom, 3))

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_addition[i, j, 0] = int(b1[i, j]) + int(b2[i, j])
        citra_addition[i, j, 1] = int(g1[i, j]) + int(g2[i, j])
        citra_addition[i, j, 2] = int(r1[i, j]) + int(r2[i, j])

        # revisi nilai pixel jika > 255
        if (citra_addition[i, j, 0] > 255): 
            citra_addition[i, j, 0] = 255
        
        if (citra_addition[i, j, 1] > 255): 
            citra_addition[i, j, 1] = 255

        if (citra_addition[i, j, 2] > 255): 
            citra_addition[i,++ j, 2] = 255

citra_addition = citra_addition.astype(np.uint8)
citra_skala = citra_skala.astype(np.uint8)
cv.imshow("Resize", citra_skala)
cv.imshow("Gabung", citra_addition)
cv.waitKey()
