#!/usr/bin/python3

for tens in range(10):
    for ones in range(tens + 1, 10):
        if tens * 10 + ones < 99:
            print(str(tens * 10 + ones).zfill(2), end=", ")
        else:
            print(str(tens * 10 + ones).zfill(2))
