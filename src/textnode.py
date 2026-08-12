from __future__ import annotations

from enum import Enum

from src.htmlnode import LeafNode


class TextType(Enum):

    TEXT = 'text'
    BOLD = 'bold' # **Bold**
    ITALIC = 'italic' # _Italic_
    CODE = 'code' # `code`
    LINK = 'link' # [anchor text](url)
    IMAGE = 'image' # ![alt text](url)

class TextNode:

    def __init__(
        self,
        text: str,
        text_type: TextType,
        url: str | None = None
    ) -> None:

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(
        self,
        other
    ) -> bool:
        if not isinstance(other, TextNode):
            return NotImplemented
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self) -> str:

        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode):

    if text_node.text_type == TextType.TEXT:
        return LeafNode(
            tag=None,
            value=text_node.text
        )

    if text_node.text_type == TextType.BOLD:
        return LeafNode(
            tag='b',
            value=text_node.text
        )

    if text_node.text_type == TextType.ITALIC:
        return LeafNode(
            tag='i',
            value=text_node.text
        )

    if text_node.text_type == TextType.CODE:
        return LeafNode(
            tag='code',
            value=text_node.text
        )

    if text_node.text_type == TextType.LINK:
        return LeafNode(
            tag='a',
            value=text_node.text,
            props={
                "href": text_node.url
            }
        )

    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            tag='img',
            value='',
            props={
                "src": text_node.url,
                "alt": text_node.text
            }
        )

    if text_node.text_type not in TextType:
        raise Exception("Invalid Text Type")
