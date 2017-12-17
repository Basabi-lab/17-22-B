storage = []#在庫を管理する配列

class Store():
    def store(self, partId, amount):
        # 部品IDと個数を受け取って，場所IDを返す

        for i in storage:
            for j in i:
                if j == partId:#入力した部品idが在庫にある時
                    pass

    def lookup(self, placeId):
        # 場所IDを受け取って，[部品ID,個数]を返す
        pass
