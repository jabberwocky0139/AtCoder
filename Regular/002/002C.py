import itertools
N = int(input())
inputCommand = list(input().strip())
shortcutCombinations = list(itertools.combinations(itertools.product(["A", "B", "X", "Y"], repeat=2), 2))
 
res = N
for num in shortcutCombinations:
    commandTmp = list(inputCommand)
    i = 0
    while(len(commandTmp)-1 > i):
        if (commandTmp[i],commandTmp[i+1]) == num[0] or (commandTmp[i], commandTmp[i+1]) == num[1]:
            commandTmp[i] = "S"
            commandTmp.pop(i+1)
        i += 1
    res = min(len(commandTmp), res)
print(res)

"""
# coding: utf-8
import itertools
f = open("inputC.txt")
N = int(f.readline())
inputCommand = list(f.readline().strip())
command = ["A", "B", "X", "Y"]
shortcut = list(itertools.product(command, repeat=2))
shortcutCombinations = list(itertools.combinations(shortcut, 2))


res = N
for num in shortcutCombinations:
    commandTmp = list(inputCommand)
    i = 0
    while(len(commandTmp)-1 > i):
        if (commandTmp[i],commandTmp[i+1]) == num[0] or (commandTmp[i], commandTmp[i+1]) == num[1]:
            commandTmp[i] = "S"
            commandTmp.pop(i+1)
        i += 1
    res = min(len(commandTmp), res)
print(res)
"""
