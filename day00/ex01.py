import sys

if __name__ == '__main__':
    answer = ""
    line = sys.argv[1].split()
    for word in line:
        answer+=word[0]
    print(answer)