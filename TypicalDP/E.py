import collections
f = open("inputE.txt")
D = int(f.readline())
numberN = int(f.readline())
N = list(str(numberN))

for index, num in enumerate(N):
    N[index] = int(num)


for n in range(len(N)-1):
    nfs = collections.defaultdict(int)
    if n == 0:
        for i in range(10):
            nfs[i%D] += 1
    elif n != len(N)-1:
        for a, v in fs.items():
            for i in range(10):
                nfs[(a+i)%D] += v
    print(nfs)
    fs = nfs
print(nfs[0]-1)

