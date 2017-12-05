# coding: utf-8

# CHECK: コメントにはWhyを書いてほしみある
# CHECK: 必要ないものは書かない。必要あるときだけあればいい
# CHECK: 変数名は頑張っても良い

import csv # pandasとか使うと楽かも
import numpy as np
import re
import copy

# CHECK: 普通にparts.csvとかじゃだめなの？
#csvファイル読み込み
f1 = open('parts.csv')
reader1 = csv.reader(f1) #部品

f2 = open('place.csv')
reader2 = csv.reader(f2) #場所

parts = [] #部品の配列
place = [] #場所の配列

header = next(reader1)
for row in reader1:
    parts.append(row)

header = next(reader2)
for row in reader2:
    place.append(row)

f1.close()
f2.close()

print("place")
print(np.array(place))
print("parts")
print(np.array(parts))
print()
print()

search = [] # CHECK: 多分検索結果を入れる？
decide = [] # CHECK: 謎の変数 なにこれ
a=0 # CHECK: なにこれ

for i in range(len(parts)):
    flg = 0
    for j in range(len(place)):
        # サイズの比較
        # 棚のサイズと、部品のサイズが一致したら部品を置きたい
        if parts[i][1] == place[j][1]:
            x = int(parts[i][2]) # これから置く部品の量
            y = int(place[j][2]) # 置かれてる部品の量
            z = int(parts[i][3]) # すでに部品が置かれているか
            # 一箇所における数が10個ってどっかで決めてたっけ？
            if x+y <= 10 and z == 0:
                # 在庫の増加
                place[j][2]=x+y
                decide.append(copy.deepcopy(place[j])) # CHECK: なんでdecide追加するの？
                parts[i][3]=place[j][0]
                flg = 1
    if flg == 0:
        print("Miss placing")

        # j += 1 # CHECK: なにこれ？
    # j = 0 # CHECK: なにこれ？

print("place")
print(np.array(place))
print("parts")
print(np.array(parts))
print("decide")
print(np.array(decide))
print("search")
print(np.array(search))

# これは、何のために出力してるの？
# for i in range(len(place)):
#     print(place[i])
# for j in range(len(parts)):
#     print(parts[j])

# TODOとか付けるとかっこいい
# e.g. TODO: CSVファイルを上書き保存
# CSVファイルを上書き保存
# 部品を取り出す場合

