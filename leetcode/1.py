def fizzBuzz(n):
    r_list = []
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                r_list.append('FizzBuzz')
            else:
                r_list.append('Fizz')
        elif i % 5 == 0:
            r_list.append('Buzz')
        else:
            r_list.append(str(i))
    print(r_list) 


if __name__ == '__main__':
    fizzBuzz(15)
