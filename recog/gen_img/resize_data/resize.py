import cv2
import os
import numpy as np

dirs = ["0","1","2","3","4","5","6","7","8","9","A","B","C","="]
to_size = [16,32]

def add_zeros(img, size):
    num = int((size-img.shape[0])/2)
    zeros = np.zeros(num*size)
    new_img = np.append(np.append(zeros, img), zeros)

    if new_img.shape != (size*size,):
        new_img = np.append(new_img, np.zeros(size))
    return new_img.reshape((size, size))

def padding(img, size):
    new_img = None

    if img.shape[0] == size:
        new_img = add_zeros(img.T, size).T
    else:
        new_img = add_zeros(img, size)

    return new_img

def resize(dire, imgname, size):
    imgpath = "%s/%s" % (d, imgname)
    img = cv2.imread(imgpath,0)
    x,y = img.shape[1], img.shape[0]
    padded = None
    if x > y:
        resized = cv2.resize(img,None,fx=size/x, fy=size/x, interpolation = cv2.INTER_AREA)
        padded = padding(resized, size)
    else:
        resized = cv2.resize(img,None,fx=size/y, fy=size/y, interpolation = cv2.INTER_AREA)
        padded = padding(resized, size)

    padded[padded > 0] = 255
    cv2.imwrite("%sx%d.png" % (os.path.splitext(imgname)[0], size), padded)
    # key = cv2.waitKey(0)
    # cv2.destroyAllWindows()

for d in dirs:
    for imgpath in os.listdir(d):
        for size in to_size:
            resize(d, imgpath, size)
