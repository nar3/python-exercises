i=1
x=float(input('enter x value: '))
s=0
denominator=0
while i<=10:
    denominator+=i*(x**i)
    if i%2==0:
        s-=1/(denominator)
    else:
        s+=1/(denominator)
    i+=1
print(s)