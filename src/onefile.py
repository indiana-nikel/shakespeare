from os import listdir
from os.path import isfile, join

comedy_path = "../data/comedy/"
tragedy_path = "../data/tragedy/"
history_path = "../data/comedy/"

filenames_comedy = [f for f in listdir(comedy_path) if isfile(join(comedy_path, f))]
filenames_tragedy = [f for f in listdir(tragedy_path) if isfile(join(tragedy_path, f))]
filenames_history = [f for f in listdir(history_path) if isfile(join(history_path, f))]

filenames = []

for fname in filenames_comedy:
    filenames.append(comedy_path + fname)

for fname in filenames_tragedy:
    filenames.append(tragedy_path + fname)

for fname in filenames_history:
    filenames.append(history_path + fname)

with open('../data/shakespeare.md', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
