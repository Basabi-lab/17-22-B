import cv2
import os
import numpy as np

class Resize:
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

    def resize(img, size, padding=True):
        x,y = img.shape[1], img.shape[0]
        padded = None
        if x > y:
            resized = cv2.resize(img,None,fx=size/x, fy=size/x, interpolation = cv2.INTER_AREA)
        else:
            resized = cv2.resize(img,None,fx=size/y, fy=size/y, interpolation = cv2.INTER_AREA)
        if padding == True:
            padded = padding(resized, size)
        else:
            padded = resized

        padded[padded > 0] = 255

        return padded
