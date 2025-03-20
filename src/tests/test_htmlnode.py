"""import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode()
        node.props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        correct =' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), correct)"""
        
from src.htmlnode import HTMLNode, LeafNode

def test_props_to_html() -> None:
    assert HTMLNode(None, None, None, {
    "href": "https://www.google.com",
    "target": "_blank",}).props_to_html() ==  ' href="https://www.google.com" target="_blank"'
    
    
    
def test_HTMLNode_repr() -> None:
    assert repr(HTMLNode("h1", "Text value", None, {"href": "https://www.google.com"})) == "HTMLNode(h1, Text value, children: None, {'href': 'https://www.google.com'})"
    
def test_leafnode_to_html_p() -> None:
    assert LeafNode("p", "This is a paragraph of text.").to_html() == '<p>This is a paragraph of text.</p>'
    
    
def test_leafnode_to_html_link() -> None:
    assert LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html() == '<a href="https://www.google.com">Click me!</a>'