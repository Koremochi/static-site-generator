from textnode import TextNode
from htmlnode import *

def text_node_to_html_node(text_node):
    text_type_list = ["text", "bold", "italic", "code", "link", "image"]
    leaf_node = None
    if not text_node.text_type in text_type_list:
        raise ValueError(f"Invalid text type: {text_node.text_type}")
    elif text_node.text_type == "text":
        leaf_node = LeafNode(None, text_node.text, None)
    elif text_node.text_type == "bold":
        leaf_node = LeafNode("b", text_node.text, None)
    elif text_node.text_type == "italic":
        leaf_node = LeafNode("i", text_node.text, None)
    elif text_node.text_type == "code":
        leaf_node = LeafNode("code", text_node.text, None)
    elif text_node.text_type == "link":
        leaf_node = LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        leaf_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    return leaf_node

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)

    html_node = HTMLNode()
    print(html_node)

    html_node2 = HTMLNode("p", "This is a paragraph", ["div", "p", "a", "img"], {"href": "https://www.google.com", "style": "font-weight:bold;"})
    print(html_node2)
    print(html_node2.props_to_html())
    print(html_node2.props_to_html())

main()
