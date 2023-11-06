import sys

if __name__ == '__main__':
    line_number = 0
    file = open(sys.argv[1], "r")
    error = 0
    for line in file.readlines():
        line = line.strip()
        if len(line)!= 5:
            # print(len(line))
            error = 1
            # print(error)
            break
        if line_number == 0 or line_number == 2:
            if not (line[1].isalpha() and line[3].isalpha()):
                error = 1
                print("HEre")
                break
        elif line_number == 1:
            if not line[2].isalpha():
                error = 0
                break
        else:
            error = 1
            break
        line_number+=1
    if error:
        print("Error")
    else:
        print("True")