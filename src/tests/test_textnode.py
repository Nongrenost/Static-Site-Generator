from src.textnode import TextNode, TextType


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
    
    assert TextNode("This is a text node", TextType.BOLD, "https://google.com") != TextNode("This is a text node", TextType.BOLD)


def test_eq_not_equal_text_type() -> None:

    assert TextNode("This is a text node", TextType.BOLD) != TextNode("This is a text node", TextType.CODE)

def test_repr() -> None:
    assert repr(TextNode("This is some anchor text", TextType.LINK, "https://www.google.com")) == "TextNode(This is some anchor text, TextType.LINK, https://www.google.com)"

"""if __name__ == "__main__":
    unittest.main()"""