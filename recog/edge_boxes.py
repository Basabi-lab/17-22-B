import copy
import numpy as np

class EdgeBoxes:
    white = 255.0
    black = 0.0

    def set_rect(edge, edge_status):
        rected = copy.deepcopy(edge)
        for box in edge_status:
            for x in range(box["min_x"],box["max_x"]):
                rected[box["min_y"]][x] = EdgeBoxes.white
                rected[box["max_y"]][x] = EdgeBoxes.white
            for y in range(box["min_y"],box["max_y"]):
                rected[y][box["min_x"]] = EdgeBoxes.white
                rected[y][box["max_x"]] = EdgeBoxes.white
        return rected

    def sort_box(box_status):
        return sorted(box_status,key=lambda x:x["min_x"])

    def edge_boxes(edge_org):
        edge = copy.deepcopy(edge_org)
        box_status = []
        for i in range(edge.shape[0]):
            for j in range(edge.shape[1]):
                if edge[i][j] == EdgeBoxes.white:
                    box_status = np.append(box_status, {"min_x":j, "min_y":i, "max_x":j, "max_y":i})
                    edge[i][j] = 1
                    EdgeBoxes.edge_box(edge, box_status, i, j)
        return EdgeBoxes.sort_box(box_status)

    # 隣接するedgeを繋げてつながるedgeを加工一つのボックス(1文字)をself.box_statusに入れる
    def edge_box(edge, box_status, first_i, first_j):
        stack = [(first_i, first_j)]
        fix = range(-15,15)
        while stack:
            now_i, now_j = stack.pop()
            for i in fix:
                for j in fix:
                    fixed_i, fixed_j = now_i+i, now_j+j
                    if fixed_i >= 0 and fixed_i < edge.shape[0] and fixed_j >= 0 and fixed_j < edge.shape[1]:
                        # i,jが0なら自分自身を参照するのでスルー and 隣接する色が白ならself.edgeなのでつながるため次を検索
                        if (i != 0 or j != 0) and edge[fixed_i][fixed_j] == EdgeBoxes.white:
                            # 上(値の小さい方)から見ていってるのでmin_yは最初に確定する
                            if box_status[-1]["min_x"] > fixed_j: box_status[-1]["min_x"] = fixed_j
                            if box_status[-1]["max_x"] < fixed_j: box_status[-1]["max_x"] = fixed_j
                            if box_status[-1]["max_y"] < fixed_i: box_status[-1]["max_y"] = fixed_i

                            edge[fixed_i][fixed_j] = 1
                            stack.append((fixed_i, fixed_j))
