from fileinput import input

with open('proba.txt', 'r') as file:
    replacing = {
        'ana': 'milovan',
        'babo': 'tata',
    }

    # local changes

    for line in file:
        print(line)
        for replacement in replacing:
            line = line.replace(replacement, replacing[replacement])
            # print(replacement, replacing[replacement])
        print(line)

    # permanent changes
for line in input('proba.txt', inplace=True):
    for replacement in replacing:
        line = line.replace(replacement, replacing[replacement])
