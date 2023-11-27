#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    lines = []
    index = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            lines.append(text[index:i+1].strip())
            index = i+1
    if index != len(text):
        lines.append(text[index:])

    print('\n\n'.join(lines))
