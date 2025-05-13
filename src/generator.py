import os
import shutil
from src.markdown_to_html import markdown_to_html_node


    
def rewrite_public() -> None:
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
        
        if os.path.isdir(item_fullpath):
            shutil.rmtree(item_fullpath)
        else:           
            os.remove(item_fullpath)
                
    
def copy_content(source_path: str, dest_path: str) -> None:
    
    folder_contents = os.listdir(source_path)
    
    for file_path in folder_contents:
        source_file_path = os.path.join(source_path, file_path)
        dest_file_path = os.path.join(dest_path, file_path)
        
        if os.path.isfile(source_file_path):
            shutil.copy(source_file_path, dest_file_path)
            
        else:
            os.path.isdir(source_file_path)
            
            os.mkdir(dest_file_path) 
            copy_content(source_file_path, dest_file_path)
    
    
def log_file(file_path: str, operation: str, filepath2: str|None = None) -> None:
    if operation == "d":
        print(f"Deleting {file_path}")
    if operation == "c":
        print(f"Copying {file_path} to {filepath2}")
        
def extract_title(md_file: str) -> str:
    """return title (value of h1 heading) from markdown text"""
    heading = md_file.split("\n\n")[0]
    if not heading.startswith("# "):
        raise ValueError("Markdown file misses an H1 heading")
    else:
        return heading.replace("# ", "")
    
def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    """generate an html page from a markdown file at the dest_path using template.html"""
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    text= ""
    with open(from_path) as f:
        text = f.read()
    title = extract_title(text)
    html_text = markdown_to_html_node(text).to_html()
    
    template = ""
    with open(template_path) as f:
        template = f.read()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_text)
    
    
    path_with_html_extension = f"{os.path.splitext(dest_path)[0]}.html"
    
    html_text_to_file(template, path_with_html_extension)
    
    #if os.path.exists(dest_path):
    #   html_text_to_file(template, dest_path)
    #else:
    #   os.mkdir(dest_path)
    #   html_text_to_file(template, dest_path)
       
    
def html_text_to_file(html_text: str, path: str) -> None:
    """write html text into a file"""
    
    with open(path, "w") as f:
        f.write(html_text)
    
def generate_pages_recursively(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    """generate HTML pages for all markdown documents"""
    folder_content = os.listdir(dir_path_content)
    for file_name in folder_content:
        
        source_file_path = os.path.join(dir_path_content, file_name)
        dest_file_path = os.path.join(dest_dir_path, file_name)
        
        if os.path.isfile(source_file_path):
            generate_page(source_file_path, template_path, dest_file_path)
        
        if os.path.isdir(source_file_path):
            os.mkdir(dest_file_path)
            generate_pages_recursively(source_file_path, template_path, dest_file_path)
        
    
    