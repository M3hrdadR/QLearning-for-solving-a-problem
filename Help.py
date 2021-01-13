from typing import *
import sys
sys.setrecursionlimit(1500)

# Constants
Right = 0
Left = 1
UP = 2
Down = 3

alpha = 0.5
gamma = 0.9
start = [0, 0, 0, 1, 0, 1, 1, 2, 1]
final = [2, 1, 0, 1, 0, 1, 0, 1, 0]



class Help:

    def k_sub_set(self, k: int, n: int)-> List[List[int]]:
        if k > n:
            lst = []
            return lst
        if k == 1:
            lst = []
            list1 = []
            for i in range(n):
                lst.append(0)
            for i in range(n):
                lst[i] = 1
                list1.append(lst.copy())
                lst[i] = 0
        else:
            list1 = []
            lst = self.k_sub_set(k-1, n)
            for tmp in lst:
                index = tmp.index(1)
                for j in range(0, index):
                    a = tmp.copy()
                    a[j] = 1
                    list1.append(a)
        return list1
