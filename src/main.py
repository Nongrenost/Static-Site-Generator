import sys
from src.generator import rewrite_public, generate_pages

def main() -> None:
    basepath = get_basepath()
    
    rewrite_public()
    generate_pages("content", "template.html", "public", basepath)

def get_basepath() -> str:
    if len(sys.argv) > 1:
        basepath = sys.argv[1] 
        return basepath
    else:
        return "/"
    
if __name__ == "__main__":
    main()