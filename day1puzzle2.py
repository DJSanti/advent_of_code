with open("input.txt", "r") as f:
    freq = 0
    freq_list = []
    for line in f:
        if "-" not in line:
            freq = freq + int(line[1:])
        else:
            freq = freq - int(line[1:])
        freq_list.append(freq)
    #print freq_list

count = 0
for index, item in enumerate(freq_list):
    next = index + 1
    if next < len(freq_list):
        #print index, item, freq_list[next]
        if item == freq_list[x for i in range(len(freq_list))]:
            print item

