# coding: utf-8
f = open("inputA.txt")
N = int(f.readline())
inputNumbers = [int(j) for j in list(f.readline()) if j is not "\n"]
(lambda z: print("{0} {1}".format(max(z), min(z))))(list(map(lambda y: len(list(filter(lambda x: x==y, inputNumbers))), range(1, 4+1))))

"""
f = open("input.txt")
N = int(f.readline())
inputNumbers = [int(j) for j in list(f.readline()) if j is not "\n"]
for y in range(1, 4+1):
    res.append(len(list(filter(lambda x: x==y, inputNumbers))))
print("{0} {1}".format(max(res), min(res)))

"""




