import cv2
import numpy as np
import matplotlib as plt
from tqdm import tqdm


def flip(citra, latar):
    print("a")
    global cit_n_bg

    jum_baris = len(citra[:])
    jum_kolom = len(citra[0, :])

    citra_flipping = np.zeros((jum_baris, jum_kolom, 3))

    flip_vertical = 0
    flip_horizontal = 1

    for brs in range(jum_baris):
        for klm in range(jum_kolom):

            if (flip_horizontal == 1):
                kolom_baru = (jum_kolom - 1) - klm
            else:
                kolom_baru = klm

            if (flip_vertical == 1):
                baris_baru = (jum_baris - 1) - brs
            else:
                baris_baru = brs

            citra_flipping[baris_baru, kolom_baru] = citra[brs, klm]

    change_flip = np.zeros((jum_baris_baru, jum_kolom_baru, 3))

    for inc in range(jum_baris_baru):
        for anc in range(jum_kolom_baru):
            if citra_flipping[inc, anc, 2] in range(0, 1):
                if citra_flipping[inc, anc, 1] in range(0, 1):
                    if citra_flipping[inc, anc, 0] in range(0, 1):
                        change_flip[inc, anc, 2] = latar[inc, anc, 2]
                        change_flip[inc, anc, 1] = latar[inc, anc, 1]
                        change_flip[inc, anc, 0] = latar[inc, anc, 0]
                    else:
                        change_flip[inc, anc, 2] = citra_flipping[inc, anc, 2]
                        change_flip[inc, anc, 1] = citra_flipping[inc, anc, 1]
                        change_flip[inc, anc, 0] = citra_flipping[inc, anc, 0]
                else:
                    change_flip[inc, anc, 2] = citra_flipping[inc, anc, 2]
                    change_flip[inc, anc, 1] = citra_flipping[inc, anc, 1]
                    change_flip[inc, anc, 0] = citra_flipping[inc, anc, 0]
            else:
                change_flip[inc, anc, 2] = citra_flipping[inc, anc, 2]
                change_flip[inc, anc, 1] = citra_flipping[inc, anc, 1]
                change_flip[inc, anc, 0] = citra_flipping[inc, anc, 0]

    for baris_baru in range(jum_baris_baru):
        for kolom_baru in range(jum_kolom_baru):
            cit_total[baris_baru,
                      kolom_baru] = change_flip[baris_baru, kolom_baru]


def bg_ijo(citra):
    print("\na")
    # rgba(85,168,112,255) - green
    r = range(12, 62)
    g = range(214, 255)
    b = range(0, 40)
    for brs in tqdm(range(jm_brs)):
        for klm in range(jm_klm):
            if citra[brs, klm, 2] in r:
                if citra[brs, klm, 1] in g:
                    if citra[brs, klm, 0] in b:
                        cit_n_bg[brs, klm] = 0
                    else:
                        cit_n_bg[brs, klm] = citra1[brs, klm]
                else:
                    cit_n_bg[brs, klm] = citra1[brs, klm]
            else:
                cit_n_bg[brs, klm] = citra1[brs, klm]
    return cit_n_bg

    # if citra[brs,klm,2] not in range(30,135,1) and citra[brs,klm,1] not in range(100,255,1) and citra[brs,klm,0] not in range(25,165,1):
    #    cit_n_bg[brs,klm] = citra[brs,klm]
    # if np.array_equal(citra,rgb):
    #    cit_n_bg[brs,klm,0] = 0
    #    cit_n_bg[brs,klm,1] = 0
    #    cit_n_bg[brs,klm,2] = 0
    # else:
    #    cit_n_bg[brs,klm,0] = citra[brs,klm,0] + cit_n_bg[brs,klm,0]
    #    cit_n_bg[brs,klm,1] = citra[brs,klm,1] + cit_n_bg[brs,klm,1]
    #    cit_n_bg[brs,klm,2] = citra[brs,klm,2] + cit_n_bg[brs,klm,2]


def resize(citra, latar):
    print("a")

    faktor_skala_brs = jm_brs / jm_brs_ltr
    faktor_skala_klm = jm_klm / jm_klm_ltr

    wdh = np.zeros((jm_brs_ltr, jm_klm_ltr, 3))

    global jum_baris_baru
    global jum_kolom_baru
    jum_baris_baru = round(faktor_skala_brs * jm_brs_ltr)
    jum_kolom_baru = round(faktor_skala_klm * jm_klm_ltr)

    global bg_rsz
    bg_rsz = np.zeros((jum_baris_baru, jum_kolom_baru, 3))

    for brs_baru in range(jum_baris_baru):
        for klm_baru in range(jum_kolom_baru):
            # cek posisi brs dan klm pixel pada citra awal
            brs = int(brs_baru / faktor_skala_brs)
            klm = int(klm_baru / faktor_skala_klm)

            # isi pixel pada citra baru (citra skala)
            wdh[brs_baru, klm_baru] = latar[brs, klm]
            bg_rsz[brs_baru, klm_baru] = wdh[brs_baru, klm_baru]


def gnt_bg(citra, latar):
    print("a")
    wdh = np.zeros((jum_baris_baru, jum_kolom_baru, 3))

    for ab in range(jum_baris_baru):
        for bc in range(jum_kolom_baru):
            if citra[ab, bc, 2] in range(0, 1):
                if citra[ab, bc, 1] in range(0, 1):
                    if citra[ab, bc, 0] in range(0, 1):
                        wdh[ab, bc, 2] = latar[ab, bc, 2]
                        wdh[ab, bc, 1] = latar[ab, bc, 1]
                        wdh[ab, bc, 0] = latar[ab, bc, 0]
                    else:
                        wdh[ab, bc, 2] = citra[ab, bc, 2]
                        wdh[ab, bc, 1] = citra[ab, bc, 1]
                        wdh[ab, bc, 0] = citra[ab, bc, 0]
                else:
                    wdh[ab, bc, 2] = citra[ab, bc, 2]
                    wdh[ab, bc, 1] = citra[ab, bc, 1]
                    wdh[ab, bc, 0] = citra[ab, bc, 0]
            else:
                wdh[ab, bc, 2] = citra[ab, bc, 2]
                wdh[ab, bc, 1] = citra[ab, bc, 1]
                wdh[ab, bc, 0] = citra[ab, bc, 0]

    for brs_baru in range(jum_baris_baru):
        for klm_baru in range(jum_kolom_baru):
            cit_total[brs_baru, klm_baru] = wdh[brs_baru, klm_baru]


citra1 = cv2.imread(
    "1.jpeg")
citra2 = cv2.imread(
    "latar1.jpg")

jm_brs = len(citra1[:])
jm_klm = len(citra1[0, :])
jm_brs_ltr = len(citra2[:])
jm_klm_ltr = len(citra2[0, :])


b1 = citra1[:, :, 0]
g1 = citra1[:, :, 1]
r1 = citra1[:, :, 2]

cit_n_bg = np.zeros((jm_brs, jm_klm, 3))

bg_ijo(citra1)
cit_n_bg = cit_n_bg.astype(np.uint8)
cv2.imshow("Citra bg ilang", cit_n_bg)

resize(citra1, citra2)
bg_rsz = bg_rsz.astype(np.uint8)
cv2.imshow("Background Resize", bg_rsz)
cit_total = np.zeros((jum_baris_baru, jum_kolom_baru, 3))

gnt_bg(cit_n_bg, bg_rsz)
cit_total = cit_total.astype(np.uint8)
cv2.imshow("Citra akhir", cit_total)

flip(cit_n_bg, bg_rsz)
cit_total = cit_total.astype(np.uint8)
cv2.imshow("Object Flip", cit_total)

# flip(cit_total)


print("Proses Selesai")
cv2.imshow("Citra awal", citra1)
cv2.waitKey()
