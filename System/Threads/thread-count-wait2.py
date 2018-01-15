import _thread as thread
import time
stdoutmutex = thread.allocate_lock()
exitmutex = [False] * 10


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print("[{0}] => {1}".format(myId, i))
        stdoutmutex.release()
    exitmutex[myId] = True


def parent():
    for i in range(10):
        thread.start_new_thread(counter, (i, 50))
    #while False in exitmutex:
    #        pass
    print("Main Thread exist")


parent()
