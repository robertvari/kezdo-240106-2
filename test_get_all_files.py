from my_functions.file_functions import get_all_files

root_folder = r"D:\Work\_PythonSuli\kezdo-240106"
file_list = []
get_all_files(root_folder, file_list, extension=".py")

for i in file_list:
    print(i)