import time
 
timer = time.time()

for i in range(5):
    print(i)
    time.sleep(0.2)
 
print(f'{time.time() - timer}, seconds')

