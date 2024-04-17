# import cv2 as cv
# import numpy as np
# from tqdm import tqdm
# from responsi import *

# jum_baris = len(cit_n_bg[:])
# jum_kolom = len(cit_n_bg[0, :])

# citra_flipping = np.zeros((jum_baris, jum_kolom, 3))

# flip_vertical = 0
# flip_horizontal = 1

# for brs in range(jum_baris):
#     for klm in range(jum_kolom):
        
#         if (flip_horizontal == 1) :
#             kolom_baru = (jum_kolom - 1) - klm
#         else:
#             kolom_baru = klm
        
#         if (flip_vertical == 1):
#             baris_baru = (jum_baris - 1) - brs
#         else:
#             baris_baru = brs

#         citra_flipping[baris_baru, kolom_baru] = cit_n_bg[brs, klm]

# citra_flipping = citra_flipping.astype(np.uint8)
# cv.imshow("Flip", citra_flipping)

# b1 = citra_flipping[:,:,0]
# g1 = citra_flipping[:,:,1]
# r1 = citra_flipping[:,:,2]

# b2 = bg_rsz[:,:,0]
# g2 = bg_rsz[:,:,1]
# r2 = bg_rsz[:,:,2]

# jum_baris = len(cit_n_bg[:])
# jum_kolom = len(cit_n_bg[0, :])

# citra_gabung = np.zeros((jum_baris, jum_kolom, 3))

# for i in range(jum_baris):
#     for j in range(jum_kolom):
#         citra_gabung[i, j, 0] = int(b1[i, j] + int(b2[i, j]))
#         citra_gabung[i, j, 1] = int(g1[i, j] + int(g2[i, j]))
#         citra_gabung[i, j, 2] = int(r1[i, j] + int(r2[i, j]))
        
#         if (citra_gabung[i, j, 0]) > 255:
#             citra_gabung[i, j, 0] = 255
            
#         if (citra_gabung[i, j, 1]) > 255:
#             citra_gabung[i, j, 1] = 255
            
#         if (citra_gabung[i, j, 2]) > 255:
#             citra_gabung[i,++ j, 2] = 255

# citra_gabung = citra_gabung.astype(np.uint8)

# cv.imshow("Add" ,citra_gabung)
# cv.waitKey()



def gnt_bg (citra,latar):
    print("a")
    wdh = np.zeros((jum_baris_baru,jum_kolom_baru,3))
    
    for ab in range(jum_baris_baru):
        for bc in range(jum_kolom_baru):
            if citra[ab,bc,2] in range(0,1) :
                if citra[ab,bc,1] in range(0,1) :
                    if citra[ab,bc,0] in range(0,1) :
                        wdh[ab,bc,2] = latar[ab,bc,2]
                        wdh[ab,bc,1] = latar[ab,bc,1]
                        wdh[ab,bc,0] = latar[ab,bc,0]
                    else:
                        wdh[ab,bc,2] = citra[ab,bc,2]
                        wdh[ab,bc,1] = citra[ab,bc,1]
                        wdh[ab,bc,0] = citra[ab,bc,0]    
                else:
                    wdh[ab,bc,2] = citra[ab,bc,2]
                    wdh[ab,bc,1] = citra[ab,bc,1]
                    wdh[ab,bc,0] = citra[ab,bc,0]    
            else:
                wdh[ab,bc,2] = citra[ab,bc,2]
                wdh[ab,bc,1] = citra[ab,bc,1]
                wdh[ab,bc,0] = citra[ab,bc,0]
    
    for brs_baru in range(jum_baris_baru):
        for klm_baru in range(jum_kolom_baru):
            cit_total[brs_baru, klm_baru] = wdh[brs_baru, klm_baru]