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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # children must always be None for a leaf node
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        # No tag: return raw text
        if self.tag is None:
            return self.value

        # Tag with optional props
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # hier KEIN value
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have children")

        # alle Kinder zu HTML konvertieren
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
