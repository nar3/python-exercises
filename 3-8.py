from math import *
def fac_equ(w):
    q=w
    digit=0
    one=10
    while True:
        if w//one<1:
            digit+=1
            break
        one*=10
        digit+=1
    w=list(str(w))
    w=list(map(int,w))
    if sum((map(factorial,w)))==q:
        print(sum((map(factorial,w))),q)
for i in range(100,1000):
    fac_equ(i)
