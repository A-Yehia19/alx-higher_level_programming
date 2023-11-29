#!/usr/bin/python3

"""Module that prints a text with 2 new lines after each of these characters:
    ., ? and :."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
      ., ? and :.

    Args:
        text (str): text to print.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    lines = []
    index = 0
    new_text = text.strip()
    for i in range(len(new_text)):
        if new_text[i] in ['.', '?', ':']:
            lines.append(new_text[index:i+1].strip())
            index = i+1
    if index != len(new_text):
        lines.append(new_text[index:])

    print('\n\n'.join(lines))
