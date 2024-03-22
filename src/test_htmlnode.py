import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("p", "This is a paragraph", ["div", "p", "a", "img"], {"href": "https://www.google.com", "style": "font-weight:bold;"})
        node2 = HTMLNode("p", "This is a paragraph", ["div", "p", "a", "img"], {"href": "https://www.google.com", "style": "font-weight:bold;"})
        self.assertEqual(vars(node), vars(node2))

    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"src": "https://www.googleimagelink.com", "type": "text"})
        self.assertEqual(node.props_to_html(), f" src=\"https://www.googleimagelink.com\" type=\"text\"")

if __name__ == "__main__":
    unittest.main()