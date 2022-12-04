from time import sleep, perf_counter
from threading import Thread

start_time = perf_counter()

def task_1():
    for i in range(1,5):
        print(f"starting task - {i}")
        sleep(2)

def task_2():
    for i in range(6,11):
        print(f"strating new task- {i}")
        sleep(2)

t1 = Thread(target=task_1)
t2 = Thread(target=task_2)
# task_1()
# task_2()

t1.start()
t2.start()
t1.join()
t2.join()

end_time = perf_counter()
print(f"total time = {end_time - start_time}")