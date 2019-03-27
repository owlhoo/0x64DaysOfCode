import shutil
import os
import fileinput

# copy file

shutil.copyfile('../gotto.txt', './manual_copy.txt')

# check if file exists

print(os.path.isfile('./manual_copy.txt'))

# check if file path exists

print(os.path.exists('/home/home'))

source = '../'
destination = './tree'
# shutil.copytree(source, destination)          Copy a directory tree

# iterating files

for root, folder, files in os.walk('/home/goofy'):
    for filename in files:
        print(root, filename) if 'gotto.txt' in filename else False

# more efficient method

for entry in os.scandir('/home/goofy/projects/'):
    if not entry.name.startswith('.') and '0x64' in entry.name:     # entry.is_file() checks if its a file
        print(entry.name)

# replacing a text in file

replacement = {'search1': 'replace1',
               'search2': 'replace2'}

for line in fileinput.input('somefile.txt', inplace=True):
    for search_for in replacement:
        replace_with = replacement[search_for]
        line = line.replace(search_for, replace_with)
    print(line)
