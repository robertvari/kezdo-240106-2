import os
from my_functions.file_functions import get_all_files

def main():
    clear_screen()
    print("-"*50, "Get Proto Data", "-"*50)

    folder_path = get_root_folder()
    image_list = collect_photos(folder_path)
    photo_data = collect_data(image_list)
    # save_data(photo_data)

def get_root_folder():
    # folder_path = input("Where are your photos?")
    folder_path = r"D:\Work\_PythonSuli\kezdo-240106\alapok_1\photos"

    assert os.path.isdir(folder_path), f"This is not a valid folder: {folder_path}"

    return folder_path

def collect_photos(folder_path):
    file_list = []
    get_all_files(folder_path, file_list, extension=".jpg")
    return file_list

def collect_data(image_list):
    return {}

def save_data(photo_data):
    pass

def clear_screen():
    os.system("cls")  #linux, mac: os.system("clear")


main()