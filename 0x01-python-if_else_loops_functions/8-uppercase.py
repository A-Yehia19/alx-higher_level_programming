#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if 'a' <= letter <= 'z':
            letter = chr(ord(letter) - 32)
        
        print(letter, end='')
    print()
