import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("p", "This is a paragraph", ["div", "p", "a", "img"], {"href": "https://www.google.com", "style": "font-weight:bold;"})
        node2 = HTMLNode("p", "This is a paragraph", ["div", "p", "a", "img"], {"href": "https://www.google.com", "style": "font-weight:bold;"})
        self.assertEqual(vars(node), vars(node2))

    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"src": "https://www.googleimagelink.com", "type": "text"})
        self.assertEqual(node.props_to_html(), f" src=\"https://www.googleimagelink.com\" type=\"text\"")

    def test_leafnode_to_html_no_children(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leafnode_to_html_w_children(self):
        node = LeafNode("p", "This is a paragraph of text.", {"style": "font-weight:bold;"})
        node2 = LeafNode("p", "This is a paragraph of text.", {"style": "font-weight:bold;"})
        self.assertEqual(node.to_html(), node2.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()