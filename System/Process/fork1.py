import os


def child():
    print('hello from child', os.getpid())
    os._exit(0)


def parent():
    new_pid = os.fork()
    if new_pid == 0:
        child()
    else:
        print("Hello from parent", os.getpid(), "child pid" ,new_pid)



while True:
    parent()
    if input() == "q":
        break
