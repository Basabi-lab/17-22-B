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
from utils.resize import Resize
from recog.edge_boxes import EdgeBoxes
from recog.data_format import DataFormat

seed = 10

class RecogTrainer:
    def __init__(self, size):
        self.size = size
        self.train = Datasets(self.size)
        self.model = None

    def training(self, model_name="KNN", extract_name="all"):
        model, extract = self.strategy(model_name, extract_name)

        data, target = copy.deepcopy(self.train.data), copy.deepcopy(self.train.target)
        data = self.pre(data)
        data = extract(data)

        model.fit(data, target)
        self.model = model
        return self

    def grid_search(self):
        train, target = copy.deepcopy(self.train.data), copy.deepcopy(self.train.target)

        model = GridSearchCV(
                    GaussianNB(), # 識別器
                    {"class_count": 13},
                    cv=11)

        model.fit(train, target)
        print(model.best_params_)
        print(model.best_score_)

        return model.best_score_

    def model_strategy(self, model_name="KNN"):
        model = None
        if model_name == "KNN":
            model = KNeighborsClassifier(n_neighbors=1)
        elif model_name == "RFC":
            model = RandomForestClassifier(min_samples_leaf=1,max_depth=15,max_features=5,min_samples_split=5,n_estimators=300,n_jobs=1,random_state=seed)
        elif model_name == "SVM":
            model = svm.SVC(kernel="rbf", C=10, gamma=0.001)
            # model = svm.SVC(kernel="poly",C=1000,gamma=0.001,degree=2)
        elif model_name == "GNB":
            model = GaussianNB()
        elif model_name == "LR":
            model = LogisticRegression(C=0.001,solver='newton-cg',random_state=seed)
        elif model_name == "GBC":
            model = GradientBoostingClassifier(random_state=seed)
        else:
            model = KNeighborsClassifier(n_neighbors=1)
        return model

    def extract_strategy(self, extract_name="all"):
        extract = None
        if extract_name == "all":
            extract = lambda train: train.reshape((train.shape[0], train.shape[1]*train.shape[2]))
        elif extract_name == "frame4":
            extract = lambda train: np.array([DataFormat.framing(d, 4) for d in train])
        elif extract_name == "frame8":
            extract = lambda train: np.array([DataFormat.framing(d, 8) for d in train])
        elif extract_name == "row":
            extract = lambda train: np.array([DataFormat.row(d) for d in train])
        else:
            extract = lambda train: train.reshape((train.shape[0], train.shape[1]*train.shape[2]))
        return extract

    def pre(self, data):
        ddata = copy.deepcopy(data)
        ddata[ddata > 0] = 1.0 # 白いとこが255で黒いとこが0なので、255は1にしたほうが扱い易いので修正
        return ddata.astype(np.float64)

    def cross_validation(self, model_name="KNN", extract_name="all"):
        kf = KFold(n_splits=11, random_state=seed, shuffle=True)

        model, extract = self.strategy(model_name, extract_name)

        train, target = copy.deepcopy(self.train.data), copy.deepcopy(self.train.target)

        train = self.pre(train)
        train = extract(train)

        scores = np.array([])
        for train_i, test_i in kf.split(train, target):
            model.fit(train[train_i], target[train_i])
            scores = np.append(scores, model.score(train[test_i], target[test_i]))

        return np.mean(scores)

    def strategy(self, model_name="KNN", extract_name="all"):
        return self.model_strategy(model_name), self.extract_strategy(extract_name)

    def convert(self, data):
        _, extract = self.strategy()
        data = self.pre(data)

        return extract(data)

    def generate_model(self):
        model, extract = self.strategy()

        data, target = copy.deepcopy(self.train.data), copy.deepcopy(self.train.target)
        data = extract(data)

        model.fit(data, target)
        return model


class Recog(RecogTrainer):
    def __init__(self, size):
        np.random.seed(seed)
        super(Recog, self).__init__(size)

    def __eq__(self, other):
        return \
            self.size == other.size and \
            self.train == other.train and \
            self.model == other.model

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
            Resize.resize(
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

    def grid_search(self):
        train, target = copy.deepcopy(self.train.data), copy.deepcopy(self.train.target)

        model = GridSearchCV(
                    GaussianNB(), # 識別器
                    {"class_count": 13},
                    cv=11)

        model.fit(train, target)
        print(model.best_params_)
        print(model.best_score_)

        return model.best_score_

    def __read_letters(self, letter_imgs):
        test = copy.deepcopy(letter_imgs)
        test = self.convert(test)

        return self.model.predict(test)
