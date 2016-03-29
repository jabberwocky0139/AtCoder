# coding: utf-8
import numpy as np
import sys

f = open("inputC.txt")
board = [[s for s in list(f.readline().strip())] for j in range(8)]
boardTrueOrFalse = [[True for i in range(8)] for j in range(8)]

# 配置できないところを更新
def reLoad(board, boardTrueOrFalse):
    tmp = []
    # Qの位置を出力
    for i in range(8):
        for j in range(8):
            if(board[i][j] is "Q"):
                tmp.append([i,j])
    for arr in tmp:
        # ヨコ
        for j in range(8):
            boardTrueOrFalse[arr[0]][j] = False
            boardTrueOrFalse[j][arr[1]] = False
        j = 1
        while(arr[0]+j != 8 and arr[1]+j != 8):
            boardTrueOrFalse[arr[0]+j][arr[1]+j] = False
            j += 1
        j = 1
        while(arr[0]-j != -1 and arr[1]+j != 8):
            boardTrueOrFalse[arr[0]-j][arr[1]+j] = False
            j += 1
        j = 1
        while(arr[0]+j != 8 and arr[1]-j != -1):
            boardTrueOrFalse[arr[0]+j][arr[1]-j] = False
            j += 1
        j = 1
        while(arr[0]-j != -1 and arr[1]-j != -1):
            boardTrueOrFalse[arr[0]-j][arr[1]-j] = False
            j += 1
            

# 配置して次を見る
# k番目のクイーンを(i, j)に配置して次へ
def Arrangement(board, i, j, k):
    #print("i, j, k = {} {} {}".format(i, j, k))
    board[i][j] = "Q"
    reLoad(board, boardTrueOrFalse)
    if(j < 7):
        DynamicProgramming(board, i, j+1, k+1)
    else:
        DynamicProgramming(board, i+1, 0, k+1)

# 配置を変更せずに次へ
def NotArrangement(board, i, j, k):
    #print("i, j, k = {} {} {}".format(i, j, k))
    if(j < 7):
        DynamicProgramming(board, i, j+1, k)
    else:
        DynamicProgramming(board, i+1, 0, k)

#--- クイーンを(i, j)マス目に配置 ---#
def DynamicProgramming(board, i, j, k):
    #これ以上配置が不可能
    if i == 8:
        print("Pass")
        return False
    # 全て配置が終了
    elif k == 8:
        print("True")
        return True
    # (i, j)には配置できない
    elif(not(boardTrueOrFalse[i][j])): 
        NotArrangement(board, i, j, k)
        return True
    # (i, j)に配置が可能
    elif(Arrangement(board, i, j, k)): # 配置する
        return True
    elif(NotArrangement(board, i, j, k)): # 配置しない
        return True
    else:
        print("i, j, k = {} {} {}".format(i, j, k))
        return False
        
print(DynamicProgramming(board, 0, 0, 4))
#print(np.array(boardTrueOrFalse))
#print(np.array(board))

