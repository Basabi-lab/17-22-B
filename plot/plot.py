from matplotlib import pyplot as plt
import numpy as np

# 画像の読み込み
img = np.array( Image.open('tana.png') )

#画像サイズの取得
hsize = img.shape[0]
wsize = img.shape[1]

#点のサイズ変更
size = 10

x=0
var=p_list[x]

class Drawing:
    def __init__(self):
        self.p_list =[(600,32),(600,96),(600,160),(600,224),(600,288),(600,352),(600,416),(600,480),(600,544),(600,608),(600,672),(600,736),(600,800),(600,864),(600,928),(600,992),(600,1056),(600,1120),(600,1184),(600,1248),
         (360,64),(360,192),(360,320),(360,448),(360,576),(360,704),(360,832),(360,960),(360,1088),(360,1216),
         (130,128),(130,384),(130,640),(130,896),(130,1152)]

    def plot(self, var):
        #エラー処理＆点の表示

        for i in
        var　=　self.p_list[x]
        if wsize>var[0] or hsize>var[1]:
            for r in range(var[0]-size, var[0]+size):
                for g in range(var[1]-size, var[1]+size):
                    for b in range(0,3):
                        img[r][g][b] = 0

        else:
            print("エラー! 入力を確認してください")

drawing = Drawing()
drawing.plot(p_list[x])

# 画像の表示
plt.figure(figsize=(16,9))
plt.imshow(img)#, aspect='auto')


