import collections

f = open("inputD.txt")
N, D = map(int, f.readline().split())
 
d2 = 0
while D % 2 == 0:
    D //= 2
    d2 += 1
d3 = 0
while D % 3 == 0:
    D //= 3
    d3 += 1
d5 = 0
while D % 5 == 0:
    D //= 5
    d5 += 1
 
def solve(d2, d3, d5, D, N):
    if D != 1:
        return 0
    if d2 > N*2:
        return 0
    if d3 + d5 > N:
        return 0
    fs = {(0, 0, 0): 1}
    for n in range(N):
        nfs = collections.defaultdict(int)
        for (a2, a3, a5), v in fs.items():
            nfs[a2, a3, a5] += v
            nfs[min(a2 + 1, d2), a3, a5] += v
            nfs[a2, min(a3 + 1, d3), a5] += v
            nfs[min(a2 + 2, d2), a3, a5] += v
            nfs[a2, a3, min(a5 + 1, d5)] += v
            nfs[min(a2 + 1, d2), min(a3 + 1, d3), a5] += v
        fs = nfs
        print(fs)
    return nfs[d2, d3, d5] / (6 ** N)
 
print('{:.8f}'.format(solve(d2, d3, d5, D, N)))
