import io
import os
Dir=input('please enter direction of text file: ')
if os.path.exists(Dir):
    my_file=open(Dir,'r')
    while True:
        line=my_file.readline()
        if line !='':
            print(line,end='')
        else:
            my_file.close()
            break