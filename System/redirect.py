import sys


class Output:

    def write(self):
        pass

    def flush():
        pass


class Input:
    text = ''

    def __init__(self, input=''):
        self.text = input

    def readlines(self):
        return self.text


if __name__ == '__main__':
    input = "my redirect test"
    save_streams = sys.stdin, sys.stdout
    sys.stdin = Input(input)
    sys.stdout = Output()
    output = sys.stdin.readlines()
    sys.stdin, sys.stdout = save_streams
    print(output)


    
