from scanfile import scanner
import sys


class UnknownError(Exception):
    def __init__(self, line):
        print("test {0}".format(line), end='')
    pass


class MyCommand(dict):
    def __missing__(self, key):
        return "no such key"

def processline(line):
    if line[0] == '*':
        print("Ms. {0}".format(line[1:]),end='')
    elif line[0] == '+':
        print("Mr. {0}".format(line[1:]), end='')
    else:
        raise UnknownError(line)

def processlinelite(line):
    commands = {'*': 'Ms. ', '+': 'Mr.'}
    com = MyCommand(commands)
    print('{0}{1}'.format(com[line[0]], line[1:]))

filename = 'hillbillies.txt'
if len(sys.argv) == 2:
    filename = sys.argv[1]
# scanner(filename, processline)
scanner(filename, processlinelite)
