import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_(self):
        node = HTMLNode()
        node.props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        correct =' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), correct)