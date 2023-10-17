import os


def CntFiles(path):
    no_of_files = 0
    ls = os.listdir(path)
    for file in ls:
        if os.path.isfile(os.path.join(path, file)):
            no_of_files += 1;

    return no_of_files;


def CntFilesRecursive(path):
    no_of_files = 0;
    no_of_files += CntFiles(path)
    ls = os.listdir(path)
    file_paths = [os.path.join(path, file) for file in ls]
    for file in file_paths:
        if os.path.isdir(file):
            no_of_files += CntFilesRecursive(file)

    return no_of_files;



print(str(CntFilesRecursive("."))) 

