from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # alles, was kein reiner TEXT ist, unverändert übernehmen
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # Wenn die Anzahl Teile ungerade ist, muss sie >= 1 sein.
        # Für gültige Paare von Delimitern brauchen wir eine **ungerade** Anzahl Teile:
        # Text, markiert, Text, markiert, Text, ...
        if len(parts) % 2 == 0:
            # gerade Anzahl => es existiert ein öffnendes ohne schließendes Delimiter
            raise Exception(f"Invalid markdown, unmatched delimiter '{delimiter}' in '{node.text}'")

        # Teile in neue Nodes umwandeln
        for i, part in enumerate(parts):
            if part == "":
                # leere Teile überspringen (z.B. wenn Text direkt mit Delimiter beginnt)
                continue

            if i % 2 == 0:
                # gerade Indizes: normaler Text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # ungerade Indizes: Text innerhalb der Delimiter
                new_nodes.append(TextNode(part, text_type))

    return new_nodes
