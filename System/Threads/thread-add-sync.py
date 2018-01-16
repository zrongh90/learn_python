import threading
import time
count = 0


def counter(addlock):
    global count
    with addlock:
        count = count + 1
    time.sleep(0.5)
    with addlock:
        count = count + 1

lock = threading.Lock()
threads = []
for i in range(100):
    thread = threading.Thread(target=counter, args=(lock,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(count)
