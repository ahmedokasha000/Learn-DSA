"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from enum import IntEnum


class TextHeader(IntEnum):
    SENDER = 0,
    RECEIVER = 1,
    TS = 2,


class CallHeader(IntEnum):
    CALLER = 0,
    RECEIVER = 1,
    TS = 2,
    DURATION = 3,


def task4():
    text_sending_numbers, text_receiving_numbers = set(), set()
    caller_numbers, called_numbers = set(), set()
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        for text_rec in reader:
            text_sending_numbers.add(text_rec[TextHeader.SENDER])
            text_receiving_numbers.add(text_rec[TextHeader.RECEIVER])

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        for call_rec in reader:
            if not call_rec[CallHeader.CALLER].startswith('140'):
                caller_numbers.add(call_rec[CallHeader.CALLER])
            called_numbers.add(call_rec[CallHeader.RECEIVER])
    # print(f"length of callers {len(caller_numbers)} length of called {len(called_numbers)}")
    # print(f"length of senders {len(text_sending_numbers)} length of txt receivers {len(text_receiving_numbers)}")
    res_set = caller_numbers - called_numbers - text_receiving_numbers - text_sending_numbers

    # print(f"length of result {len(res_set)}")
    print("These numbers could be telemarketers: ")
    print(*sorted(res_set), sep='\n')
    # print(res_set)


def main():
    task4()


if __name__ == '__main__':
    main()
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
