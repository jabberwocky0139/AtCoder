### input
f = open("input/inputC.txt", "r")
K = int(f.readline())
R = [int(f.readline()) for i in range(2**K)]

def win_P(P, Q):
    return (1 + 10**((Q - P)/400))**-1


dp = [1] * (2**K)
# k回戦
def rec_tournament(k):
    if k == K:
        
    


