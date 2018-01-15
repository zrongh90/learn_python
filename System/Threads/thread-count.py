import _thread as thread, time


def counter(myId, count):
    for i in range(count):
        # time.sleep(i)
        print("[{0}] => {1}".format(myId, i))

def parent():
    for i in range(5):
        thread.start_new_thread(counter, (i, 5))
    time.sleep(10)
    print("Main thread exiting.")
    print(a)


parent()
