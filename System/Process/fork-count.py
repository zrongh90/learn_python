import os
import time
import sys


def counter(count):
    for i in range(count):
        time.sleep(1)
        print("[{0}] => {1}".format(os.getpid(), i))
    pass


for i in range(5):
    new_pid = os.fork()
    if new_pid == 0:
        counter(5)
        sys.exit(0)
    else:
        print('Proces {0} spawned'.format(new_pid))

print("Main process existing")
