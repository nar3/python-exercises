import time

start_time=time.time()
for i in range(100000):
    i*=5
    i**=3
print(time.time()-start_time)