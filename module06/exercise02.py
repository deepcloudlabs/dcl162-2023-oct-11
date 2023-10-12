from threading import Thread

data: int = 0


def task(name):
    global data
    print(f"Thread ({name}) is running the task.")
    for i in range(0, 10_000):
        local = data
        local += 1
        print(f"{name}: {local}")
        data = local
    print(f"Thread ({name}) has been completed: {data}")


print("Application is just started.")
t1 = Thread(target=task, args=("t1",))
t2 = Thread(target=task, args=("t2",))

t1.start()
t2.start()
t1.join()
t2.join()
print(f"Application is completed: {data}")
