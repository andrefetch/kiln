from __future__ import annotations

class HTMLNode:

    '''
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    '''

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict | None = None
    ) -> None:

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:

        result: str = ""

        if self.props is None:
            return ""

        for key, value in self.props.items():
            result += f' {key}="{value}"'

        return result

    def __repr__(self) -> str:

        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props: dict | None = None,
    ):
        super().__init__(
            tag,
            value,
            props=None,
        )

    def to_html(self) -> str:

        if self.value is None:
            raise ValueError(
                "All leaf nodes must have a value."
            )

        if self.tag is None:
            return self.value
        else:
            return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"

    def __repr__(self) -> str:

        return f"LeafNode({self.tag}, {self.value}, {self.props})"
