# coding: utf-8
import sys
length = int(input())

def firstCheck(accessory):
    if(length % 2 == 0 or accessory[length//2] != "b"):
        print(-1)
        sys.exit()
        
def secondCheck(accessory, n):
    if(not(accessory[length//2+(n+1)] == "c" and accessory[length//2-(n+1)] == "a")):
        print(-1)
        sys.exit()

def thirdCheck(accessory, n):
    if(not(accessory[length//2+(n+1)] == "a" and accessory[length//2-(n+1)] == "c")):
        print(-1)
        sys.exit()

def fourthCheck(accessory, n):
    if(not(accessory[length//2+(n+1)] == "b" and accessory[length//2-(n+1)] == "b")):
        print(-1)
        sys.exit()
        
accessory = [str(s) for s in input().strip()]
firstCheck(accessory)
n = 0
while(True):
    try:
        secondCheck(accessory, n)
        n += 1
    except:
        break
    try:
        thirdCheck(accessory, n)
        n += 1
    except:
        break
    try:
        fourthCheck(accessory, n)
        n += 1
    except:
        break
print(n)
