# coding: utf-8
import itertools
import functools
try:
    f = open("inputA.txt")
    N = int(f.readline())
    inputP = [int(i) for i in f.readline().split()]
except:
    N = int(input())
    inputP = [int(i) for i in input().split()]

setPoint = set([0])
for i in inputP:
    for j in list(setPoint):
        setPoint.add(i+j)
print(setPoint)
