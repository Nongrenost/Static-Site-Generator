from htmlnode import HTMLNode

"""class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super.__init__(tag=self.tag, value=self.value, chilren=None)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        return f"{self.tag}"""