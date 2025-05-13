from src.generator import rewrite_public, generate_pages_recursively

def main() -> None:
    rewrite_public()
    generate_pages_recursively("content", "template.html", "public")

if __name__ == "__main__":
    main()