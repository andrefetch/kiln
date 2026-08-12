from __future__ import annotations
from enum import Enum

class TextType(Enum):

    PLAIN_TEXT = 'plain_text'
    BOLD_TEXT = 'bold_text' # **Bold**
    ITALIC_TEXT = 'italic_text' # _Italic_
    CODE_TEXT = 'code_text' # `code`
    LINKS = 'links' # [anchor text](url)
    IMAGES = 'images' # ![alt text](url)

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
