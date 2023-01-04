"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

from enum import IntEnum
import parse


class TextHeader(IntEnum):
    SENDER = 0,
    RECEIVER = 1,
    TS = 2,


class CallHeader(IntEnum):
    CALLER = 0,
    RECEIVER = 1,
    TS = 2,
    DURATION = 3,


class PhoneType(IntEnum):
    FIXED = 0,
    MOBILE = 1,
    TELEMAR = 2,


class PhoneNumber():
    fixed_line_parser = parse.compile("({prefix}){number}")
    mobile_parser = parse.compile("{prefix_plus_digit} {number}")
    telemark_parser = parse.compile("140{number}")

    def __init__(self, raw_val):
        self._type = None
        self._prefix = None
        self._raw_value = raw_val
        self._number = None

    @property
    def type(self):
        return self._type

    @property
    def prefix(self):
        return self._prefix

    @property
    def raw_value(self):
        return self._raw_value

    @property
    def number(self):
        return self._number

    def process(self):
        res = self.fixed_line_parser.parse(self.raw_value)
        if res is not None:
            self._type = PhoneType.FIXED
            self._prefix = res['prefix']
            self._number = res['number']
            return
        res = self.mobile_parser.parse(self.raw_value)
        if res is not None:
            self._type = PhoneType.MOBILE
            self._prefix = res['prefix_plus_digit'][:4]
            self._number = res['prefix_plus_digit'][4:] + res['number']
            return
        res = self.telemark_parser.parse(self.raw_value)
        if res is not None:
            self._type = PhoneType.TELEMAR
            self._prefix = '140'
            self._number = res['number']
            return
        raise Exception(' Could not parese given number')


# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

def task3():
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        bangalore_code = '(080)'
        area_mobile_prefixes = set()
        calls_from_bang_count = 0
        calls_from_to_bang_count = 0
        for rec in reader:
            if rec[CallHeader.CALLER].startswith(bangalore_code):
                calls_from_bang_count += 1
                called_number = PhoneNumber(rec[CallHeader.RECEIVER])
                called_number.process()
                if called_number.type != PhoneType.TELEMAR:
                    area_mobile_prefixes.add(called_number.prefix)
                    if called_number.type == PhoneType.FIXED and called_number.prefix == '080':
                        calls_from_to_bang_count += 1

        print(f"The numbers called by people in Bangalore have codes:")
        print(*sorted(area_mobile_prefixes), sep="\n")
        print(f"{calls_from_to_bang_count/(calls_from_bang_count+1e-7):.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


def main():
    task3()


if __name__ == '__main__':
    main()

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
