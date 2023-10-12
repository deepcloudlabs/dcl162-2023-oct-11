from threading import Thread, Lock

data: int = 0
lock = Lock()

def task(name):
    global data
    print(f"Thread ({name}) is running the task.")
    for i in range(0, 10_000):
        with lock:
            local = data
            local += 1
            print(f"{name}: {local}")
            data = local

    print(f"Thread ({name}) has been completed: {data}")


print("Application is just started.")
t1 = Thread(target=task, args=("t1",))
t2 = Thread(target=task, args=("t2",))
t3 = Thread(target=task, args=("t3",))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(f"Application is completed: {data}")
