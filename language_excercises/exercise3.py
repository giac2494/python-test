def count_lines(file_name):

    in_f = open(file_name,"rb")

    i = 0
    for line in in_f:
        i+= 1

    in_f.close()
    return i

print count_lines('words.txt')