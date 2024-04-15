from PIL.Image import linear_gradient
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# baca gambar dari direktori yang ditentukan
image_dir = ("D:/Berkas Penting/Tugas Kuliah/Code/Py/image processing/chelsea-rgb.jpg")
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

# Resize
#   small_image = cv.resize(image,(100, 200), interpolation=cv.INTER_CUBIC)
#   plt.imshow(small_image)

#   plt.waitforbuttonpress(0)

# Rotasi
    # rows, cols = image.shape[:2]
    # M = cv.getRotationMatrix2D((cols/2,rows/2),10,1) 
    # dst = cv.warpAffine(image,M,(cols,rows)) 
    # plt.imshow(dst)
    # plt.waitforbuttonpress(0)
    
# Translasi
    # M = cv.getRotationMatrix2D((cols/2,rows/2),90,1) 
    # dst = cv.warpAffine(image,M,(cols,rows)) 
    # plt.imshow(dst)

# Advance thresholding
    # ret,thresh_global = cv.threshold(image_gray,127,255,cv.THRESH_BINARY)
    # #here 11 is the pixel neighbourhood that is used to calculate the threshold value
    # thresh_mean = cv.adaptiveThreshold(image_gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

    # thresh_gaussian = cv.adaptiveThreshold(image_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

    # names = ['Original Image','Global Thresholding','Adaptive Mean Threshold','Adaptive Gaussian Thresholding']
    # images = [image_gray,thresh_global,thresh_mean,thresh_gaussian]

    # for i in range(4):
    #     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    #     plt.title(names[i])
    #     plt.xticks([]),plt.yticks([])
        
    # plt.show()

# Image Segmentation

# apply thresholding
    # ret,thresh = cv.threshold(image_gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    #get a kernel
    # kernel = np.ones((3,3),np.uint8)
    # opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel,iterations = 2)
    #extract the background from image
    # sure_bg = cv.dilate(opening,kernel,iterations = 3)

    # dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
    # ret,sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # sure_fg = np.uint8(sure_fg)
    # unknown = cv.subtract(sure_bg,sure_bg)

    # ret,markers = cv.connectedComponents(sure_fg)

    # markers = markers+1

    # markers[unknown==255] = 0

    # markers = cv.watershed(image,markers)
    # image[markers==-1] = [255,0,0]

    # plt.imshow(sure_fg)

    # plt.waitforbuttonpress(0)
    
# Edge Detection
    # edges = cv.Canny(image_gray, 128, 200)
    # plt.imshow(edges)
    # plt.waitforbuttonpress(0)   

#converting RGB image to Binary 