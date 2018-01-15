import _thread as thread, time


def counter(myId, count):
    mutex.acquire()
    for i in range(count):
        time.sleep(1)
        # mutex.acquire()
        print("[{0}] => {1}".format(myId, i))
        # mutex.release()
    mutex.release()


def parent():
    for i in range(5):
        thread.start_new_thread(counter, (i, 5))
    time.sleep(20)
    print("Main thread exiting.")

mutex = thread.allocate_lock()

parent()
