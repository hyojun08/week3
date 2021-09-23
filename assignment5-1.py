import time
import random

def interfibo(n):
    First, Second = 0, 1
    for i in range(n):
        First, Second = Second, First + Second
    return First


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = interfibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
