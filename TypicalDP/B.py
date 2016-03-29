# coding: utf-8
# P, Q = すめけ, すぬけ
import sys
sys.setrecursionlimit(10000)

try:
    f = open("inputB.txt")
    A, B = [int(i) for i in f.readline().split()]
    a = [int(i) for i in f.readline().split()]
    b = [int(i) for i in f.readline().split()]
except:
    A, B = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

# DP[who][i][j]
DP =[[-1 for i in range(B+1)] for j in range(A+1)]

#who : PならTrue, QならFalse
#i, j : 左の山の先頭がi番目, 右の山の先頭がj番目
#res : Pの得点
def DynamicProgramming(who, i, j):
    # メモ化
    try:
        if DP[i][j] >= 0:
            return DP[i][j]
    except IndexError:
        pass
    
    res = None
    # 終了条件
    if i == A and j == B:
        res = 0
    # aを取る
    elif i != A and j == B:
        if who:
            res = DynamicProgramming(not(who), i+1, j) + a[i]
        else:
            res = DynamicProgramming(not(who), i+1, j)
    # bを取る
    elif i == A and j != B:
        if who:
            res = DynamicProgramming(not(who), i, j+1) + b[j]
        else:
            res = DynamicProgramming(not(who), i, j+1)
    # a, bのどちらを取るか
    else:
        # Pの番
        if who:
            res = max(DynamicProgramming(not(who), i+1, j) + a[i], DynamicProgramming(not(who), i, j+1) + b[j])
        else:
            res = min(DynamicProgramming(not(who), i+1, j), DynamicProgramming(not(who), i, j+1))
    
    try:
        DP[i][j] = res
    except IndexError:
        pass

    return res

#print(DynamicProgramming(True, 0, 0))
#print(DP)

DP[A][B] = 0
for i in range(A, -1, -1):
    for j in range(B, -1, -1):
        if i == A and j == B:
            continue
        # 偶数番目に取るのはQ
        elif (i+j) % 2 != 0:
            # 左を取る
            #if i != A and j == B:
            if j == B:
                DP[i][j] = DP[i+1][j]
            # 右を取る
            elif i == A:
                DP[i][j] = DP[i][j+1]
            else:
                DP[i][j] = min(DP[i+1][j], DP[i][j+1])
        # 奇数番目に取るのはP
        elif (i+j) % 2 == 0:
            # 左を取る
            if j == B:
                DP[i][j] = DP[i+1][j] + a[i]
            # 右を取る
            elif i == A:
                DP[i][j] = DP[i][j+1] + b[j]
            else:
                DP[i][j] = max(DP[i+1][j] + a[i], DP[i][j+1] + b[j])

print(DP[0][0])



