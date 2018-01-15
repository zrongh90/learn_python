import sys,os

def lister(root, modules):
    match = []
    for (thisdir, subdirs, files) in os.walk(root):
        for one_file in files:
            if one_file.endswith('.py'):
                abs_file = os.path.join(thisdir, one_file)
                if modules in open(abs_file, 'r').read():
                    match.append(abs_file)
    for name in match:
        print(name)


if __name__ == '__main__':
    lister(os.sys.argv[1], os.sys.argv[2])
