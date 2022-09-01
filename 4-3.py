# by list
'''n=int(input('enter num of insert: '))
my_array=list()
new=list()
for i in range(n):  
    my_array.append(int(input('my_array[{}]='.format(i+1))))
while len(my_array):    
    new.append(min(my_array))
    my_array.remove(min(my_array))
print(new)'''


from array import *
n=int(input('enter num of insert: '))
my_array=array('i',[])
new=array('i',[])
for i in range(n):  
    my_array.append(int(input('my_array[{}]='.format(i+1))))
while len(my_array):    
    new.append(min(my_array))
    my_array.remove(min(my_array))
print(new)