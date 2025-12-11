import  time

start_time = time.time()

M = 3
N = 2

for i in range(M):
    print(f'внешний цикл: {i}')
    time.sleep(1)

for j in range(N):
    print(f'внутренний цикл: {j}')
    time.sleep(1)

end_time = time.time()

time_ = end_time - start_time
print(f'общее время: {time_} секунд')




for i in range(2):
    print(f'i: {i}')
    time.sleep(1)
    for j in range(3):
        print(f'\t j: {j}')
        time.sleep(1)