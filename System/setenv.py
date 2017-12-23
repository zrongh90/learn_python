import os
print('setenv...', end = '  ')
print(os.environ['USER'])

os.environ['USER'] = "Brian"
os.system('python3.4 echoenv.py')
