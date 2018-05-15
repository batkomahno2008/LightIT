import sys

# define roman digits values
ROMAN_DIGITS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def main():
    # ensure argument specified
    try:
        input_string = sys.argv[1].upper()
    except:
        # if argument not specified than print usage
        print("usage: python roman_converter.py number")
        exit(1)
    # check input and select required action
    if input_string.isdigit():
        print(arabic_to_roman(int(input_string)))
    elif is_roman(input_string):
        print(roman_to_arabic(input_string))
    elif input_string == 'HELP':
        help_call()
    else:
        incorrect_format()


# function that print help and exit program
def help_call():
    help_message = """

Usage: python roman_converter.py number

This program converts roman positive number (integer) to arabic number or arabic number to roman number, depend on input number 
in command line argument

- - -

To convert roman number to arabic number use rules:

DIGITS:
Symbol	   I  	V   X   L   C   D   M
Value	   1	5   10  50  100 500 1,000

There are only 7 rules of subtraction:
IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900

Some of digits (I, X, C, M) may repeat, but not more than three times

- - - 

To convert arabic number to roman number just use any positive integer. Max number is 3999

To learn more visit: 
https://en.wikipedia.org/wiki/Roman_numerals
    """
    print(help_message)
    exit(0)


# function that checks if input is a roman number
def is_roman(input_string):
    for char in input_string:
        if char not in ROMAN_DIGITS.keys():
            return 0
    for digit in ROMAN_DIGITS:
        if digit * 4 in input_string:
            return 0
    return 1


# function that convert roman number to arabic number
def roman_to_arabic(roman_number):
    arabic_number = 0
    # check rules and calculate number
    if roman_number.__len__() == 1:
        return ROMAN_DIGITS[roman_number]
    for index in range(roman_number.__len__()):
        # check incorrect rules
        if index < roman_number.__len__() - 1:
            if (roman_number[index] == ('I') and roman_number[index + 1] in ('L', 'C', 'D', 'M')) or \
                    (roman_number[index] == ('V') and roman_number[index + 1] in ('V', 'X', 'L', 'C', 'D', 'M')) or \
                    (roman_number[index] == ('X') and roman_number[index + 1] in ('D', 'M')) or \
                    (roman_number[index] == ('L') and roman_number[index + 1] in ('L', 'C', 'D', 'M')) or \
                    (roman_number[index] == ('D') and roman_number[index + 1] in ('D', 'M')):
                incorrect_format()
        # subtraction rule
        if index < roman_number.__len__() - 1:
            if (roman_number[index] == ('I') and roman_number[index + 1] in ('X', 'V')) or \
                    (roman_number[index] == ('X') and roman_number[index + 1] in ('L', 'C')) or \
                    (roman_number[index] == ('C') and roman_number[index + 1] in ('D', 'M')):
                # check incorrect rules in subtraction rule
                if index > 0:
                    if (roman_number[index] == ('I') and roman_number[index - 1] == ('I') and roman_number[
                        index + 1] in ('X', 'V')) or \
                            (roman_number[index] == ('X') and roman_number[index - 1] == ('X') and roman_number[
                                index + 1] in ('L', 'C')) or \
                            (roman_number[index] == ('C') and roman_number[index - 1] == ('C') and roman_number[
                                index + 1] in ('D', 'M')):
                        incorrect_format()
                arabic_number -= ROMAN_DIGITS[roman_number[index]]
                continue
        arabic_number += ROMAN_DIGITS[roman_number[index]]

    return arabic_number


# function that convert arabic number to roman number
def arabic_to_roman(arabic_number):
    # ensure the number less than 4000
    if not arabic_number < 4000:
        print('Max roman number is 3999')
        exit(3)
    # define rules for all orders
    ROMAN_DIGITS_ORDERS = ({1: 'M', 4: '', 5: '', 9: ''}, {1: 'C', 4: 'CD', 5: 'D', 9: 'CM'},
                           {1: 'X', 4: 'XL', 5: 'L', 9: 'XC'}, {1: 'I', 4: 'IV', 5: 'V', 9: 'IX'})
    roman_number = ''
    # iterate orders of number and write it in string
    for n in range(4):
        temp = arabic_number // (1000 / (10 ** n))
        if temp in (4, 9):
            roman_number += ROMAN_DIGITS_ORDERS[n][temp]
            temp = 0
        roman_number += ROMAN_DIGITS_ORDERS[n][5] * int(temp // 5)
        roman_number += ROMAN_DIGITS_ORDERS[n][1] * int(temp % 5)
        arabic_number %= 1000 / (10 ** n)
    return roman_number


def incorrect_format():
    print("""Unfortunately input is neither correct roman number nor arabic number.
To help execute: python roman_converter help""")
    exit(2)


if __name__ == "__main__":
    main()
