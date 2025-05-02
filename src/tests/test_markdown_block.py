import pytest
from src.markdown_block import markdown_to_blocks, block_to_block_type, BlockType

def test_markdown_to_blocks() -> None:
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
    test = markdown_to_blocks(md)
    result = [
        "This is **bolded** paragraph", "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line", "- This is a list\n- with items"]
    assert test == result
        
    
def test_block_to_block_type_paragraph() -> None:
    block = "This is a normal paragraph of text.\nSome more text on the new line."
    test = block_to_block_type(block)
    result = BlockType.PARAGRAPH
    assert test == result
    

def test_block_to_block_type_heading() -> None:
    block = "# Heading"
    test = block_to_block_type(block)
    result = BlockType.HEADING
    assert test == result
    
def test_block_to_block_type_heading3() -> None:
    block = "### Heading"
    test = block_to_block_type(block)
    result = BlockType.HEADING
    assert test == result
    
def test_block_to_block_type_heading6() -> None:
    block = "###### Heading"
    test = block_to_block_type(block)
    result = BlockType.HEADING
    assert test == result

def test_block_to_block_type_not_heading_but_tag() -> None:
    block = "#tag"
    test = block_to_block_type(block)
    result = BlockType.PARAGRAPH
    assert test == result

def test_block_to_block_type_code() -> None:
    block = """```python
Print("Hello World")
```"""
    test = block_to_block_type(block)
    result = BlockType.CODE
    assert test == result

def test_block_to_block_type_quote() -> None:
    block = """> Some quote
> 
> - Name"""
    test = block_to_block_type(block)
    result = BlockType.QUOTE
    assert test == result
    

def test_block_to_block_type_unordered_list() -> None:
    block = """- item
- another item
- yet another item"""
    test = block_to_block_type(block)
    result = BlockType.UNORDERED_LIST
    assert test == result
    

def test_block_to_block_type_ordered_list() -> None:
    block = """1. first
2. second
3. third"""
    test = block_to_block_type(block)
    result = BlockType.ORDERED_LIST
    assert test == result
    
def test_block_to_block_type_ordered_list_broken() -> None:
    block = """1. first
d. wrong
3. third"""
    test = block_to_block_type(block) 
    assert test == BlockType.PARAGRAPH


def test_block_to_block_type_ordered_list_wrong_numeration() -> None:
    block = """1. first
5. second
3. third"""
    test = block_to_block_type(block)
    assert test == BlockType.PARAGRAPH