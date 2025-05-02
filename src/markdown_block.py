from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(block: str) -> BlockType:
    """given markdown block, returns its type"""
    lines = block.split("\n")
    
    headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(headings):
        return BlockType.HEADING
    
    if block.startswith('```') and block.endswith('```') and len(lines) > 1:
            return BlockType.CODE
    
    if lines[0].startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE 
            
    if lines[0].startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST   
    
    if lines [0].startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST 
    
    return BlockType.PARAGRAPH
    


def markdown_to_blocks(text: str) -> list[str]:
    """given a valid markdown text, break it into blocks separated by an empty line"""
    splitted= text.split("\n\n")
    stripped = []
    for block in splitted:
        if block == "":
            continue
        stripped.append(block.strip())
    
    return stripped