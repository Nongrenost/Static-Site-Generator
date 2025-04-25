import pytest
from src.inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
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

def test_extract_markdown_images() -> None:
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    extracted = extract_markdown_images(text)
    result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    assert extracted == result
    

def test_extract_markdown_links() -> None:
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    extracted = extract_markdown_links(text)
    result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    assert extracted == result
    
def test_split_nodes_link() -> None:
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT)
    splitted = split_nodes_link([node])
    result = [
     TextNode("This is text with a link ", TextType.TEXT),
     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
     TextNode(" and ", TextType.TEXT),
     TextNode(
         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
     )]
    assert splitted == result
    
    
def test_split_nodes_image6() -> None:
    node = TextNode(
        "TEXT1",
        TextType.TEXT)
    splitted = split_nodes_image([node])
    result = [
            TextNode("TEXT1", TextType.TEXT),
            ]
    assert splitted == result
    
    
def test_split_nodes_image7() -> None:
    node = TextNode(
        "![IMAGE1](https://i.imgur.com/zjjcJKZ.png)",
        TextType.TEXT)
    splitted = split_nodes_image([node])
    result = [
            TextNode("IMAGE1", TextType.IMAGE,"https://i.imgur.com/zjjcJKZ.png"),
            ]
    assert splitted == result

def test_split_nodes_image8() -> None:
    node = TextNode(
        "TEXT1 ![IMAGE1](https://i.imgur.com/zjjcJKZ.png)",
        TextType.TEXT)
    splitted = split_nodes_image([node])
    result = [
            TextNode("TEXT1 ", TextType.TEXT),
            TextNode("IMAGE1", TextType.IMAGE,"https://i.imgur.com/zjjcJKZ.png"),
            ]
    assert splitted == result
    
def test_split_nodes_image() -> None:
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT)
    splitted = split_nodes_image([node])
    result = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ]
    assert splitted == result
    
def test_split_nodes_image2() -> None:
    node = TextNode(
        "![IMAGE1](https://i.imgur.com/zjjcJKZ.png) ![IMAGE2](https://i.imgur.com/3elNhQu.png) TEXT1",
        TextType.TEXT)
    splitted = split_nodes_image([node])
    result = [
            TextNode("IMAGE1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("IMAGE2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode(" TEXT1", TextType.TEXT)
            ]
    assert splitted == result

def test_split_nodes_image3() -> None:
    node = TextNode(
        "TEXT1 ![IMAGE1](https://i.imgur.com/zjjcJKZ.png) ![IMAGE2](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT)
    splitted = split_nodes_image([node])
    result = [
            TextNode("TEXT1 ", TextType.TEXT),
            TextNode("IMAGE1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("IMAGE2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ]
    assert splitted == result

def test_split_nodes_image4() -> None:
    node = TextNode(
        "TEXT1 ![IMAGE1](https://i.imgur.com/zjjcJKZ.png) TEXT2 ![IMAGE1](https://i.imgur.com/zjjcJKZ.png)",
        TextType.TEXT)
    splitted = split_nodes_image([node])
    result = [
            TextNode("TEXT1 ", TextType.TEXT),
            TextNode("IMAGE1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" TEXT2 ", TextType.TEXT),
            TextNode("IMAGE1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ]
    assert splitted == result
    
def test_split_nodes_image5() -> None:
    node = TextNode(
        "TEXT1 ![IMAGE1](https://i.imgur.com/zjjcJKZ.png) ![IMAGE2](https://i.imgur.com/3elNhQu.png) ![IMAGE1](https://i.imgur.com/zjjcJKZ.png)",
        TextType.TEXT)
    splitted = split_nodes_image([node])
    result = [
            TextNode("TEXT1 ", TextType.TEXT),
            TextNode("IMAGE1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("IMAGE2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("IMAGE1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ]
    assert splitted == result

