N = int(input())
list(map(lambda j: print(j),[i[::-1] for i in sorted([input().strip()[::-1] for i in range(N)])]))
"""
# coding: utf-8
f = open("inputB.txt")
N = int(f.readline())
list(map(lambda j: print(j),[i[::-1] for i in sorted([f.readline().strip()[::-1] for i in range(N)])]))
"""
