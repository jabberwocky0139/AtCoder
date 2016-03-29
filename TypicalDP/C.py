# coding: utf-8
# 入力
# f = open("inputC.txt")
# K = int(f.readline())
K = int(input())
R = []
N = 2**K
# for i in range(N):
#     R.append(int(f.readline()))
for i in range(N):
    R.append(int(input()))
inputMembers = [int(i) for i in range(N)]
setMembers = [[] for i in range(K)]
for i in range(0, N, 2):
    setMembers[0].append([inputMembers[i],inputMembers[i+1]])
for j in range(K-1):
    for i in range(0, len(setMembers[j]), 2):
        setMembers[j+1].append(setMembers[j][i]+setMembers[j][i+1])

# aがbに勝つ確率
def f(a, b):
    if a == b:
        return 0
    else:
        return 1/(1 + 10**((R[b]-R[a])/400))

# プレイヤーiがk回戦目に当たる相手のリストのインデックスを返す
def g(i, k):
    for index, setMember in enumerate(setMembers[k-1]):
        if i in setMember:
            if k == 1:
                return k-1, index
            elif i in  setMembers[k-2][2*index]:
                return k-2, 2*index+1
            else:
                return k-2, 2*index

# iがk回戦目で勝ち残っている確率
# a[i][k]
a = [[1 for k in range(K+1)] for i in range(N)]
for k in range(K+1):
    for i in range(N):
        if k == 0:
            a[i][k] = 1
        else:
            productor = 0
            i1, i2 = g(i, k)
            for j in setMembers[i1][i2]:
                productor += a[j][k-1]*f(i, j)
            a[i][k] = a[i][k-1]*productor

for i in range(N):
    print(a[i][K])


    
