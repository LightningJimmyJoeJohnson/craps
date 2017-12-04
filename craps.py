import random

def roll(n):
    rN = random.randint(1,6) + random.randint(1,6)
    if rN == 7:
        print("%d Loose \n" % rN)
    elif rN == n:
        print("%d Win \n" % rN)
    else:
        print("%d, " % rN, end="") 
        roll(n)

i = 0
while i<20:
    n = random.randint(1,6) + random.randint(1,6)
    if n in [2,3,12]:
        print("%d, loose \n" % n)
    elif n in [7,11]:
        print("%d, Win \n" % n)
    else:
        print("%d, " % n, end="") 
        roll(n)
    i += 1
print("end")
