def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line.strip())
        # load_more = input('more?')
        if lines:
            # load_more = open("/dev/tty").readline().strip()
            load_more = input('more?')
            if load_more not in ['Y', 'y']:
                break


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("read stdin")
        more(sys.stdin.read(),2)
    else:
        more(open(sys.argv[1]).read(),2)
