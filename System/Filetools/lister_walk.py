import sys,os


def lister(root):
    for (thisdir, subdirs, files) in os.walk(root):
        print('[' + thisdir + ']')
        for one_file in files:
            abs_file = os.path.join(thisdir, one_file)
            print(abs_file, end='\n')


if __name__ == '__main__':
    lister(os.sys.argv[1])
