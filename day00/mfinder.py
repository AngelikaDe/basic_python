import sys

def check_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.read().splitlines()

        if (
            len(lines) == 3
            and len(lines[0]) == len(lines[1]) == len(lines[2]) == 5
            and lines[0][1] != "*" and lines[0][3] != "*"
            and lines[1][2] != "*"
        ):
            return "True"
        else:
            return "Error"
    except (IOError, IndexError):
        return "Error"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py filename")
    else:
        result = check_file(sys.argv[1])
        print(result)
