def scanner(filename, function):
    file = open(filename)
    for line in file:
        function(line)
    file.close()
