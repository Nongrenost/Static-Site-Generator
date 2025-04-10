import pytest
from src.inline import split_nodes_delimiter
from src.textnode import TextNode, TextType



def test_split_nodes_delimiter_code() -> None:
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    result = [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
    ]
    assert new_nodes == result
    
def test_split_nodes_delimiter_links() -> None:
    node = TextNode("Some anchoring text", TextType.LINK)
    new_nodes = split_nodes_delimiter([node], "`", TextType.LINK)
    result = [TextNode("Some anchoring text", TextType.LINK)] 
    
    assert new_nodes == result
    
def test_split_nodes_delimiter_code_single_text() -> None:
    node = TextNode("Text", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.TEXT) 
    result = [TextNode("Text", TextType.TEXT)]
    
    assert new_nodes == result
    
def test_split_nodes_delimiter_bold_text() -> None:
    node = TextNode("Text", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.TEXT)
    result = [TextNode("Text", TextType.TEXT)]
    
    assert new_nodes == result
    
def test_split_nodes_delimiter_italic_text() -> None:
    node = TextNode("Text", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.TEXT)
    result = [TextNode("Text", TextType.TEXT)]
    
    assert new_nodes == result
    
def test_split_nodes_delimiter_code_broken() -> None:
    node = TextNode("`some code without second delimiter", TextType.TEXT)
    with pytest.raises(ValueError, match="Wrong markdown syntax, delimiter misses its pair"):
        split_nodes_delimiter([node], "`", TextType.CODE) 
    
        
def test_split_nodes_bold() -> None:
    node = TextNode("This is text with **bold text** words", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    result = [
    TextNode("This is text with ", TextType.TEXT),
    TextNode("bold text", TextType.BOLD),
    TextNode(" words", TextType.TEXT),
    ]
    
    assert new_nodes == result
    
def test_split_nodes_italic() -> None:
    node = TextNode("This is text with _italic text_ words", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    result = [
    TextNode("This is text with ", TextType.TEXT),
    TextNode("italic text", TextType.ITALIC),
    TextNode(" words", TextType.TEXT),
    ]
    
    assert new_nodes == result
    
def test_split_node_codeblock_with_other_delimiters() -> None:
    node = TextNode('`hello_string = "Hello, World!"`', TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    result = [TextNode('hello_string = "Hello, World!"', TextType.CODE)]
    
    assert new_nodes == result
