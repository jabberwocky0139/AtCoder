# coding: utf-8
import sys
#sys.setrecursionlimit(100000)
f = open("inputC.txt")
f2 = open("output.txt", "w")
N, M = [int(i) for i in f.readline().split()]
board = [[s for s in list(f.readline().strip())] for j in range(N)]

#"""
# 今(i, j)にいる！時刻t
def DynamicProgramming(i, j, t):
    f2.write("{},{},{}\n".format(i, j, t))
    res = None
    # ゴール
    if board[i][j] == "S":
        res = 0
    else:
        print("!!!")
        nextSquare = [[i, j+1], [i, j-1], [i+1, j], [i-1, j]]
        # マスの外か行き止まりには行かない
        for num in nextSquare:
            if(not(0 <= num[0] <= N-1 and 0 <= num[1] <= M-1) or board[num[0]][num[1]] == "#" or board[num[0]][num[1]] == "s"):
                nextSquare.remove(num)
            elif(board[num[0]][num[1]] == "g"):
                f2.write("!!!\n")
                DynamicProgramming(num[0], num[1])
                break
        else:
            f2.write("{}\n".format(nextSquare))
            res = min( map(lambda k: DynamicProgramming(k[0], k[1], t+1)+int(board[k[0]][k[1]])*(0.99**t) , nextSquare) )
    return res

print(DynamicProgramming(0, 0, 0))


"""
def rN(n):
    return n

print(0.99**5)
"""
