import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_false(self):
        node3 = TextNode("This is a text node", "italic")
        node4 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node3, node4)
    
    def test_url(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)
    
    def test_url_false(self):
        node3 = TextNode("This is a text node", "bold", None)
        node4 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertNotEqual(node3, node4)

    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()

