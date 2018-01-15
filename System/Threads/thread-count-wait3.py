import _thread as thread
import time
stdoutmutex = thread.allocate_lock()
exitmutex = [thread.allocate_lock() for i in range(5)]


def counter(myId, count):
    for i in range(count):
        time.sleep(1 / (myId+1))
        with stdoutmutex:
            print("[{0}] => {1}".format(myId, i))
    exitmutex[myId].acquire()


def parent():
    for i in range(5):
        thread.start_new_thread(counter, (i, 10))
    #while False in exitmutex:
    #        pass
    for mutex in exitmutex:
        print(mutex.locked())
        while not mutex.locked():
            time.sleep(0.25)
    # while not all(mutex.locked() for mutex in exitmutex):
    #    time.sleep(0.25)
    print("Main Thread exist")


parent()
