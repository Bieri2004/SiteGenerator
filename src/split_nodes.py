from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # nur TEXT-Nodes werden gesplittet
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        for alt, url in images:
            split_str = f"![{alt}]({url})"
            sections = text.split(split_str, 1)
            before = sections[0]
            after = sections[1]

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            text = after

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        for anchor, url in links:
            split_str = f"[{anchor}]({url})"
            sections = text.split(split_str, 1)
            before = sections[0]
            after = sections[1]

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(anchor, TextType.LINK, url))

            text = after

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
