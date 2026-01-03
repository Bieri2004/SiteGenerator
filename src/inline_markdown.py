from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link
from split_delimiter import split_nodes_delimiter  # deine Funktion aus der Delimiter-Lesson


def text_to_textnodes(text):
    # Starte mit einem einzigen TEXT-Node
    nodes = [TextNode(text, TextType.TEXT)]

    # Reihenfolge ist wichtig: zuerst Code, dann Bold, dann Italic
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    # Danach Images und Links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
