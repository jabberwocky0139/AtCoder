import functools
N = int(input())
print(functools.reduce(lambda a,b: a+b, map(lambda p: 4 if p == "A" else 3 if p == "B" else 2 if p == "C" else 1 if p == "D" else 0  ,input().strip()))/N)


"""
# coding: utf-8
import functools
f = open("inputA.txt")
N = int(f.readline())
print(functools.reduce(lambda a,b: a+b, map(lambda p: 4 if p == "A" else 3 if p == "B" else 2 if p == "C" else 1 if p == "D" else 0  ,f.readline().strip()))/N)
"""
