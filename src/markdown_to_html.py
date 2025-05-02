from src.htmlnode import ParentNode, NodeType
from src.markdown_block import markdown_to_blocks, block_to_block_type, BlockType
from src.textnode import text_node_to_html_node, TextNode, TextType
from src.markdown_inline import text_to_textnodes
from typing import Sequence


def markdown_to_html_node(md: str) -> NodeType:
    list_of_blocks = markdown_to_blocks(md)
    list_of_block_nodes = []
    
    for block in list_of_blocks:
        list_of_block_nodes.append(block_to_html_node(block))

    return ParentNode("div", list_of_block_nodes, None)


def block_to_html_node(block: str) -> NodeType:
    """create an html node from a markdown block"""    
    block_type = block_to_block_type(block)
    
    match block_type:
        
        case BlockType.CODE:
            #! Stripping ``` from code markdown
            block = block.replace("```", "")
            #! Striping first \n from code markdown
            block = block.replace("\n","", 1)
        
            return ParentNode("pre", [text_node_to_html_node(TextNode(block, TextType.CODE, None))], None)
    
        case BlockType.PARAGRAPH:
            return ParentNode("p", text_to_children(block), None)
        
        case BlockType.HEADING:
            heading_tag = get_heading_tag(block)
            return ParentNode(heading_tag, text_to_children(block), None)

        case BlockType.QUOTE:
            return ParentNode("blockquote", text_to_children(block), None)
    
        case BlockType.ORDERED_LIST:
            return ParentNode("ol", text_to_children(block), None)
            
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul", text_to_children(block), None)
            
    
def get_heading_tag(s: str) -> str:
    """markdown heading -> html heading"""
    if s.startswith("# "):
        return "h1"
    if s.startswith("## "):
        return "h2"
    if s.startswith("### "):
        return "h3"
    if s.startswith("#### "):
        return "h4"
    if s.startswith("##### "):
        return "h5"
    return "h6"
    
    
def text_to_children(s: str) -> Sequence[NodeType]:
    """given text, return list of HTML block node's child HTML nodes"""
    while "\n" in s:
        s = s.replace("\n", " ")   
    
    list_of_text_nodes = text_to_textnodes(s)
    list_of_html_nodes = []
    
    for text_node in list_of_text_nodes:
        list_of_html_nodes.append(text_node_to_html_node(text_node))
        
    return list_of_html_nodes


    