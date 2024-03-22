from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
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