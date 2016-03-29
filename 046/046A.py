# coding: utf-8

n = int(input())
digit = n//9 + 1 if n%9 is not 0 else n//9
number = n%9 if n%9 is not 0 else 9

print(str(number)*digit)
