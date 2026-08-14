def markdown_to_blocks(markdown):

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
