import csv
import random as rnd

size_num = [20,10,5]
tag  = [0,1,2] # 小 中 大

with open('shelf.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows([[tag[i]] for i in range(len(tag)) for _ in range(size_num[i])])

part_char = ["A", "B", "C"]
part_num  = 999

with open('parts.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows([["%s%03d" % (pc, i), rnd.choice(tag)] for pc in part_char for i in range(part_num)])

