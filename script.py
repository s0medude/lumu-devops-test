import os
import re
import operator
from os.path import join, getsize

# Search for the given path and returned it if exists or return False if it is not present
def is_directory(path):
    if os.path.isdir(path) and os.path.exists(path):    
        print('The {} is an existing directory!'.format(path))
        return path
    else:
        print('The {} is not a directory'.format(path))
        print('Try again!')
        return False

# Find the directory name by executing a bash command with the name as a parameter,
# then check if the resulting path is an existing directory
def find_directory(name):
    command = 'find ~/ -type d -name {}'.format(name)
    p = os.popen(command).read()
    if p:
        name = re.sub('\n', '', p)
        path = is_directory(name)
        return path
    else: 
        print("\nThere's not a directory such as: {} ".format(name))
        return False


# Return a list of the files for the given directory
def get_files_from_directory(directory):
    try:
        files = []
        for r, d, f in os.walk(directory):
            for name in f:
                files.append(os.path.join(r, name))
    except PermissionError:
        print('You dont have the right permission to access this directory')
    else:
        return files

# Return a dictionary for the given list, the key is the name of th file and the value is the size of that file.
def get_files_size(files):
    size_dict = {}
    for file in files:
        try:
            os.path.join(file)                        
        except FileNotFoundError:
            print('{} file does not exist or is innacesible'.format(file))
        else:
            size = getsize(file)
            size_dict[file] = size
    return size_dict      

# Count the files for a given list of files and return the final number        
def get_files_count(files):
    if len(files) > 0:
        total = len(files)
        return total
    else:
        print('The list of files is empty!')

# Create a dictionary for the top 5 size files in the given directory
def get_top_files(size_dict, number_of_files = 5):
    final_dict = dict(sorted(size_dict.items(), key=operator.itemgetter(1), reverse=True)[:number_of_files])
    return final_dict

# Sum the the sizes of each file of a given list of filenames
def get_total_size(files):
    total_size = sum(getsize(f) for f in files)
    return total_size

# Calculate the average size files of a given list of files
def get_average_size(files):
    if len(files) > 0:
        total_files =  get_files_count(files)
        total_size = get_total_size(files)
        average = total_size / total_files
        return round(average)
    else:
        print('The list of files is empty!')

# Initializa the script 
def initialize():
    directory, choice = None, 0
    
    while choice == 0 or choice > 2:
        choice = int(input('Press the number option:\n1. Directory Full Path\n2, Directory Name\n'))
    else:       
        if choice == 1:       
            while not directory:
                input_path = input('Please enter the full path of the directory to be analyze: \n')
                print('\n')
                directory = is_directory(input_path)                
        elif choice == 2:
            while not directory:
                input_path = input('Please enter the name of the directory to be analyze: \n')
                print('\n')
                directory = find_directory(input_path)
                

    files           = get_files_from_directory(directory)
    total_files     = get_files_count(files)
    total_size      = get_total_size(files)
    average_size    = get_average_size(files)
    sizes           = get_files_size(files)
    top_files       = get_top_files(sizes)

    print(f'Total files: {total_files}', end='  ')
    print(f'Total size: {total_size}', end='    ')
    print(f'Average file size: {average_size}')
    print('Top Files: ')
    for file, size in top_files.items():
        """ file = os.path.basename(file) """
        print(f'{file} ', end='==> ')
        print(f'{size} kb')
        


        
if __name__ == "__main__":
    initialize()