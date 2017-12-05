import cv2
import numpy as np

class ImageConverter:
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
            new_img = ImageConverter.add_zeros(img.T, size).T
        else:
            new_img = ImageConverter.add_zeros(img, size)
        return new_img

    def resize(img, size):
        x,y = img.shape[1], img.shape[0]
        padded = None
        if x > y:
            resized = cv2.resize(img,None,fx=size/x, fy=size/x, interpolation = cv2.INTER_AREA)
            padded = ImageConverter.padding(resized, size)
        else:
            resized = cv2.resize(img,None,fx=size/y, fy=size/y, interpolation = cv2.INTER_AREA)
            padded = ImageConverter.padding(resized, size)
        return padded
