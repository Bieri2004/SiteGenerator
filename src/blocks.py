from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    blocks = []
    for block in raw_blocks:
        stripped = block.strip()
        if stripped == "":
            continue
        blocks.append(stripped)
    return blocks


def block_to_block_type(block):
    # block ist bereits .strip()'ed
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if block.startswith("#"):
        count = 0
        for ch in block:
            if ch == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and len(block) > count and block[count] == " ":
            return BlockType.HEADING

    lines = block.split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    is_ordered = True
    expected_number = 1
    for line in lines:
        prefix = f"{expected_number}. "
        if not line.startswith(prefix):
            is_ordered = False
            break
        expected_number += 1

    if is_ordered and len(lines) > 0:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
