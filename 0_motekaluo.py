#!/usr/bin/python3

import random
import math
def main():
    print("number")
n = int(input())
if n == 0:
    print("erro,please try again:")
    n=int(input())
elif n != 0:
    total=0
    for i in range(n):
        x=random.random()
        y=random.random()
        if math.sqrt(x**2+y**2)<1.0:
            total +=1
    mypi=4.0*total/n
    print("number"+str(n)+"pi's"+str(mypi))
    print("pi"+str(math.pi))
    print("error's"+str(abs(math.pi-mypi)/math.pi))
main()
