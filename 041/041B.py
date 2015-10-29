# coding: utf-8

class Ameba:
    def __init__(self):
        #--- 入力 ---#
        # f = open("inputB.txt")
        # self.columns, self.rows = [int(i) for i in f.readline().split()]
        # self.b = [[int(j) for j in list(f.readline()) if j is not "\n"] for i in range(self.columns)]
        self.columns, self.rows = [int(i) for i in input().split()] # 標準入力
        self.b = [[int(j) for j in list(input()) if j is not "\n"] for i in range(self.columns)] # 標準入力
        self.a = [[int(0) for j in range(self.rows)] for i in range(self.columns)]
    
    # 1 <= i <= columns-1, 1 <= j <= rows-1 
    def Switch(self, i, j):
        switchNumber = min(self.b[i][j+1], self.b[i][j-1], self.b[i+1][j], self.b[i-1][j])
        if switchNumber > 0:
            self.a[i][j] += switchNumber
            self.b[i+1][j] -= switchNumber
            self.b[i-1][j] -= switchNumber
            self.b[i][j+1] -= switchNumber
            self.b[i][j-1] -= switchNumber

    def PrintAnswer(self):
        for b in self.a:
            list(map(lambda x: print(x, end=""), b))
            print()
    
    def Ameba(self):
        for column in range(1, self.columns-1):
            for row in range(1, self.rows-1):
                self.Switch(column, row)
        self.PrintAnswer()

var = Ameba()
var.Ameba()
