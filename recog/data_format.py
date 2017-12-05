import numpy as np

class DataFormat:
    def framing(img, frame):
        shape = img.shape
        data = np.array([])
        for i in range(frame):
            for j in range(frame):
                # data = np.append(data, np.where(img[i*frame:(i+1)*frame, j*fram:(j+1)*frame] > 0)[0].shape[0])
                data = np.append(data, np.count_nonzero(img[i*frame:(i+1)*frame, j*frame:(j+1)*frame]))
        return data

    def column(img):
        data = np.array([])
        for col in range(img.shape[1]):
            data = np.append(data, np.count_nonzero(img[:,col]))
        return data

    def row(img):
        data = np.array([])
        for row in range(img.shape[0]):
            data = np.append(data, np.count_nonzero(img[row]))
        return data

    def step_column(img, step):
        data = np.array([])
        for col in range(step):
            data = np.append(data, np.count_nonzero(img[:, col::step]))
        return data

    def step_row(img, step):
        data = np.array([])
        for row in range(step):
            data = np.append(data, np.count_nonzero(img[row::step]))
        return data

    def continuous_column(img, cont):
        data = np.array([])
        for col in range(0, img.shape[1], cont):
            data = np.append(data, np.count_nonzero(img[:, col:(col+cont)]))
        return data

    def continuous_row(img, cont):
        data = np.array([])
        for row in range(0, img.shape[0], cont):
            data = np.append(data, np.count_nonzero(img[row:(row+cont)]))
        return data
