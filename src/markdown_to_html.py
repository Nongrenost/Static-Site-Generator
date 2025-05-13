import re
from src.htmlnode import ParentNode, NodeType
from src.markdown_block import markdown_to_blocks, block_to_block_type, BlockType
from src.textnode import text_node_to_html_node, TextNode, TextType
from src.markdown_inline import text_to_textnodes
from typing import Sequence


def markdown_to_html_node(md: str) -> ParentNode:
    """convert markdown document into a parent HTML node and it's children"""
    list_of_blocks = markdown_to_blocks(md)
    list_of_children = []
    
    for block in list_of_blocks:
        list_of_children.append(block_to_html_node(block))

    return ParentNode("div", list_of_children, None)


def block_to_html_node(block: str) -> NodeType:
    """create an html node from a markdown block"""    
    block_type = block_to_block_type(block)
    
    match block_type:
        
        case BlockType.CODE:
            #strip ``` from start and end
            #remove newline after first ```
            # wrap in <pre> ParentNode
            #! Stripping ``` from code markdown
            block = block.replace("```", "")
            #! Striping first \n from code markdown
            block = block.replace("\n","", 1)
        
            return ParentNode("pre", [text_node_to_html_node(TextNode(block, TextType.CODE, None))], None)
    
        case BlockType.PARAGRAPH:
            return ParentNode("p", text_to_children(block, block_type), None)
        
        case BlockType.HEADING:
            heading_tag = get_heading_tag(block)
            return ParentNode(heading_tag, text_to_children(block, block_type), None)

        case BlockType.QUOTE:
            return ParentNode("blockquote", text_to_children(block, block_type), None)
    
        case BlockType.ORDERED_LIST:
            
            return ParentNode("ol", text_to_children(block, block_type), None)
            
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul", text_to_children(block, block_type), None)
            
    
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
    
    
def text_to_children(block: str, block_type: BlockType) -> Sequence[NodeType]:
    """given block of markdown text, transform its inline markdown into list of HTMLNodes"""

    #deal with each block type 
    #remove its block markdown syntax
    #remove newlines
    # wrap if needed
    children = []
    
    match block_type:
        case BlockType.HEADING:
            
            
            md_heading = re.search(r"#{1,6}\s", block)
            assert md_heading is not None
            block = block.replace(md_heading.group(), "", 1)
            
            text_nodes = text_to_textnodes(block)
            
            for node in text_nodes:
                children.append(text_node_to_html_node(node))
            
        case BlockType.ORDERED_LIST:
            #? can abstract ordered and unordered into "deal with list(block, func)"
            lines = block.split("\n")
            
            for line in lines:
                md_list_syntax = re.search(r"\d+\.\s", line)
                assert md_list_syntax is not None
                line = line.replace(md_list_syntax.group(), "", 1)
                
                leaf_nodes = []
                
                text_nodes = text_to_textnodes(line)
                for node in text_nodes:
                    leaf_nodes.append(text_node_to_html_node(node))
                    
                children.append(ParentNode("li", leaf_nodes))
            
        case BlockType.UNORDERED_LIST:
            
            lines = block.split("\n")
            for line in lines:
                line = line.replace("- ", "", 1)
                
                leaf_nodes = []
                
                text_nodes = text_to_textnodes(line)
                for node in text_nodes:
                    leaf_nodes.append(text_node_to_html_node(node))
                    
                children.append(ParentNode("li", leaf_nodes))

        case BlockType.QUOTE:
           
            lines = block.split("\n")
            stripped_lines = []
            text_nodes = []
            leaf_nodes = []
            
            for line in lines:
                stripped_lines.append(line.replace("> ", "", 1))
                
            text_nodes = text_to_textnodes("\n".join(stripped_lines))
            for node in text_nodes:
                node.text = node.text.replace("\n", " ")
                children.append(text_node_to_html_node(node))
         
        case BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            text_nodes = text_to_textnodes(block)
            for node in text_nodes:
                children.append(text_node_to_html_node(node))
    
    return children