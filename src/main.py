from textnode import TextNode
from htmlnode import *

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
