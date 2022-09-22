from array import *

code=[1000,2000,3000,4000,5000,8000,10000,20000,30000,50000]

def calculator(carid):
    penalty=0
    n=int(input('please enter num of penalty: '))
    l=1
    while l<=n:
        entry_code=int(input('Enter code {}: '.format(-n+(2*n))))
        if entry_code>=0 and entry_code<=9:
            penalty+=code[entry_code]
            l+=1
        else:
            print('Enter code between 0-9')
    return penalty

def main():
    car_id=int(input('enter car id:'))
    while car_id!=(-999):
        print('total penalty for car number {} is: '.format(car_id),calculator(car_id))
        car_id=int(input('enter car id:'))


main()
