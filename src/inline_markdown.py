from src.textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType
) -> list[TextNode]:

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)

            if len(parts) % 2 == 0: # if it splits into an even amount, means there is a non closed tick "`"
                raise Exception(
                    "Found: non closing delimiter, please close it."
                )

            for i, part in enumerate(parts):
                if part == "": # checks if split part is an empty string, if so discard
                    continue

                if i % 2 == 0: # If even, its a normal text type : else a special type (code blocks, etc)
                    node_type = TextType.TEXT
                else:
                    node_type = text_type

                new_nodes.append(TextNode(part, node_type))

    return new_nodes
