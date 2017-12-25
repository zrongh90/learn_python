def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        load_more = input('more?')
        print(load_more)
        if lines and load_more not in ['Y', 'y']:
            break


if __name__ == '__main__':
    import sys
    print(len(sys.argv))
    print(sys.stdin.read())
    # more(open(sys.argv[1]).read(), 10)
