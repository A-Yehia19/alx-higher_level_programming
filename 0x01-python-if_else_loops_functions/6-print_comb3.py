#!/usr/bin/python3

for tens in range(10):
    for ones in range(tens + 1, 10):
        num = tens * 10 + ones
        print(str(num).zfill(2), end=", " if num < 99 else "\n")
