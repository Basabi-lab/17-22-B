# -*- coding: utf-8 -*-
import sys
import cv2
import copy
import numpy as np
import urllib
from ..utils.read_datasets import Datasets
from sklearn.datasets import load_digits

class ImageGenerator:
    def __init__(self, imagepath):
        self.white = 255.0
        self.black = 0.0

        img = cv2.imread(imagepath,0)

        # Canny(image, Low, High)
        # Low  Threathold: Low以下の色はエッジでは無いとして、黒になる(0)
        # High Threathold: High以上の色はエッジであるとして白になる(255)
        canny = cv2.Canny(img,50,200)

        self.box_num = 0
        self.box_status = np.array([])
        self.edge = copy.deepcopy(canny)
        self.edge_boxes()
        self.edge = copy.deepcopy(canny)
        self.set_rect(canny)
        self.gen_edge_img()
        # self.set_rect(img)
        # self.set_rect(canny)
        cv2.imshow('window name',canny)
        # cv2.imwrite('1_edge.png',canny)
        # cv2.imshow('window name',img)
        # cv2.imwrite('1_edge.png',img)
        # self.read_letter()

        print("number of box : ", self.box_num)
        print(self.box_status)

        # キーボード入力を待ってウィンドウを閉じる
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
        print

    def gen_edge_img(self):
        num = 0
        for box in self.box_status:
            box_edge_img = self.edge[box["min_y"]:box["max_y"], box["min_x"]:box["max_x"]]
            cv2.imshow('some', box_edge_img)
            cv2.imwrite('gen_img/%d.png' % (num), box_edge_img)
            num += 1

        print

    def to_digits(self, box_edge):
        box_edge_fixed = np.arange(0,8*8).reshape((8,8))
        for i in range(0, box_edge.shape[0], 4):
           for j in range(0, box_edge.shape[1], 4):
               tmp = 0
               for ii in range(4):
                   for jj in range(4):
                       if box_edge[i+ii][j+jj] == self.white:
                           tmp += 1
               box_edge_fixed[int(i/4)][int(j/4)] = np.float32(tmp)

        return box_edge_fixed

    def read_letter(self):
        model = cv2.ml.KNearest_create()
        # model = cv2.ml.SVM_create()

        train = load_digits()
        data, target = train.data, train.target
        data = data.astype(np.float32)

        retval = model.train(data, cv2.ml.ROW_SAMPLE, target)

        num = 0
        for box in self.box_status:
            box_edge_img = self.edge[box["min_y"]:box["max_y"], box["min_x"]:box["max_x"]]

            # それぞれがどうゆうアルゴリズムなのかは知らん
            box_edge = cv2.resize(box_edge_img,None,fx=32/box_edge_img.shape[1], fy=32/box_edge_img.shape[0], interpolation = cv2.INTER_AREA) # 体感これがいい
            # box_edge = cv2.resize(box_edge_img,None,fx=32/box_edge_img.shape[1], fy=32/box_edge_img.shape[0], interpolation = cv2.INTER_NEAREST)
            # box_edge = cv2.resize(box_edge_img,None,fx=32/box_edge_img.shape[1], fy=32/box_edge_img.shape[0], interpolation = cv2.INTER_LINEAR)
            # box_edge = cv2.resize(box_edge_img,None,fx=32/box_edge_img.shape[1], fy=32/box_edge_img.shape[0], interpolation = cv2.INTER_CUBIC)
            # box_edge = cv2.resize(box_edge_img,None,fx=32/box_edge_img.shape[1], fy=32/box_edge_img.shape[0], interpolation = cv2.INTER_LANCZOS4)
            # box_edge = np.where(box_edge > 0, self.white, self.black)
            box_edge = np.where(box_edge > 16-1, self.white, self.black)

            # 1ボックス(文字)をsklearn.datasetsのdigitsにデータ型を合わせる
            box_edge_fixed = self.to_digits(box_edge)
            box_edge_fixed = box_edge_fixed.astype(np.float32).flatten()
            # print(box_edge_fixed)

            # retval, results, neigh_resp, dists = model.findNearest(np.array([box_edge_fixed]), k = 11) # KNN
            retval, results, neigh_resp, dists = model.findNearest(np.array([box_edge_fixed]), k = 3) # KNN

            print(box_edge_fixed)
            print(neigh_resp)
            print(results)
            # sampleMat = np.array([[j, i]], np.float32)

            # response = model.predict(np.array([box_edge_fixed])) # SVM
            # print(response)

            cv2.imshow('some', box_edge_img)
            cv2.imwrite('edges.png', box_edge_img)
            key = cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imshow('some', box_edge)
            cv2.imwrite('gen_img/%d.png' % (num), box_edge)
            key = cv2.waitKey(0)
            cv2.destroyAllWindows()

            num += 1
        print

    def set_rect(self, edge):
        for rect in self.box_status:
            for i in range(rect["min_y"], rect["max_y"]+1):
                print(i)
                edge[i][rect["min_x"]] = self.white
                edge[i][rect["max_x"]] = self.white
            for j in range(rect["min_x"], rect["max_x"]+1):
                print(j)
                edge[rect["min_y"]][j] = self.white
                edge[rect["max_y"]][j] = self.white

    def edge_boxes(self):
        for i in range(self.edge.shape[0]):
            for j in range(self.edge.shape[1]):
                if self.edge[i][j] == self.white:
                    self.box_status = np.append(self.box_status, {"min_x":j, "min_y":i, "max_x":j, "max_y":i})
                    self.edge[i][j] = 1
                    self.edge_box(i, j)
                    self.box_num += 1

    # 隣接するedgeを繋げてつながるedgeを加工一つのボックス(1文字)をself.box_statusに入れる
    def edge_box(self, first_i, first_j):
        stack = [(first_i, first_j)]
        # fix = range(-4,4)
        # fix = range(-10,10)
        fix = range(-12,12)
        # fix = range(-23,23)
        while stack:
            now_i, now_j = stack.pop()
            for i in fix:
                for j in fix:
                    fixed_i, fixed_j = now_i+i, now_j+j
                    if fixed_i >= 0 and fixed_i < self.edge.shape[0] and fixed_j >= 0 and fixed_j < self.edge.shape[1]:
                        # i,jが0なら自分自身を参照するのでスルー and 隣接する色が白ならself.edgeなのでつながるため次を検索
                        if (i != 0 or j != 0) and self.edge[fixed_i][fixed_j] == self.white:
                            # 上(値の小さい方)から見ていってるのでmin_yは最初に確定する
                            if self.box_status[self.box_num]["min_x"] > fixed_j: self.box_status[self.box_num]["min_x"] = fixed_j
                            if self.box_status[self.box_num]["max_x"] < fixed_j: self.box_status[self.box_num]["max_x"] = fixed_j
                            if self.box_status[self.box_num]["max_y"] < fixed_i: self.box_status[self.box_num]["max_y"] = fixed_i

                            self.edge[fixed_i][fixed_j] = 1
                            stack.append((fixed_i, fixed_j))

if __name__ == "__main__":
    # ins = ImageGenerator("datasets/white5.jpg")
    ins = ImageGenerator("src/train9.jpg")

