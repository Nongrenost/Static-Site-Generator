from src.textnode import TextNode, TextType, text_node_to_leaf_node
from src.htmlnode import LeafNode


"""class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a node", TextType.BOLD)
        self.assertNotEqual(node, node2)"""
        
def test_eq_equal() -> None:
    
    assert TextNode("This is a text node", TextType.BOLD) == TextNode("This is a text node", TextType.BOLD)
    
    
def test_eq_not_equal() -> None:
    
    assert TextNode("", TextType.BOLD) != TextNode("This is a text node", TextType.BOLD)
    
    
def test_eq_not_equal_url() -> None:
    
    assert TextNode("Some anchoring text", TextType.LINK, "https://google.com") != TextNode("Some anchoring text", TextType.LINK)


def test_eq_type_not_equal() -> None:

    assert TextNode("This is a text node", TextType.BOLD) != TextNode("This is a text node", TextType.CODE)

def test_repr() -> None:
    assert repr(TextNode("This is some anchor text", TextType.LINK, "https://www.google.com")) == "TextNode(This is some anchor text, TextType.LINK, https://www.google.com)"
    
    
def test_text_node_to_html_text() -> None:
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_leaf_node(node)
    assert html_node.tag is None
    assert html_node.value, "This is a text node"
    
    
def test_text_type_to_html_bold() -> None:
    
    assert text_node_to_leaf_node(TextNode("bold text", TextType.BOLD)) == LeafNode("b", "bold text", None)
        
def test_text_type_to_html_italic() -> None:
    text_node = TextNode("italic text", TextType.ITALIC)
    to_leaf_node = text_node_to_leaf_node(text_node)
    leaf_node = LeafNode("i", "italic text", None)
    assert to_leaf_node == leaf_node
    
def test_text_type_to_html_link() -> None:
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.google.com")
    to_leaf_node = text_node_to_leaf_node(text_node)
    leaf_node = LeafNode("a", "This is some anchor text", {"href": "https://www.google.com"} )
    assert to_leaf_node == leaf_node

def test_text_type_to_html_img() -> None:
    text_node = TextNode("some alt text", TextType.IMAGE, "https://www.google.com/lol.png")
    to_leaf_node = text_node_to_leaf_node(text_node)
    leaf_node = LeafNode("img", "", {"src": "https://www.google.com/lol.png", "alt": "some alt text"})
    assert to_leaf_node == leaf_node
    
def test_text_type_to_html_code() -> None:
    text_node = TextNode('Print("hello world")', TextType.CODE, None) 
    to_leaf_node = text_node_to_leaf_node(text_node)
    leaf_node = LeafNode("code", 'Print("hello world")', None) 
    assert to_leaf_node == leaf_node
