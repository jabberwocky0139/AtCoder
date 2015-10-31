N = int(input())
print("YES") if N % 400 == 0 else print("NO") if N % 100 == 0 else print("YES") if N % 4 == 0 else print("NO")

"""
# coding: utf-8
f = open("inputA.txt")
N = int(f.readline())

if(N % 400 == 0):
    print("YES")
elif(N % 100 == 0):
    print("NO")
elif(N % 4 == 0):
    print("YES")
else:
    print("NO")
"""
