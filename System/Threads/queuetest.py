import queue
import time
import _thread as thread


numconsumers = 2
numproducers = 4
nummessages = 4

myQueue = queue.Queue()
safePrint = thread.allocate_lock()

def producer(idnum):
    for i in range(nummessages):
        myQueue.put('product id{0}  put{1}'.format(idnum, nummessages))
    pass


def consumer(idnum):
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
    for j in range(numconsumers):
        thread.start_new_thread(consumer, (j,))
    for i in range(numproducers):
        thread.start_new_thread(producer, (i,))
    time.sleep(5)
    print("main thread exit.")
