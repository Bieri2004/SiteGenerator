class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html must be implemented by subclasses")

    def props_to_html(self):
        if not self.props:
            return ""
        parts = []
        for key, val in self.props.items():
            parts.append(f'{key}="{val}"')
        return " " + " ".join(parts)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

