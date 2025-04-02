from src.textnode import TextType, TextNode
from typing import List

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    return [TextNode("This is a text node", TextType.BOLD, None)]

