#!/usr/bin/python3

def remove_char_at(str, n):
    if (n > 0):
        ans = ''
        ans += str[:n]
        ans += str[n + 1:]
    else:
        ans = str
    return ans
