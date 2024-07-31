import rerun as rr

from typing import List
import numpy as np

import leetcode_rerun.rr_helpers as rrh


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rrh.log_mat("/", matrix)
        # return
        rows = [m[0] for m in matrix]

        row = self.search_lin(rows, target)
        print("row", row)
        rrh.log_list("row", matrix[row])
        if matrix[row][0] == target:
            return True
        col = self.search_lin(matrix[row], target)
        print("col", col)
        rrh.log_list("col", row)

        if matrix[row][col] == target:
            return True

        return False

    def search_lin(self, lst, target):
        left = 0
        right = len(lst) - 1

        i = 0

        print(lst)
        while left <= right:
            i += 1
            piv = (left + right) // 2
            val = lst[piv]

            disp = [np.nan] * len(lst)
            disp[left] = -1
            disp[piv] = 0
            disp[right] = 1

            rrh.log_list("", lst)

            print("left", left)
            print("piv", piv)
            print("right", right)
            print("val", val)
            if val == target:
                print("found index", piv)
                return piv
            if val < target:
                print("val < target")
                left = piv + 1
            else:
                print("val > target")
                right = piv - 1
        print("not in array")
        print("left", left)
        print("piv", piv)
        print("right", right)
        print("val", val)
        return right


if __name__ == "__main__":
    rr.init("mat", spawn=True)
    mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    Solution().searchMatrix(mat, 3)
