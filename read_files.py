# read a file content

with open('inputFile.txt', 'r') as f:
    count = 0
    for line in f:
        line_split = line.split()   # Split line to segmented value
        if line_split[2] == 'P':    # Chech if value P or F
            print(f"{line}")        # Print line with P value
        # print(str(count) + '. ' + line)
        # count += 1
