from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    # Texttype()
    
class TextNode:
    """An intermediate representation of an inline markdown element
    """
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text           #The text content of the node
        self.text_type = text_type #The type of text this node contains, which is a member of the TextType enum.
        self.url = url             #The URL of the link or image, if the text is a link. Default to None if nothing is passed in. 
        
        #TextNode(This is some anchor text, link, https://www.google.com)
        
    def __eq__(self, other: object) -> bool:
        """
        >>> TextNode("Text", TextType.BOLD) == TextNode("Text", TextType.BOLD)
        True
        >>> TextNode("Text", TextType.BOLD) == TextNode("", TextType.BOLD)
        False
        """
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self) -> str:
        """ print TextNode object in correct format
        >>> repr(TextNode("This is some anchor text", "link", "https://www.google.com")) 
        TextNode(This is some anchor text, link, https://www.google.com)'"""
        
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"