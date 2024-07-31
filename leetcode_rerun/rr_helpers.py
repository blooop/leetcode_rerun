import rerun as rr
from typing import List, Any
from collections.abc import Iterable

def log_mat(path: str, matrix: List[List[Any]]):
    points = []
    labels = []
    for i in range(len(matrix)):        
        for j in range(len(matrix[i])):
            points.append((i, j))
            labels.append(matrix[i][j])
    rr.log(f"{path}/data", rr.Points2D(points, labels=labels))
    rr.log(path, rr.Boxes2D(centers=points, sizes=[1, 1] * len(points)))


def log_list(path: str, lst: List[Any], ptr_list: List[int] = None):
    if isinstance(lst,Iterable):
        points = list(range(len(lst)))
        rr.log(f"{path}/data", rr.Points2D(points, labels=lst))
        rr.log(path, rr.Boxes2D(centers=points, sizes=[1, 1] * len(lst)))


        if ptr_list is not None:
            
            rr.log(f"{path}", rr.Boxes2D(centers=points, sizes=[1, 1] * len(lst)),labels=ptr_list)


    # if ptr_list is not None:
        # rr.log(f"{path}/ptrs",rr.Arrows2D(vectors=[0,-1]*len(lst)))
