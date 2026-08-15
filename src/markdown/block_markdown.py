from enum import Enum
from re import L

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

def block_to_block_type(markdown: str):

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
