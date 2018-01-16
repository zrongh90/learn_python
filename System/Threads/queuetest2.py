import queue
import time
import threading


numconsumers = 2
numproducers = 4
nummessages = 4

dataQueue = queue.Queue()
safePrint = threading.Lock()

def producer(idnum, myQueue):
    for i in range(nummessages):
        myQueue.put('product id{0}  put{1}'.format(idnum, i))
    pass


def consumer(idnum, myQueue):
    while True:
        time.sleep(0.1)
        try:
            data = myQueue.get(block=False)
        except queue.Empty:
            print('queue empty')
            pass
        else:
            with safePrint:
                print('get {0}'.format(data))
    pass


if __name__ == "__main__":
    threads = []
    for j in range(numconsumers):
        thread = threading.Thread(target=consumer, args=(j, dataQueue))
        thread.daemon = True
        thread.start()
    for i in range(numproducers):
        thread = threading.Thread(target=producer, args=(i, dataQueue))
        threads.append(thread)
        thread.start()
    # get enough time for consumer to get output
    time.sleep(3)
    for thread in threads:
        thread.join()
    print("main thread exit.")
