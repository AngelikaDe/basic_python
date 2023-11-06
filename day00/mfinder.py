import sys

if __name__ == '__main__':
    line_number = 0
    file = open(sys.argv[1], "r")
    error = 0
    for line in file.readlines():
        line = line.strip()
        if len(line)!= 5:
            error = 1
            break
        if line_number == 0 or line_number == 2:
            if line[1] == '*' and line[3] == '*':
                error = 1
                break
        elif line_number == 1:
            if line[2] == '*':
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