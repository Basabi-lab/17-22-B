import glob
import cv2
import numpy as np
from utils.utils import Utils as Utils

class Datasets:
    def __init__(self, size):
        self.__size = size
        self.__prefix = "datasets/train_raw_data"
        self.__target_names = np.array(["0","1","2","3","4","5","6","7","8","9","A","B","C","="])
        self.__target,self.__data = self.__load_target_and_data()

    @property
    def target(self):
        return self.__target

    @property
    def target_names(self):
        return self.__target_names

    @property
    def data(self):
        return self.__data

    @property
    def size(self):
        return self.__size

    def __eq__(self, other):
        return \
            Utils.nparray_eq(self.target,       other.target)       and \
            Utils.nparray_eq(self.target_names, other.target_names) and \
            Utils.nparray_eq(self.data,         other.data)         and \
            self.size == other.size

    def __load_target_and_data(self):
        data   = []
        target = []
        for letter in self.__target_names:
            for letter_imgpath in glob.glob("%s/%s/%s*" % (self.__prefix, self.__size, letter)):
                data.append(cv2.imread(letter_imgpath, 0))
                target.append(letter)
        return np.array(target), np.array(data)

    def load_16():
        return Datasets("16")

    def load_32():
        return Datasets("32")
