# coding: utf-8
string = str(input())
num_arr = [int(n) for n in input().split()]
string = list(string.strip())
for index, i in enumerate(num_arr):
    string.insert(i + index, "\"")
print("".join(string))
