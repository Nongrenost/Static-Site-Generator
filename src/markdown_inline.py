from src.textnode import TextType, TextNode
from typing import List
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    """split 'text' textnodes by delimiter into a list of textnodes with correct text type"""

    result = []
    # iterate over input list
    for node in old_nodes:

        if delimiter not in node.text: 
            #deal with non-TEXT nodes
            result.append(node)
            continue
        
        splitted = node.text.split(delimiter)
        #check is there are any non-paired delimiters
        if len(splitted) % 2 == 0:
            raise ValueError("Wrong markdown syntax, delimiter misses its pair")
        
        # create new nodes
        for s in range(0, len(splitted)):
            if splitted[s] == "":
                continue
            if s % 2 == 0:
               result.append(TextNode(splitted[s], TextType.TEXT))
            else:
                result.append(TextNode(splitted[s], text_type))
                
    return result

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """return a list of (alt text, image_url) pairs from markdown string"""
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    result = re.findall(pattern, text)
    return result

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """return a list of (alt text, link_url) pairs from markdown string"""
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"   
    result = re.findall(pattern, text)
    return result

def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    """given list of textnodes, split its text into list of text and image textnodes"""
       
    result = []
    
    for old_node in old_nodes:
        text = old_node.text
        
        if text == "":
            result.append(TextNode(text, TextType.TEXT))
            continue
    
        while text:
            images = extract_markdown_images(text)
            
            if old_node.text_type != TextType.TEXT:
                result.append(old_node)
                break
            
            if not extract_markdown_images(text):
                result.append(TextNode(text,TextType.TEXT))
                break
            
            delimiter = f"![{images[0][0]}]({images[0][1]})"
            splitted = text.split(delimiter, 1)
            
            if len(splitted) % 2 != 0:
                ValueError("Wrong markdown link syntax")
            chunk = ""
            
            if splitted[0] == "":
                result.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))
                chunk = delimiter
            else:
                result.append(TextNode(splitted[0], TextType.TEXT))
                chunk = splitted[0]
            text = text.removeprefix(chunk)
            
    return result
        
def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    """given list of textnodes, split its text into list of text and link textnodes"""

    result = []
    
    for old_node in old_nodes:
        text = old_node.text
        
        if text == "":
            result.append(TextNode(text, TextType.TEXT))
            continue
        
        while text:
            links = extract_markdown_links(text)
            
            if old_node.text_type != TextType.TEXT:
                result.append(old_node)
                break
            
            if not extract_markdown_links(text):
                result.append(TextNode(text,TextType.TEXT))
                break
            
            delimiter = f"[{links[0][0]}]({links[0][1]})"
            splitted = text.split(delimiter, 1)
            
            if len(splitted) % 2 != 0:
                ValueError("Wrong markdown link syntax")
            chunk = ""
            
            if splitted[0] == "":
                result.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
                chunk = delimiter
            else:
                result.append(TextNode(splitted[0], TextType.TEXT))
                chunk = splitted[0]
            text = text.removeprefix(chunk)
            
    return result


def text_to_textnodes(text: str) -> list[TextNode]:
    """given markdown text, return a list of Text nodes"""
    old_textnode = [TextNode(text, TextType.TEXT)]
    
    bold_nodes = split_nodes_delimiter(old_textnode, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    image_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(image_nodes)

    
    return link_nodes
