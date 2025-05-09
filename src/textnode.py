from enum import Enum
from src.htmlnode import LeafNode

class TextType(Enum):
    """Types of inline markdown text"""
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"  
    
class TextNode:
    """An intermediate representation of an inline markdown element"""
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text           #The text content of the node
        self.text_type = text_type #The type of text from TextType enum.
        self.url = url             #The URL if type link or image, else None
        #TextNode(This is some anchor text, link, https://www.google.com)
        
    def __eq__(self, other: object) -> bool:
        """return true if objects are equal"""
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    """coverts TextNode to an HTMLNode(LeafNode)"""
   
    match text_node.text_type:
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        
        case TextType.CODE:
            return LeafNode("code", text_node.text, None)
        
        case TextType.IMAGE:
            assert text_node.url is not None
            
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        
        case TextType.LINK:
            assert text_node.url is not None
            
            return LeafNode("a", text_node.text, {"href": text_node.url})
        
        case TextType.TEXT:
            return LeafNode(None, text_node.text, None)
        
        case _:
            raise ValueError(f"{text_node.text_type} type is of invalid type")
        