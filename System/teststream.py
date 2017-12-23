def interact():
    print('Hello stream world')
    while True:
        try:
            num = input('Enter a nmber>')
            print(num, ' squared is  ', int(num) ** 2)
        except EOFError:
            break
    print('Bye')

if __name__ == '__main__':
    interact()
        
