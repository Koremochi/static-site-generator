import unittest

from htmlnode import *



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

    def test_leafnode_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parentnode_to_html_nested_parent(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("a", "link", {"href": "www.cute.com"}),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode("i", "italic text")
                    ]
                ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><p><a href="www.cute.com">link</a>Normal text<i>italic text</i><i>italic text</i></p>Normal text<i>italic text</i>Normal text</p>')

    def test_parentnode_to_html_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertTrue("tag needs to be provided" in str(context.exception))


    def test_parentnode_to_html_no_children(self):
        node = ParentNode(
            "p",
            []
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertTrue("children need to be provided" in str(context.exception))


if __name__ == "__main__":
    unittest.main()