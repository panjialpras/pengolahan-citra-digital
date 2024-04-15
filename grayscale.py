import cv2
import numpy as np

# RGB TO GRAYSCALE

# baca gambar dari direktori yang ditentukan
image = cv2.imread("chelsea-rgb.jpg")

# menyimpan channel warna RGB dan menyimpannya ke dalam variabel terpisah
b = image[:,:,0] #menyimpan channel biru
g = image[:,:,1] #menyimpan channel green
r = image[:,:,2] #menyimpan channel red

jum_baris = len(image)
jum_kolom = len(image[0])
image_gray = np.zeros((jum_baris, jum_kolom))

for i in range (jum_baris):
    for h in range (jum_kolom) :
        image_gray[i, h] = round(0.299 * r[i, h] + 0.587 * g[i, h] + 0.114 * b[i, h])

image_gray = image_gray.astype(np.uint8)
print(image_gray)
cv2.imshow("Chelsea grayscale", image_gray)

threshold = 128

for b in range(jum_baris):
    for k in range(jum_kolom) :
        if image_gray[b, k] >= threshold:
            image_gray[b, k] = 1
        else:
            image_gray[b, k] = 0


print(image_gray)

cv2.imshow("Chelsea Bit", image_gray)
cv2.waitKey()

# fungsi cepat
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Chelsea", image_gray)
# cv2.waitKey()
