def trailingZeros(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    print(result)
    num_list = list(str(result))
    num_list.reverse()
    count = 0
    for i in num_list:
        if i == "0":
            count = count + 1
        else:
            break
    return count


if __name__ == "__main__":
    print(trailingZeros(1001171717))
        
