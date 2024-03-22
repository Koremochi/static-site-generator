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
