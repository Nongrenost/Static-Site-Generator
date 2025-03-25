from typing import TypeAlias
from typing import Sequence

NodeType: TypeAlias = 'LeafNode | ParentNode'

class HTMLNode():
    """represent a "node" in an HTML document tree, block or inline
    """
    def __init__(self, tag: str | None = None, value: str | None = None, children: Sequence["HTMLNode"] | None = None, props: dict[str, str] | None  = None) -> None:
        self.tag = tag              # tag name string # None tag will just render as raw text
        self.value = value          # value of the html tag # if None node assumed to have children
        self.children = children    # a list of node's children # if None node assumed to have a value
        self.props = props          # key-value pairs representing the attributes of the HTML tag
        #{"href": "https://www.google.com"}
        
        
    def to_html(self) -> str:
        """child classes override to render as html"""
        raise NotImplementedError
    
    def props_to_html(self) -> str | None:
        """ returns html attributes as a string
        """
        if self.props is None:
            return ""
        prop_str = "" 
        
        for key, value in self.props.items():
            prop_str += f' {key}="{value}"'
        
        return prop_str
    
    def __repr__(self) -> str:
            return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        
class LeafNode(HTMLNode):
    """represents a single HTML tag with no children"""
    def __init__(self, tag:str | None, value:str | None, props: dict[str,str] | None = None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    """represents HTML node with children"""
    def __init__(self, tag:str, children:Sequence[NodeType], props: dict[str,str] | None = None) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Parentnode missing a tag")
        if self.children is None:
            raise ValueError("Childnode is missing a value")

        result ="" 
        for child in self.children:
            result += child.to_html()
                   
        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'    


    
    