"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    longest_call = next(reader)
    for call_record in reader:
        if (int(call_record[CallHeader.DURATION]) > int(longest_call[CallHeader.DURATION])):
            longest_call = call_record
    print(f"{longest_call[CallHeader.RECEIVER]} spent the longest time, {longest_call[CallHeader.DURATION]} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016.".
"""
