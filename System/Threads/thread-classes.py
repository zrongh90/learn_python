import threading
import time


class MyThread(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(1)
        for i in range(self.count):
            with self.mutex:
                print('[{0}] => {1}'.format(self.myId, i))


lock = threading.Lock()
threads = []

for i in range(10):
    thread = MyThread(i, 5, lock)
    thread.start()
    threads.append(thread)

# mutil cpu perform different
for thread in threads:
    thread.join()
# without join Main thread will exist not wait the child thread
print('Main thread exiting')
