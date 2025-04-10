from src.textnode import TextType, TextNode
from typing import List

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    """split 'text' textnodes by delimiter into textnodes with correct text type"""

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

