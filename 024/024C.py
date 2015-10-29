# coding: utf-8

class Greedy:
    #--- 初期化および入力 ---#
    def __init__(self):
        #--- 入力 ---#
        #f = open("input.txt")
        #N : 街の数, D : D日以内に移動, K : 民族の数
        #self.N, self.D, self.K = [int(i) for i in f.readline().split()]
        self.N, self.D, self.K = [int(i) for i in input().split()] # 標準入力
        #self.inputLR = [[int(lr) for lr in f.readline().split()] for d in range(self.D)]
        self.inputLR = [[int(lr) for lr in input().split()] for d in range(self.D)] # 標準入力
        #self.inputST = [[int(st) for st in f.readline().split()] for k in range(self.K)]
        self.inputST = [[int(st) for st in input().split()] for k in range(self.K)] # 標準入力
        self.outputDay = []
        self.var = [None for i in range(4)]
    
    def Greedy(self):
        for place, destination in self.inputST:
            day = 0
            for low, high in self.inputLR:
                day += 1
                if((low <= place <= high) and (low <= destination <= high)):
                    print(day)
                    break
                elif((low <= place <= high) and not(low <= destination <= high)):
                    place = high if place < destination else low
            
ins = Greedy()
ins.Greedy()
