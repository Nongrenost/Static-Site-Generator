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
        
from src.htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    
def test_parent_simple() -> None:
    parent = ParentNode("div", [
    LeafNode("p", "Paragraph text"),
    LeafNode("span", "Span text")
    ])    
    assert parent.to_html() == '<div><p>Paragraph text</p><span>Span text</span></div>'
    
def test_parentnode_to_html_multiple_leafs() -> None:
    assert ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    ).to_html() == "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    
def test_parentnode_to_html_nested_parentnode() -> None:
    children = [LeafNode("b", "Bold text")]
    child_parent_node = [ParentNode("p", children, None)]
    assert ParentNode("p", child_parent_node, None).to_html() == "<p><p><b>Bold text</b></p></p>"
    
def test_parentnode_to_html_with_children() -> None:
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() == "<div><span>child</span></div>"

def test_parentnode_to_html_with_grandchildren() -> None:
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() =="<div><span><b>grandchild</b></span></div>"