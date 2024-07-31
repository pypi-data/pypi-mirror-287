#Sort files in a directory based on their extensions
__all__=['sort_files','find_extensions']

def find_extensions(dir:str):
    """
    Finds all the file types in the given directory.
    """
    import os
    extensions=set()
    for filename in os.listdir(dir):
        ext=os.path.splitext(filename)[1]
        if ext:
            extensions.add(ext)
    return extensions

def sort_files(dir_to_sort:str, extensions:dict[str,str]):
    """
    Sort files in the given directory based on their extensions.
    
    ## Args:
    dir_to_sort (str): Path to the directory to sort\n
    extensions (dict ["extensions":"folder_name"] ): Dictionary mapping file extensions to folder names
    
    ### Example:
    
    extensions={
        'c':'code',
        'cpp':'code',
        'txt':'documents',
        'pdf':'documents',
        'png':'images'
    }
    
    Returns:
    dict: A summary of the sorting operation
    """
    summary={"moved": 0,"skipped": 0,"errors": 0}
    import os
    import shutil
    from colorama import Fore as fc
    def __create_folders(base_dir, folders):
        """Create folders if they don't exist."""
        for folder in set(folders):
            folder_path=os.path.join(base_dir, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
    
    # Create necessary folders
    __create_folders(dir_to_sort,extensions.values())
    
    # Sort files
    for filename in os.listdir(dir_to_sort):
        file_path = os.path.join(dir_to_sort,filename)
        if os.path.isfile(file_path):
            # Get the file extension
            ext=os.path.splitext(filename)
            ext=ext[1:]  # Remove the dot
            
            if ext in extensions:
                # Get the destination folder
                dest_folder=os.path.join(dir_to_sort, extensions[ext])
                dest_path=os.path.join(dest_folder, filename)
                
                try:
                    # Move the file
                    shutil.move(file_path,dest_path)
                    print(f"{fc.GREEN}Moved {filename} to {dest_folder}")
                    summary["moved"]+= 1
                except Exception as e:
                    print(f"{fc.RED}Error moving {filename}: {str(e)}")
                    summary["errors"]+= 1
            else:
                print(f"{fc.BLUE}No defined folder for {filename}")
                summary["skipped"]+= 1
    
    return summary