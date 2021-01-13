from typing import *
from Help import *
import random

# 0 is sun
# 1 is moon
# 2 is blank

# Right = 0
# Left = 1
# UP = 2
# Down = 3


class RL:
    def __init__(self):
        list1 = list()
        help = Help()
        lst = help.k_sub_set(4, 8)
        for i in range(9):
            for tmp in lst:
                a = tmp.copy()
                a.insert(i, 2)
                list1.append(a)
        self.table = self.MakingTable(list1)
        return

    def Print(self):
        for x in self.table:
            for a in self.table[x]['order']:
                if a == 0:
                    print("s", end=" ")
                if a == 1:
                    print("m", end=" ")
                if a == 2:
                    print("b", end=" ")
            print(" | ", end="")
            for a in self.table[x]['actions']:
                if a == 0:
                    print("Right :", self.table[x]['actions'][a], end=" | ")
                if a == 1:
                    print("Left :", self.table[x]['actions'][a], end=" | ")
                if a == 2:
                    print("Up :", self.table[x]['actions'][a], end=" | ")
                if a == 3:
                    print("Down :", self.table[x]['actions'][a], end=" | ")
            print("State number:", self.table[x]['no'])
        return

    def Episode(self, table: Dict)-> List[Tuple]:
        list1 = list()
        num = random.randint(0, len(table) - 1)
        for x in table:
            if table[x]['no'] == num:
                code = self.Coding(table[x]['order'])
                break
        current_state = code
        for i in range(31):
            direction = random.randint(0, 3)
            while table[current_state]['actions'][direction] == -1000:
                direction = random.randint(0, 3)
            tuple1 = (current_state, direction)
            list1.append(tuple1)
            current_state = self.Transition(current_state, direction)
        return list1

    def Coding(self, lst: List[int])-> int:
        tmp = lst.copy()
        num = pow(2, tmp.index(2)) * pow(11, tmp.index(1))
        tmp[tmp.index(1)] = 3
        num *= pow(7, tmp.index(1))
        tmp[tmp.index(1)] = 3
        num *= pow(5, tmp.index(1))
        tmp[tmp.index(1)] = 3
        num *= pow(3, tmp.index(1))
        tmp[tmp.index(1)] = 3
        return num

    def MakingTable(self, list_of_initial_states: List[List[int]])-> Dict:
        dict1 = dict()
        for i in range(len(list_of_initial_states)):
            code = self.Coding(list_of_initial_states[i])
            dict1[code] = dict()
            dict1[code]["order"] = list_of_initial_states[i]
            dict1[code]["actions"] = dict()
            dict1[code]["actions"][Right] = 0
            dict1[code]["actions"][Left] = 0
            dict1[code]["actions"][UP] = 0
            dict1[code]["actions"][Down] = 0
            dict1[code]["r"] = 0
            dict1[code]["no"] = i
            index = list_of_initial_states[i].index(2)
            if index <= 2:
                dict1[code]["actions"][UP] = -1000
            if index >= 6:
                dict1[code]["actions"][Down] = -1000
            if index % 3 == 0:
                dict1[code]["actions"][Left] = -1000
            if index % 3 == 2:
                dict1[code]["actions"][Right] = -1000
        dict1[self.Coding(final)]['r'] = 100
        return dict1

    def Transition(self, state: int, action: int)-> int:
        initial = self.table[state]
        lst = initial["order"].copy()
        blank_index = lst.index(2)
        if action == UP:
            lst[blank_index] = lst[blank_index - 3]
            lst[blank_index-3] = 2
        if action == Down:
            lst[blank_index] = lst[blank_index + 3]
            lst[blank_index + 3] = 2
        if action == Left:
            lst[blank_index] = lst[blank_index - 1]
            lst[blank_index - 1] = 2
        if action == Right:
            lst[blank_index] = lst[blank_index + 1]
            lst[blank_index + 1] = 2
        final_state = self.Coding(lst)
        return final_state

    def QLearn(self):
        for i in range(800):
            lst = self.Episode(self.table)
            for x in lst:
                code = x[0]
                act = x[1]
                next = self.Transition(code, act)
                tmp = self.table[code]['actions'][act]
                tmp = (1 - alpha) * tmp + alpha * (self.table[next]['r'] +
                                                   gamma * max(list(self.table[next]['actions'].values())))
                tmp = round(tmp, 2)
                self.table[code]['actions'][act] = tmp
        return


