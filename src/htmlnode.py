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
    def __init__(self, tag, value, props=None):
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

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag needs to be provided")
        if not self.children:
            raise ValueError("children need to be provided")
        parent_opening_tag = f"<{self.tag}{self.props_to_html()}>"
        parent_closing_tag = f"</{self.tag}>"
        children_string = ""

        for i in range(0, len(self.children)):
            children_string += self.children[i].to_html()

        return parent_opening_tag + children_string + parent_closing_tag
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"





        

        


