from numpy import random,average,amax,amin,sum as Sum
def pri_array(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print(x[i,j],end='\t')
        print()

def main():
    Arr=random.randint(0,21,(3,3))
    pri_array(Arr)
    print('='*20)
    print('Sum of all items in Array is: ',Sum(Arr))
    print('Average of all items in Array is: ',average(Arr))
    print('Max item of Array in row: ',amax(Arr,axis=1))
    print('Max item of Array in col: ',amin(Arr,axis=0))
main()




