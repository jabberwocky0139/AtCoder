# coding: utf-8
import sys
#sys.setrecursionlimit(100000)
f = open("inputC.txt")
f2 = open("output.txt", "w")
N, M = [int(i) for i in f.readline().split()]
board = [[str(s) for s in list(f.readline().strip())] for j in range(N)]



#"""
# 時刻tに(i, j)にいる！前はPijにいた
def DynamicProgramming(i, j, pi, pj, t):
    res = None
    nextSquare = [[i, j+1], [i, j-1], [i+1, j], [i-1, j]]
    if [pi, pj] != [0, 0]:
        nextSquare.remove([pi, pj])
    # マスの外か行き止まりには行かない
    for num in nextSquare:
        if(not(0 <= num[0] <= N-1 and 0 <= num[1] <= M-1) or board[num[0]][num[1]] == "#" or board[num[0]][num[1]] == "s"):
            nextSquare.remove(num)
        elif(board[num[0]][num[1]] == "g"):
            f2.write("!!!\n")
            res = 0
            break
    else:
        f2.write("{}\n".format(nextSquare))
        res = min( map(lambda k: DynamicProgramming(k[0], k[1], i, j, t+1)+int(board[k[0]][k[1]])*(0.99**t) , nextSquare) )
    return res

print(DynamicProgramming(0, 0, 0, 0, 0))


"""
def rN(n):
    return n

print(0.99**5)
"""
