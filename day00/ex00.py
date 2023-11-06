# 0000071f49cffeaea4184be3d507086v

# import sys
# num_lines = 0
# if len(sys.orig_argv) > 2:
#     num_lines = sys.orig_argv[2]
import fileinput

for line in fileinput.input():
    print(line[0:5])
    print(line[5])
    print(len(line))
    if len(line) == 33 and line[5] != '0' and line[0:4] == '00000':
        print("HEHEH")
