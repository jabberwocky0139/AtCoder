# coding: utf-8

f = open("inputB.txt")
A, B = [int(i) for i in f.readline().split()]
#A, B = [int(i) for i in input().split()]

#--- ワンライナーで書けるか？ ---#
res = 0
A ,res = A + 10*(abs(B-A)//10) if A <= B else A - 10*(abs(B-A)//10), res + abs(B-A)//10
A, res = (A+10, res+1) if ((A < B) and (abs(B-A) >= 8)) else (A-10, res+1) if ((A > B) and (abs(B-A) >= 8)) else (A, res)
A ,res = A + 5*(abs(B-A)//5) if A <= B else A - 5*(abs(B-A)//5), res + abs(B-A)//5
A, res = (A+5, res+1) if ((A < B) and (abs(B-A) >= 4)) else (A-5, res+1) if ((A > B) and (abs(B-A) >= 4)) else (A, res)
print(res+abs(B-A))

"""
A, B = [int(i) for i in input().split()]
res = 0
A ,res = A + 10*(abs(B-A)//10) if A <= B else A - 10*(abs(B-A)//10), res + abs(B-A)//10
if abs(B-A) >= 8:
    A += 10 if A < B else -10
    res += 1
A ,res = A + 5*(abs(B-A)//5) if A <= B else A - 5*(abs(B-A)//5), res + abs(B-A)//5
if abs(B-A) >= 4:
    A += 5 if A < B else -5
    res += 1
res += abs(B-A)
print(res)
"""
