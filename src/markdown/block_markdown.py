from enum import Enum

from src.markdown.inline_markdown import text_to_textnodes
from src.nodes.htmlnode import HTMLNode, ParentNode
from src.nodes.textnode import TextNode, TextType, text_node_to_html_node

class BlockType(Enum):

    PARAGRAPH = 'paragraph' # no conditions met: normal text is paragraph
    HEADING = 'heading' # (#)
    CODE = 'code' # ``` \n ```
    QUOTE = 'quote' # >
    UNORDERED_LIST = 'unordered_list' # -
    ORDERED_LIST = 'ordered_list' # (number) + . ex : 1.

def markdown_to_blocks(markdown: str) -> list:

    stripped_blanks = []
    filtered_blocks = []

    split_blank = markdown.split("\n\n")

    for splits in split_blank:
        stripped_blanks.append(splits.strip())

    for stripped in stripped_blanks:
        if stripped == "":
            continue
        else:
            filtered_blocks.append(stripped)

    return filtered_blocks

def block_to_block_type(markdown: str) -> Enum:

    i = 1
    lines = markdown.split("\n")

    if markdown.startswith(
        ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    ):
        return BlockType.HEADING

    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE

    if markdown.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH

        return BlockType.QUOTE

    if markdown.startswith('- '):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH

        return BlockType.UNORDERED_LIST

    if markdown.startswith(f"{i}. "):
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1

        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def text_to_children(text: str) -> list[HTMLNode]:

    children = []

    for text_node in text_to_textnodes(text):
        children.append(text_node_to_html_node(text_node))

    return children

def paragraph_to_html_node(block: str) -> ParentNode:

    # a paragraph can span several lines: markdown collapses them into one
    paragraph = " ".join(block.split("\n"))

    return ParentNode(
        "p",
        text_to_children(paragraph)
    )

def heading_to_html_node(block: str) -> ParentNode:

    level = 0

    for char in block:
        if char != "#":
            break
        level += 1

    if level + 1 >= len(block):
        raise ValueError(
            f"Found: invalid heading level: {level}"
        )

    text = block[level + 1:] # skips the hashes plus the space after them

    return ParentNode(
        f"h{level}",
        text_to_children(text)
    )

def code_to_html_node(block: str) -> ParentNode:

    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError(
            "Found: invalid code block, please fence it with ```."
        )

    text = block[3:-3].lstrip("\n") # drops the fences and the newline after the opener

    # code blocks are literal: no inline markdown parsing happens in here
    code = text_node_to_html_node(TextNode(
        text,
        TextType.TEXT
    ))

    return ParentNode(
        "pre",
        [ParentNode("code", [code])]
    )

def quote_to_html_node(block: str) -> ParentNode:

    stripped_lines = []

    for line in block.split("\n"):
        stripped_lines.append(line.lstrip(">").strip())

    quote = " ".join(stripped_lines)

    return ParentNode(
        "blockquote",
        text_to_children(quote)
    )

def unordered_list_to_html_node(block: str) -> ParentNode:

    items = []

    for line in block.split("\n"):
        text = line[2:] # skips the "- " marker

        items.append(ParentNode(
            "li",
            text_to_children(text)
        ))

    return ParentNode(
        "ul",
        items
    )

def ordered_list_to_html_node(block: str) -> ParentNode:

    items = []

    for i, line in enumerate(block.split("\n"), start=1):
        text = line[len(f"{i}. "):] # skips the "1. ", "2. ", ... marker

        items.append(ParentNode(
            "li",
            text_to_children(text)
        ))

    return ParentNode(
        "ol",
        items
    )

def block_to_html_node(block: str) -> ParentNode:

    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)

    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)

    if block_type == BlockType.CODE:
        return code_to_html_node(block)

    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)

    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)

    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)

    raise ValueError(
        f"Found: unknown block type: {block_type}"
    )

def markdown_to_html_node(markdown: str) -> ParentNode:

    children = []

    for block in markdown_to_blocks(markdown):
        children.append(block_to_html_node(block))

    return ParentNode(
        "div",
        children
    )
