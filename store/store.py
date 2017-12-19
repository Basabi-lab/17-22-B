import numpy as np
import pandas as pd

place = np.array(pd.read_csv("datasets/shelf.csv", header=None))
storage=[{}]

for r in range(place.shape[0]-1):
    storage.append({})

class Store():
    # 部品IDと個数を受け取って，場所IDを返す
    def store(self,partId, amount):
        parts = np.array(pd.read_csv("datasets/parts.csv", header=None, sep=","))
        self.partId=partId
        self.amount=amount
        placeId=-1
        #partIdを比較してsizeを出す
        for i in range(len(parts)):
            if partId==parts[i][0]:
                size=parts[i][1]

        #sizeが0ならば
        if size==0:
            #storageの分だけ繰り返す
            for i in range(len(storage)):
                s=sum(storage[i].values())
                #合計とamountを足して10以下ならば
                if s+amount<=10:
                    placeId=i
                    storage[i].update({partId:amount}) #要素を更新
                    return placeId

        elif size==1:
            for i in range(len(storage)-15,len(storage)):
                s=sum(storage[i].values())
                if s+amount<=10:
                    placeId=i
                    storage[i].update({partId:amount})
                    return placeId

        else:
            for i in range(len(storage)-5,len(storage)):
                s=sum(storage[i].values())
                if s+amount<=10:
                    placeId=i
                    storage[i].update({partId:amount})
                    return placeId

    # 場所IDを受け取って，[部品ID,個数]を返す
    def lookup(self,placeId):
        partId=[]
        add=[]
        count=0
        item=storage[placeId].items()
        for i in item:
            partId.append(i[0])
            add.append(i[1])
        count=sum(add)
        return partId,count
