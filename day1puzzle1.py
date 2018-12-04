with open("input.txt", "r") as f:
    freq = 0
    for line in f:
        if "-" not in line:
            freq = freq + int(line[1:])
        else:
            freq = freq - int(line[1:])
print freq

