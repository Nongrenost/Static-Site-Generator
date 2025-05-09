import os
import shutil



    #delete everything inside public until empty
    # copy everything from static into public
    # log the path of each file copied to debug
    # add public dir to gitignore
    #test
    
def generate_website() -> None:
    """delete all files in public, then copy all files from static into public"""
    public_path = "/home/liras/workspace/Github.com/Nongrenost/Static-Site-Generator/public"
    static_path = "/home/liras/workspace/Github.com/Nongrenost/Static-Site-Generator/static"
    
    delete_contents(public_path)
    copy_content(static_path, public_path)
   
    

    
def delete_contents(path:str) -> None:
    """recursively delete everything in public folder"""
    public_content = os.listdir(path)
    
    for item in public_content:
        item_fullpath = os.path.join(path, item)
        
        log_file(item_fullpath, "d") 
        shutil.rmtree(item_fullpath)
                
    
def copy_content(static_path: str, public_path: str) -> None:
    
    folder_contents = os.listdir(static_path)
    
    for item in folder_contents:
        item_abs_path = os.path.join(static_path, item)
        destination_abs_path = os.path.join(static_path, item)
        
        if os.path.isfile(item_abs_path):
            log_file(item_abs_path, "c", destination_abs_path)
            
            shutil.copy(item_abs_path, destination_abs_path)
        elif os.path.isdir(item_abs_path):
            
            log_file(item_abs_path, "c", destination_abs_path) 
            shutil.copy(item_abs_path, destination_abs_path)
            
            copy_content(item_abs_path, destination_abs_path)
    
    
def log_file(file_path: str, operation: str, filepath2: str|None = None) -> None:
    if operation == "d":
        print(f"Deleting {file_path}")
    if operation == "c":
        print(f"Copying {file_path} to {filepath2}")
    