import os

def get_all_files(root_folder: str, file_list: list):
    """
    Find all files in the root_folder and all its subfolders.
    root_folder: (str) The folder to start the search
    file_list: (list) An empty list to collect files
    """

    # check root_folder type
    assert isinstance(root_folder, str), "root_folder must be of type string"
    
    # Check folder validity
    assert os.path.exists(root_folder), f"Path does not exist: {root_folder}"

    # Check if root_folder is a folder
    assert os.path.isdir(root_folder), f"root_folder must be a folder: {root_folder}"

    # check is file_ist is a list
    assert isinstance(file_list, list), "file_list must be of type list"

    root_folder_content = os.listdir(root_folder)

    subfolders = []

    # collect files and subfolders
    for i in root_folder_content:
        full_path = os.path.join(root_folder, i)
        if os.path.isfile(full_path):
            file_list.append(full_path)
        else:
            subfolders.append(full_path)

    for folder in subfolders:
        get_all_files(folder, file_list)