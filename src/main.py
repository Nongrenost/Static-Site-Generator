import sys
from src.generator import rewrite_public, generate_pages

def main() -> None:
    basepath = get_basepath()
    site_build_dir = "docs"
    
    rewrite_public(site_build_dir)
    generate_pages("content", "template.html", site_build_dir, basepath)

def get_basepath() -> str:
    if len(sys.argv) > 1:
        basepath = sys.argv[1] 
        return basepath
    else:
        return "/"
    
if __name__ == "__main__":
    main()