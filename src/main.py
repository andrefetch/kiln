from textnode import TextNode, TextType

def main():

    return TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")


if __name__ == "__main__":

    print(main())
