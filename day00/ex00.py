import sys

if __name__ == '__main__':
    num_lines = None
    count = 0
    if len(sys.argv) > 1:
        num_lines = int(sys.argv[1])

    for line in sys.stdin:
        if num_lines is None or count < num_lines:
            line = line.strip()
            if len(line) == 32 and line[5] != '0' and '00000' in line[0:5]:
                print(line)
                count += 1
        else:
            break