#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or isinstance (roman_string, str) == False:
        return 0

    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    prev_digit = 1000

    for letter in roman_string:
        # case of IX or similar cases
        # subtract the lower letter (I in this case)
        # once to undo last step and other to acheive subtaction
        if numbers[letter] > prev_digit:
            ans -= prev_digit * 2
            prev_digit = numbers[letter]

        prev_digit = numbers[letter]
        ans += numbers[letter]

    return ans
