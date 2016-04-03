# coding: utf-8

class UnionFind:
    #--- 初期化 ---#
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    #--- rootを求める ---#
    def Find(self, x):
        if(self.par[x] == x):
            return x
        else:
            self.par[x] = self.Find(self.par[x])
            return self.par[x]
    #--- 2つの集合を併合 ---#
    def Unite(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if(x == y):
            return
        if(self.rank[x] < self.rank[y]):
            self.par[x] = y
        else:
            self.par[y] = x
            if(self.rank[x] == self.rank[y]):
                self.rank[x] += 1
    #--- 同じ集合かどうか ---#
    def Same(self,x, y):
        return self.Find(x) == self.Find(y)

#--- 入力 ---#
N, M = [int(i) for i in input().split()] # 標準入力
#f = open("input.txt")
#N, M = [int(i) for i in f.readline().split()]

input = [[int(node) for node in input().split()] for m in range(M)] # 標準入力
#input = [[int(node) for node in f.readline().split()] for m in range(M)]

var = UnionFind(N)
list(map(lambda i: var.Unite(i[0]-1, i[1]-1), input))
num = set()
list(map(lambda i: num.add(var.Find(i)), range(N)))
print(len(num)-1)

