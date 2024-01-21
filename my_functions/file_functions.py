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

    # check is file_ist is a list
    assert isinstance(file_list, list), "file_list must be of type list"

    