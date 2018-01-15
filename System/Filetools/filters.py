import sys


def filter_files(name, function):
    in_f = open(name, 'r')
    out_f = open('{0}.out'.format(name), 'w')
    for line in in_f:
        out_line = function(line)
        out_f.write(out_line)
    in_f.close()
    out_f.close()


def filter_stream(function):
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        print(function(line), end='')


if __name__ == '__main__':
    filter_stream(lambda line:line)
