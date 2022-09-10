from array import *
p=array('f',list(float(input('enter items: ')) for i in range(int(input('enter number of items: ')))))
n=len(p)
if n==1:
    if p[0]==0:
        print('*unexecutable command*')
    else:
        print('{}/{}=1'.format(p[0],p[0]))
else:
    mid=(n//2)
    if p.count(0)==n:
        print('*unexecutable command*')
    else:
        j=0
        sign=1
        for i in range(n):
            if exit==1:
                break
            if p[mid+(sign*j)]==0:
                if sign==1:
                    j+=1
                sign=sign*(-1)
            else:
                for a in range(n):
                    print('{}/{}={}'.format(p[a],p[mid+(sign*j)],(p[a]/p[mid+(sign*j)])))
                    exit=1
