# -*- coding: utf-8 -*-
import copy
import cv2
import numpy as np
import sys
import urllib

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble  import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn import svm

from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import KFold

from utils.read_datasets import Datasets
from recog.edge_boxes import EdgeBoxes as EdgeBoxes
from recog.image_converter import ImageConverter as ImageConverter
from recog.data_format import DataFormat as DataFormat

seed = 10

class Recog:
    def __init__(self, size):
        self.size = size
        self.train = Datasets(self.size)
        self.generate_model()

    def __eq__(self, other):
        return \
            self.size == other.size and \
            self.train == other.train

    def recog16():
        return Recog("16")

    def recog32():
        return Recog("32")

    def __get_edge_and_box(self, imgpath):
        img = cv2.imread(imgpath, 0)
        edge = cv2.Canny(img, 100, 200)
        edge_status = EdgeBoxes.edge_boxes(edge)
        return edge, edge_status

    def recog(self, imgpath, box_view=False):
        edge, edge_status = self.__get_edge_and_box(imgpath)

        resized = np.array([
            ImageConverter.resize(
                self.__get_box_img(edge, box),
                int(self.size))
            for box in edge_status])
        if box_view == True:
            for processed in resized:
                cv2.imshow("tmp", processed)
                key = cv2.waitKey(0)
                cv2.destroyAllWindows()

        return self.__read_letters(resized)

    def __get_box_img(self, edge, box):
        return edge[box["min_y"]:box["max_y"], box["min_x"]:box["max_x"]]

    def show_letter(self, imgpath):
        edge, edge_status = self.__get_edge_and_box(imgpath)
        rected = EdgeBoxes.set_rect(edge, edge_status)
        cv2.imshow(imgpath, rected)

        key = cv2.waitKey(0)
        cv2.destroyAllWindows()

    def cross_validation(self):
        np.random.seed(seed)

        kf = KFold(n_splits=11, random_state=seed, shuffle=True)

        # model = KNeighborsClassifier(n_neighbors=1)
        # model = RandomForestClassifier(min_samples_leaf=1, max_depth=15, max_features=5, min_samples_split=5, n_estimators=300, n_jobs=1, random_state=seed)
        # model = svm.SVC(kernel="rbf", C=10, gamma=0.001) # 0.8乗った
        # model = GaussianNB(priors=)
        # model = GaussianNB()
        # model = LogisticRegression(C=0.001, solver='newton-cg', random_state=seed)
        # model = GradientBoostingClassifier(random_state=seed)

        # model = GridSearchCV(
        #             GaussianNB(), # 識別器
        #             {"class_count": },
        #             cv=11)

        train, target = copy.deepcopy(self.train.data), copy.deepcopy(self.train.target)

        train[train > 0] = 1.0 # 白いとこが255で黒いとこが0なので、255は1にしたほうが扱い易いので修正
        train = train.astype(np.float64)

        # train = train.reshape((train.shape[0], train.shape[1]*train.shape[2]))

        # train = np.array([DataFormat.framing(d, 8) for d in train])

        train = np.array([DataFormat.row(d) for d in train])

        ## 以下5つは使い物にならない
        # train = np.array([DataFormat.column(d) for d in train])
        # train = np.array([DataFormat.step_row(d, 16) for d in train])
        # train = np.array([DataFormat.step_column(d, 2) for d in train])
        # train = np.array([DataFormat.continuous_row(d, 8) for d in train])
        # train = np.array([DataFormat.continuous_column(d, 2) for d in train])

        # model.fit(train, target)
        # print(model.best_params_)
        # print(model.best_score_)

        scores = np.array([])
        for train_i, test_i in kf.split(train, target):
            model.fit(train[train_i], target[train_i])
            scores = np.append(scores, model.score(train[test_i], target[test_i]))

        # return model.best_score_
        return np.mean(scores)

    def convert(data):
        data[data > 0] = 1.0 # 白いとこが255で黒いとこが0なので、255は1にしたほうが扱い易いので修正
        data = data.astype(np.float64)
        data = np.array([DataFormat.row(d) for d in data])
        # data = np.array([DataFormat.framing(d, 4) for d in data])
        # data = data.reshape((data.shape[0], data.shape[1]*data.shape[2]))
        return data

    def generate_model(self):
        # self.model = KNeighborsClassifier(n_neighbors=1)
        self.model = svm.SVC(kernel="rbf", C=10, gamma=0.001)
        # self.model = RandomForestClassifier(min_samples_leaf=1, max_depth=15, max_features=5, min_samples_split=5, n_estimators=300, n_jobs=1, random_state=seed)
        # self.model = GaussianNB()

        data, target = copy.deepcopy(self.train.data), copy.deepcopy(self.train.target)
        data = Recog.convert(data)

        self.model.fit(data, target)

    def __read_letters(self, letter_imgs):
        test = copy.deepcopy(letter_imgs)
        test = Recog.convert(test)

        return self.model.predict(test)
