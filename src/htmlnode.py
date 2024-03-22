class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NonImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""

        props_to_html_string = ""
        for key, value in self.props.items():
            props_to_html_string += f' {key}="{value}"'

        return props_to_html_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        leafnode = self.value
        if self.value is None:
            raise ValueError("LeafNode needs to have a value")
        if self.tag is None:
            return leafnode
        leafnode = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return leafnode

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

        

        


