# coding: utf-8
import sys
import math as m

def factorialAll(i1, i2, i3, i4, i5, i6):
    return m.factorial(int(i1))*m.factorial(int(i2))*m.factorial(int(i3))*m.factorial(int(i4))*m.factorial(int(i5))*m.factorial(int(i6))

f = open("inputD.txt")
N, D = [int(i) for i in f.readline().split()]

p2 = p3 = p5 = 0
while(D%2 == 0 and D!= 0):
    D = D/2
    p2 +=1

while(D%3 == 0 and D!= 0):
    D = D/3
    p3 +=1

while(D%5 == 0 and D!= 0):
    D = D/5
    p5 +=1
if(D != 1):
    print("No answer")
    sys.exit(-1)

# <--- i5 --->
i5 = p5
# 6の個数の最大値を決定
i6Max = min(p2, p3)
print("i6Max:{}".format(i6Max))
# <--- i5, i6 --->
# 0 <= i6 <= i6Max
res = 0
factN = m.factorial(N)
for i6 in range(0, i6Max+1):
    # <--- i3, i5, i6 --->
    i3 = p3-i6
    print("i3:{}".format(i3))
    # i2 + 2*i4 = p2 - i6を満たす(i2, i4)の組
    # 右辺が偶数
    if((p2-i6) % 2 == 0):
        for i2 in range(0, (p2-i6)+1 , 2):
            # <--- i2, i3, i4, i5, i6 --->
            i4 = ((p2 - i6) - i2)/2
            # !!!<--- 全て確定 --->!!!
            i1 = N - (i2+i3+i4+i5+i6)
            if(i1 >= 0):
                print(i1, i2, i3, i4, i5, i6)
                res += factN/factorialAll(i1, i2, i3, i4, i5, i6)
    # 右辺が奇数
    else:
        for i2 in range(1, (p2-i6)+1 , 2):
            # <--- i2, i3, i4, i5, i6 --->
            i4 = ((p2 - i6) - i2)/2
            # !!!<--- 全て確定 --->!!!
            i1 = N - (i2+i3+i4+i5+i6)
            if(i1 >= 0):
                print(i1, i2, i3, i4, i5, i6)
                res += factN/factorialAll(i1, i2, i3, i4, i5, i6)
    # i2 + 2*i4 = p2 + 1 - i6を満たす(i2, i4)の組
    # 右辺が偶数
    if((p2 + 1 - i6) % 2 == 0):
        for i2 in range(0, (p2 + 1 - i6) + 1, 2):
            # <--- i2, i3, i4, i5, i6 --->
            i4 = ((p2 - i6) + 1 - i2)/2
            # !!!<--- 全て確定 --->!!!
            i1 = N - (i2+i3+i4+i5+i6)
            if(i1 >= 0):
                print(i1, i2, i3, i4, i5, i6)
                res += factN/factorialAll(i1, i2, i3, i4, i5, i6)
    # 右辺が奇数
    else:
        for i2 in range(1, (p2 + 1 - i6) + 1 , 2):
            # <--- i2, i3, i4, i5, i6 --->
            i4 = ((p2 - i6) + 1 - i2)/2
            # !!!<--- 全て確定 --->!!!
            i1 = N - (i2+i3+i4+i5+i6)
            if(i1 >= 0):
                print(i1, i2, i3, i4, i5, i6)
                res += factN/factorialAll(i1, i2, i3, i4, i5, i6)

print(res)
print(res/6**N)
