# write a file content

with open('inputFile.txt', 'r') as f:
    with open('PassFile.txt', 'w') as pf:
        with open('FailFile.txt', 'w') as ff:
            for line in f:
                line_split = line.split()
                if line_split[2] == 'P':
                    pf.write(line)
                else:
                    ff.write(line)
