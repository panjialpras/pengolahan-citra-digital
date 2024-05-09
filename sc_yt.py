import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import sys

# baca gambar dari direktori yang ditentukan
image_dir = ("chelsea-rgb.jpg")
image = cv.imread(image_dir)
cv.imshow("RGB", image)

# grayscale
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

    # # crop image
    # crop_image = image[50:100, 30:100]
    # cv.imshow("Cropped Image",crop_image)
        
    # # resize image
    # resize = cv.resize(crop_image, None, fx=2, fy=2)
    # cv.imshow("Resize", resize)

# Flip Image
    # image_flip_horz = cv.flip(image, 1)
    # image_flip_vert = cv.flip(image, 0)
    # image_flip_both = cv.flip(image, -1)
    # plt.figure(figsize=[18, 5])
    # plt.subplot(141);plt.imshow(image_flip_horz);plt.title("Horizontal")
    # plt.subplot(142);plt.imshow(image_flip_vert);plt.title("Vertical")
    # plt.subplot(143);plt.imshow(image_flip_both);plt.title("Both flip")

#  # Anotasi gambar
# Line
imageCopy = image.copy()

    # cv.line(imageCopu, (30, 60), (100, 150), (255, 0, 255), thickness=3, lineType=cv.LINE_AA)
    # cv.imshow("Line", imageCopy)

    # cv.waitKey()

# Cirle
    # cv.circle(imageCopy, (92, 105), 10, (0, 0, 255), thickness=1, lineType=cv.LINE_AA)
    # cv.imshow("Circle",imageCopy)
    # cv.waitKey(0)

# Rectangle
    # cv.rectangle(imageCopy, (30, 50), (100, 90), (0, 0, 255), thickness=2, lineType=cv.LINE_8)
    # cv.imshow("Rectangle", imageCopy)
    # cv.waitKey(0)

# Text
text = "Chelsea Islan"
fontScale = 2
fontFace = cv.FONT_HERSHEY_PLAIN
fontColor = (255, 255, 255)

cv.putText(imageCopy, text, (20, 300), fontFace, fontScale, fontColor, 2, cv.LINE_AA)
cv.imshow("Text",imageCopy)
cv.waitKey(0)

